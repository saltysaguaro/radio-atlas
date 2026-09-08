#!/usr/bin/env python3
"""Canonical country labels, complete shared-code geometry, and location sanity checks."""
import collections, json, math
from build_catalog import OUT,DOC,fetch,normalized

def inside(x,y,ring):
    result=False
    for i,(x1,y1) in enumerate(ring):
        x2,y2=ring[i-1]
        if (y1>y)!=(y2>y) and x < (x2-x1)*(y-y1)/(y2-y1)+x1:result=not result
    return result

def main():
    data=json.loads((OUT/'catalog.json').read_text())
    previous=json.loads((DOC/'location-audit.json').read_text()) if (DOC/'location-audit.json').exists() else {}
    same_refresh=previous.get('catalogGeneratedAt')==data['metadata']['generatedAt']
    audited={s['id']:s for s in previous.get('movedToCountryLocation',[])} if same_refresh else {}
    geo=fetch('https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson')
    iso=fetch('https://raw.githubusercontent.com/mledoze/countries/master/countries.json')
    canonical={c['cca2']:c for c in iso}
    countries={c['code']:c for c in data['countries']}
    for code,c in countries.items():
        if code in canonical:c['name']=canonical[code]['name']['common']
    geometry=collections.defaultdict(list)
    for f in geo['features']:
        p=f['properties'];code=p.get('ISO_A2_EH') or p.get('ISO_A2')
        if code=='-99':code={'Kosovo':'XK','Somaliland':'SO','N. Cyprus':'CY'}.get(p['NAME'])
        if code not in countries:continue
        g=f['geometry'];geometry[code].extend(g['coordinates'] if g['type']=='MultiPolygon' else [g['coordinates']])
    features=[{'type':'Feature','properties':{'code':code,'name':countries[code]['name']},'geometry':{'type':'MultiPolygon','coordinates':polys}} for code,polys in geometry.items()]
    (OUT/'world.geojson').write_text(json.dumps({'type':'FeatureCollection','features':features},separators=(',',':')))
    quarantined=[];excluded=[];stations=[];names=set()
    for s in data['stations']:
        if s['id'] in audited and s['lat'] is None:s.update(lat=audited[s['id']]['sourceLat'],lon=audited[s['id']]['sourceLon'],locationSource='directory')
        if s['lat'] is not None and s['country'] in geometry:
            x,y=s['lon'],s['lat'];polys=geometry[s['country']]
            in_country=any(inside(x,y,p[0]) and not any(inside(x,y,h) for h in p[1:]) for p in polys)
            # Allow coastal stations / cartographic simplification within ~25km.
            near_coast=not in_country and any(((vx-x)*math.cos(math.radians(y)))**2+(vy-y)**2<0.25**2 for p in polys for vx,vy in p[0])
            if not in_country and not near_coast:
                quarantined.append({'id':s['id'],'name':s['name'],'country':s['country'],'sourceLat':y,'sourceLon':x})
                distance=min(((vx-x)*math.cos(math.radians(y)))**2+(vy-y)**2 for p in polys for vx,vy in p[0])
                if distance>9:
                    excluded.append(quarantined.pop());continue
                s.update(lat=None,lon=None,locationSource='country')
        stations.append(s)
    data['stations']=stations;counts=collections.Counter(s['country'] for s in stations)
    for c in countries.values():c['stationCount']=counts[c['code']]
    data['countries']=sorted(countries.values(),key=lambda c:c['name'])
    m=data['metadata'];m.update(stationCount=len(stations),countriesWithStations=len(counts),countriesAtTarget=sum(n>=10 for n in counts.values()),locatedStations=sum(s['lat'] is not None for s in stations))
    (OUT/'catalog.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
    prior=json.loads((DOC/'location-audit.json').read_text()) if (DOC/'location-audit.json').exists() else {}
    excluded = list({s['id']:s for s in (prior.get('excludedForConflictingCountry',[]) if same_refresh else [])+excluded}.values())
    (DOC/'location-audit.json').write_text(json.dumps({'catalogGeneratedAt':m['generatedAt'],'movedToCountryLocation':quarantined,'excludedForConflictingCountry':excluded,'note':'Coordinates outside the assigned country and coastal tolerance are not displayed as station pins. Clearly conflicting country/coordinate records are excluded.'},indent=2))
    if (DOC/'discovery-report.json').exists():
        discovery=json.loads((DOC/'discovery-report.json').read_text())
        discovery.setdefault('preLocationStationCount',discovery['metadata']['stationCount'])
        discovery['metadata']=m
        discovery['locationExclusions']=len(excluded)
        for row in discovery['coverage']:
            row.setdefault('networkVerified',row['verified'])
            row['verified']=counts[row['code']]
        (DOC/'discovery-report.json').write_text(json.dumps(discovery,indent=2))
    (DOC/'verification-report.json').write_text(json.dumps({'metadata':m,'coverage':[{'code':c['code'],'country':c['name'],'verified':c['stationCount']} for c in data['countries']]},indent=2))
    lines=['# Catalog coverage','',f"Refresh completed {m.get('completedAt',m['generatedAt'])}; maintained broadcaster supplements are included in the same sweep.",'',f"{m['stationCount']} checked streams across {m['countriesWithStations']} countries and territories. {m['countriesAtTarget']} have at least 10 streams. {m['locatedStations']} have usable directory coordinates.",'',m['verification'],'',m['ranking'],'','| Country / territory | Checked streams |','|---|---:|']
    lines += [f"| {c['name']} ({c['code']}) | {c['stationCount']} |" for c in data['countries']]
    (DOC/'COVERAGE.md').write_text('\n'.join(lines)+'\n')
    print(f"Final: {len(stations)} streams / {len(counts)} countries and territories; {len(quarantined)} questionable coordinates moved to country-level location.")
if __name__=='__main__':main()
