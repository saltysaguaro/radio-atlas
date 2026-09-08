#!/usr/bin/env python3
"""Refresh Radio Atlas using public Radio Browser metadata and bounded HTTPS probes."""
import concurrent.futures as futures
import collections, datetime, ipaddress, json, math, pathlib, re, socket, subprocess, sys, time, unicodedata
from urllib.parse import urlsplit, urljoin

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'website/public/data'
DOC = ROOT / 'documents'
NOW = datetime.datetime.now(datetime.timezone.utc)
AGENT = 'RadioAtlas/1.0 (public radio catalog; bounded stream checks)'

def fetch(url):
    p = subprocess.run(['curl', '-fLsS', '--max-time', '120', '--retry', '2', '-A', AGENT, url], capture_output=True, check=True)
    return json.loads(p.stdout)

def public_addresses(url):
    """Resolve once and pin curl to the checked addresses (including redirects)."""
    try:
        u = urlsplit(url)
        if u.scheme != 'https' or not u.hostname or u.username is not None or u.password is not None:
            return []
        if any(ord(c) < 33 for c in url): return []
        addresses = sorted({a[4][0] for a in socket.getaddrinfo(u.hostname, u.port or 443, type=socket.SOCK_STREAM)})
        return addresses if addresses and all(ipaddress.ip_address(a).is_global and not ipaddress.ip_address(a).is_multicast for a in addresses) else []
    except (ValueError, OSError): return []

def safe_url(url):
    return bool(public_addresses(url))

def normalized(name):
    name = unicodedata.normalize('NFKD', name).lower()
    name = re.sub(r'\b\d+\s*(kbps|kbit|mp3|aac)\b|\b(mp3|aac|aac\+|hd|stream|online)\b', '', name)
    return re.sub(r'[^a-z0-9\u0080-\uffff]+', '', name)

def endpoint_urls(station):
    urls=[]
    for value in (station.get('url'),station.get('url_resolved')):
        if not isinstance(value,str): continue
        try:
            u=urlsplit(value.strip())
            if u.scheme not in ('http','https') or not u.hostname or u.username is not None or u.password is not None: continue
            # Test TLS on the same address; never request the insecure feed.
            url=u._replace(scheme='https',fragment='').geturl()
            if url not in urls: urls.append(url)
        except ValueError: continue
    return sorted(urls,key=lambda url: not any(url==v for v in (station.get('url'),station.get('url_resolved'))))

