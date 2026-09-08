#!/usr/bin/env python3
import collections, json, pathlib, re, http.server, threading, urllib.request
root=pathlib.Path(__file__).resolve().parents[1]
site=root/'website'
data=json.loads((site/'public/data/catalog.json').read_text())
stations=data['stations']; countries={c['code']:c for c in data['countries']}
assert len(stations)==data['metadata']['stationCount']
assert data['metadata']['countryStationLimit'] is None
assert data['metadata']['checkedEndpoints'] > 0
assert len({s['id'] for s in stations})==len(stations),'Duplicate station IDs'
assert len({s['url'] for s in stations})==len(stations),'Duplicate stream URLs'
counts=collections.Counter(s['country'] for s in stations)
checks={row['url']:row for row in map(json.loads,(root/'documents/endpoint-checks.jsonl').read_text().splitlines())}
for s in stations:
    assert checks[s['url']]['ok'] and checks[s['url']]['verification']==s['verification']
    assert s['url'].startswith('https://')
    assert s['country'] in countries
    assert s['verification']['sampleBytes']>=4096
    assert s['verification']['publicAddressPinned'] is True
    assert s['verification']['contentType'].startswith(('audio/','application/ogg'))
    assert bool(s['lat'] is None)==bool(s['lon'] is None)
    if s['lat'] is not None: assert -90<=s['lat']<=90 and -180<=s['lon']<=180
for code,c in countries.items(): assert c['stationCount']==counts[code]
report=json.loads((root/'documents/discovery-report.json').read_text())
assert report['metadata']['stationCount']==len(stations)
assert sum(report['endpointOutcomes'].values())==data['metadata']['checkedEndpoints']
assert sum(row['verified'] for row in report['coverage'])==len(stations)
assert report['preLocationStationCount']-report['locationExclusions']==len(stations)
world=json.loads((site/'public/data/world.geojson').read_text())
for feature in world['features']: assert feature['properties']['code'] in countries
assert len(countries)>=249,'Missing world coverage entries'
dist=site/'dist';html=(dist/'index.html').read_text()
for url in re.findall(r'(?:src|href)="([^"]+)"',html):
    if not url.startswith(('http','#')):
        assert not url.startswith('/'),f'Root-absolute asset breaks subfolder hosting: {url}'
        assert (dist/url).exists(),f'Missing asset: {url}'
for path in ('data/catalog.json','data/world.geojson','radio.svg','THIRD-PARTY-NOTICES.txt','.nojekyll'):assert (dist/path).exists()
assert json.loads((dist/'data/catalog.json').read_text())==data
assert json.loads((dist/'data/world.geojson').read_text())==world
assert (dist/'THIRD-PARTY-NOTICES.txt').read_bytes()==(site/'public/THIRD-PARTY-NOTICES.txt').read_bytes()
print(f'PASS: {len(stations)} unique HTTPS streams, {len(counts)} countries with streams, {len(countries)} selectable countries/territories; release files and subfolder asset URLs valid.')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(dist),**kwargs)
    def log_message(self,*args):pass
    def translate_path(self,path):
        for prefix in ('/radio-atlas/', '/renamed-repository/'):
            if path.startswith(prefix):
                path=path[len(prefix)-1:]
                break
        return super().translate_path(path)
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Handler)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
    for prefix in ('/','/radio-atlas/','/renamed-repository/'):
        origin=f'http://127.0.0.1:{server.server_port}{prefix}'
        for path in ['','data/catalog.json','data/world.geojson','radio.svg','THIRD-PARTY-NOTICES.txt']+[u[2:] for u in re.findall(r'(?:src|href)="(\./assets/[^"]+)"',html)]:
            with urllib.request.urlopen(origin+path,timeout=10) as response:
                assert response.status==200,(prefix,path)
                assert len(response.read())>0
    print('PASS: real HTTP responses for page, JS, CSS, catalog, map, icon and notices at /, /radio-atlas/ and /renamed-repository/.')
finally:server.shutdown();server.server_close();thread.join()