def probe_endpoint(url):
    current=url
    for redirect in range(6):
        addresses=public_addresses(current)
        if not addresses: return {'ok':False,'reason':'unsafe_or_unresolvable_address'}
        u=urlsplit(current)
        host=u.hostname
        pinned=','.join('['+a+']' if ':' in a else a for a in addresses)
        args=['curl','--disable','-sS','--noproxy','*','--max-time','9','--connect-timeout','5','--proto','=https',
              '--resolve',f'{"["+host+"]" if ":" in host else host}:{u.port or 443}:{pinned}',
              '-A',AGENT,'-D','-',current]
        p=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
        header=b'';data=b''
        try:
            while len(header)<16384:
                line=p.stdout.readline(16385-len(header))
                if not line: break
                header+=line
                if line in (b'\r\n',b'\n'): break
            h=header.decode('latin1')
            status=re.search(r'^HTTP/[\d.]+ (\d+)',h,re.I)
            status=int(status.group(1)) if status else 0
            location=re.search(r'^location:\s*([^\r\n]+)',h,re.I|re.M)
            mime_match=re.search(r'^content-type:\s*([^\r\n;]+)',h,re.I|re.M)
            mime=mime_match.group(1).strip().lower() if mime_match else ''
            if status in (200,206) and mime in ('audio/mpeg','audio/mp3','audio/aac','audio/aacp','audio/ogg','application/ogg'):
                data=p.stdout.read(4096)
        finally:
            p.terminate()
            try:p.wait(timeout=2)
            except subprocess.TimeoutExpired:p.kill();p.wait()
            p.stdout.close()
        if status in (301,302,303,307,308):
            if not location or redirect==5:return {'ok':False,'reason':'redirect_limit_or_missing_location'}
            current=urljoin(current,location.group(1).strip());continue
        if status not in (200,206):return {'ok':False,'reason':'http_or_connection_failure','status':status}
        if mime not in ('audio/mpeg','audio/mp3','audio/aac','audio/aacp','audio/ogg','application/ogg'):
            return {'ok':False,'reason':'unsupported_response_type','contentType':mime}
        if len(data)<4096:return {'ok':False,'reason':'insufficient_audio_sample'}
        if data.lstrip().lower().startswith((b'<html',b'<!doctype',b'{',b'#extm3u')):
            return {'ok':False,'reason':'non_audio_body'}
        return {'ok':True,'finalUrl':current,'verification':{'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'contentType':mime,'sampleBytes':len(data),'httpsRedirects':redirect,'publicAddressPinned':True}}
    return {'ok':False,'reason':'redirect_limit_or_missing_location'}

def probe(station):
    for url in endpoint_urls(station):
        result=probe_endpoint(url)
        if result['ok']:
            return {**station,'_url':url,'_probe':result['verification'],'_finalUrl':result['finalUrl']}
    return None

def main():
    OUT.mkdir(parents=True, exist_ok=True); DOC.mkdir(exist_ok=True)
    geo = fetch('https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson')
    countries = {}
    features = []
    for f in geo['features']:
        p = f['properties']; code = p.get('ISO_A2_EH') or p.get('ISO_A2')
        if not code or code == '-99':
            code = {'Kosovo':'XK', 'Somaliland':'SO', 'N. Cyprus':'CY'}.get(p['NAME'])
        if not code or code in countries: continue
        lat, lon = p.get('LABEL_Y', 0), p.get('LABEL_X', 0)
        countries[code] = {'code':code, 'name':p.get('NAME_EN') or p['ADMIN'], 'lat':lat, 'lon':lon, 'region':p['CONTINENT']}
        features.append({'type':'Feature','properties':{'code':code, 'name':countries[code]['name']},'geometry':f['geometry']})
    # Add ISO territories too small for this map's polygon resolution.
    iso = fetch('https://raw.githubusercontent.com/mledoze/countries/master/countries.json')
    for c in iso:
        code = c['cca2']
        if code not in countries:
            lat, lon = c['latlng']
            countries[code] = {'code':code, 'name':c['name']['common'], 'lat':lat, 'lon':lon, 'region':c['region']}
    (OUT/'world.geojson').write_text(json.dumps({'type':'FeatureCollection','features':features}, separators=(',',':')))
    cached='--cached-source' in sys.argv
    host='de1.api.radio-browser.info'
    if cached:
        raw=json.loads((DOC/'source-snapshot.json').read_text())
    else:
        raw=None
        # A full snapshot avoids shifting offsets in popularity-sorted pagination.
        # Broken/stale metadata is also included: our own live probe decides availability.
        for host in ('de1.api.radio-browser.info','de2.api.radio-browser.info','at1.api.radio-browser.info'):
            try:
                raw=fetch(f'https://{host}/json/stations?limit=100000&hidebroken=false')
                if not isinstance(raw,list) or len(raw)<10000:raise ValueError('Incomplete snapshot')
                offset=100000
                while len(raw)>=offset:
                    page=fetch(f'https://{host}/json/stations?limit=100000&hidebroken=false&offset={offset}')
                    if not page:break
                    raw.extend(page);offset+=100000
                break
            except Exception:print(f'Mirror unavailable: {host}',flush=True)
        if not isinstance(raw,list) or len(raw)<10000:raise RuntimeError('Incomplete directory response; previous catalog preserved.')
        (DOC/'source-snapshot.json').write_text(json.dumps(raw,separators=(',',':')))
    raw=list({s['stationuuid']:s for s in raw}.values())
    supplemental=json.loads((DOC/'supplemental-stations.json').read_text())
    raw.extend({**s,'stationuuid':s['id'],'countrycode':s['country'],'language':','.join(s['languages']),'tags':','.join(s['tags'])} for s in supplemental)
    url_countries=collections.defaultdict(set)
    for s in raw:
        for url in endpoint_urls(s):url_countries[url].add(s.get('countrycode'))
    suspicious={url for url,codes in url_countries.items() if len(codes)>5}
    exclusions=collections.Counter();candidates=[];endpoints={}
    for s in sorted(raw,key=lambda s:(-s.get('clickcount',0),-s.get('votes',0),s['stationuuid'])):
        if s.get('countrycode') not in countries:exclusions['unknown_country']+=1;continue
        if not (s.get('name') or '').strip():exclusions['missing_name']+=1;continue
        urls=endpoint_urls(s)
        if any(u in suspicious for u in urls):exclusions['ambiguous_country']+=1;continue
        if not urls:exclusions['no_https_candidate']+=1;continue
        candidates.append((s,urls))
        for url in urls:endpoints.setdefault(url,None)
    print(f'Source: {len(raw)} records; {len(candidates)} candidates; {len(endpoints)} unique endpoints. No country cap.',flush=True)
    # Append-only resumable evidence. Only checks younger than 24 hours are reusable.
    cache_path=DOC/'endpoint-checks.jsonl';cache={}
    if cache_path.exists() and '--fresh-checks' not in sys.argv:
        for line in cache_path.read_text().splitlines():
            try:
                row=json.loads(line);age=(datetime.datetime.now(datetime.timezone.utc)-datetime.datetime.fromisoformat(row['checkedAt'])).total_seconds()
                if 0<=age<86400:cache[row['url']]=row
            except (ValueError,KeyError):continue
    pending=[u for u in endpoints if u not in cache]
    print(f'Reusing {len(endpoints)-len(pending)} recent checks; probing {len(pending)} endpoints.',flush=True)
    # Interleave hosts to avoid bursts; also enforce eight simultaneous connections per host.
    import threading
    host_limits=collections.defaultdict(lambda:threading.Semaphore(8))
    by_host=collections.defaultdict(collections.deque)
    for url in pending:by_host[urlsplit(url).hostname].append(url)
    pending=[]
    while by_host:
        for host_key in list(by_host):
            pending.append(by_host[host_key].popleft())
            if not by_host[host_key]:del by_host[host_key]
    def check(url):
        with host_limits[urlsplit(url).hostname]:
            try:result=probe_endpoint(url)
            except Exception:result={'ok':False,'reason':'probe_error'}
        return {'url':url,'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),**result}
    with cache_path.open('a') as log, futures.ThreadPoolExecutor(max_workers=128) as executor:
        jobs={executor.submit(check,url) for url in pending}
        passed=0
        for n,job in enumerate(futures.as_completed(jobs),1):
            row=job.result();cache[row['url']]=row;passed+=row['ok']
            log.write(json.dumps(row,separators=(',',':'))+'\n');log.flush()
            if n%250==0 or n==len(pending):print(f'Checked {n}/{len(pending)} endpoints; {passed} passed.',flush=True)
    catalog=[];seen_urls=set();reports=[];candidate_counts=collections.Counter(s['countrycode'] for s,_ in candidates)
    for s,urls in candidates:
        result=next((cache[u] for u in urls if cache[u]['ok']),None)
        if not result:exclusions['no_passing_endpoint']+=1;continue
        if result['url'] in seen_urls or result['finalUrl'] in seen_urls:exclusions['duplicate_stream']+=1;continue
        seen_urls.update((result['url'],result['finalUrl']))
        lat,lon=s.get('geo_lat'),s.get('geo_long')
        located=all(isinstance(v,(int,float)) and math.isfinite(v) for v in (lat,lon)) and -90<=lat<=90 and -180<=lon<=180 and (lat!=0 or lon!=0)
        mime=result['verification']['contentType']
        codec='AAC' if 'aac' in mime else 'OGG' if 'ogg' in mime else 'MP3'
        entry={'id':s['stationuuid'],'name':s['name'].strip(),'country':s['countrycode'],'url':result['url'],
               'tags':[t.strip() for t in s.get('tags','').split(',') if t.strip()][:8],
               'languages':[t.strip() for t in s.get('language','').split(',') if t.strip()][:4],
               'region':s.get('state','').strip(),'lat':lat if located else None,'lon':lon if located else None,
               'locationSource':'directory' if located else 'country','codec':codec,'bitrate':s.get('bitrate',0),
               'clicks':s.get('clickcount',0),'votes':s.get('votes',0),'sourceCheckedAt':s.get('lastcheckoktime_iso8601'),
               'source':s.get('source','https://www.radio-browser.info/'),'verification':result['verification']}
        if result['url'] not in (s.get('url'),s.get('url_resolved')):entry['originalDirectoryUrl']=s.get('url_resolved') or s.get('url')
        catalog.append(entry)
    counts=collections.Counter(s['country'] for s in catalog)
    for c in countries.values():c['stationCount']=counts[c['code']]
    metadata={'generatedAt':NOW.isoformat(),'completedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source':'https://www.radio-browser.info/','sourceApi':host,'stationCount':len(catalog),
        'countriesWithStations':len(counts),'countriesAtTarget':sum(n>=10 for n in counts.values()),
        'totalCountriesAndTerritories':len(countries),'countryStationLimit':None,'sourceRecords':len(raw),
        'candidateRecords':len(candidates),'checkedEndpoints':len(endpoints),'sourceWasCached':cached,
        'sourceRetrievedAt':datetime.datetime.fromtimestamp((DOC/'source-snapshot.json').stat().st_mtime,datetime.timezone.utc).isoformat(),
        'verification':'HTTPS with valid TLS, pinned public addresses at every redirect, direct audio content type and a 4096-byte sample. Point-in-time availability; not editorial certification or guaranteed playback.',
        'ranking':'All passing distinct feeds, ordered by directory clicks and votes; no per-country limit. Not national audience ratings.'}
    if len(catalog)<100:raise RuntimeError('Unexpectedly small result; existing catalog preserved.')
    atomic_json(OUT/'catalog.json',{'metadata':metadata,'countries':sorted(countries.values(),key=lambda c:c['name']),'stations':catalog})
    atomic_json(DOC/'discovery-report.json',{'metadata':metadata,'recordExclusions':dict(exclusions),
        'endpointOutcomes':dict(collections.Counter('passed' if cache[u]['ok'] else cache[u]['reason'] for u in endpoints)),
        'failedStatusCodes':dict(collections.Counter(str(cache[u]['status']) for u in endpoints if 'status' in cache[u])),
        'unsupportedContentTypes':dict(collections.Counter(cache[u]['contentType'] for u in endpoints if cache[u].get('reason')=='unsupported_response_type')),
        'coverage':[{'code':c['code'],'candidates':candidate_counts[c['code']],'verified':c['stationCount']} for c in countries.values()]})
    print(json.dumps(metadata,indent=2),flush=True)

def atomic_json(path,data):
    temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
    temporary.replace(path)

if __name__ == '__main__': main()
