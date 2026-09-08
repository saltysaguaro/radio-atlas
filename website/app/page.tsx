'use client';
import { useEffect, useLayoutEffect, useMemo, useRef, useState } from 'react';
import L from 'leaflet';
import { Globe2, Radio, Shuffle, Play, Pause, Volume2, VolumeX, ArrowUpRight, LocateFixed, ArrowLeft, Headphones, LoaderCircle } from 'lucide-react';
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from '@/components/ui/select';
import { Input } from '@/components/ui/input';
import { Pagination } from '@/components/ui/pagination';
import { Slider } from '@/components/ui/slider';
import { RadioPlayer } from '../lib/radio-player';
import type { Station, Country, Catalog, PlayerState } from '../lib/types';
import 'leaflet/dist/leaflet.css';
import './globals.css';

const flag = (code:string) => /^[A-Z]{2}$/.test(code) ? String.fromCodePoint(...code.split('').map(c=>127397+c.charCodeAt(0))) : '◎';
const titleCase = (s:string) => s ? s[0].toUpperCase()+s.slice(1) : '';
const safeText = (s:string) => { const e=document.createElement('span'); e.textContent=s; return e; };
const dateLabel = (s:string) => new Date(s).toLocaleDateString(undefined,{month:'short',day:'numeric',year:'numeric'});

export default function Home() {
  const [catalog,setCatalog]=useState<Catalog|null>(null);
  const [loadError,setLoadError]=useState('');
  const [country,setCountry]=useState('');
  const [query,setQuery]=useState('');
  const [page,setPage]=useState(0);
  const pageSize=50;
  const [playerState,setPlayerState]=useState<PlayerState>({status:'idle',station:null,message:''});
  const [volume,setVolume]=useState(()=>{
    try{const saved=Number(localStorage.getItem('radio-atlas-volume')??75);if(Number.isFinite(saved)&&saved>=0&&saved<=100)return saved;}catch{/* optional preference */}
    return 75;
  });
  const initialVolume=useRef(volume);
  const [about,setAbout]=useState(false);
  const [mapError,setMapError]=useState(false);
  const [mapReady,setMapReady]=useState(false);
  const mapNode=useRef<HTMLDivElement>(null);
  const stationScroll=useRef<HTMLDivElement>(null);
  const changePage=(next:number)=>{setPage(next);if(stationScroll.current)stationScroll.current.scrollTop=0;};
  const mapRef=useRef<L.Map|null>(null);
  const shapes=useRef<Map<string,L.GeoJSON>>(new Map());
  const markers=useRef<L.LayerGroup|null>(null);
  const player=useRef<RadioPlayer|null>(null);
  const selectRef=useRef<(code:string)=>void>(()=>{});
  const playRef=useRef<(s:Station)=>void>(()=>{});
  const catalogRef=useRef<Catalog|null>(null);
  const chosen=catalog?.countries.find(c=>c.code===country);
  const countryIndex=useMemo(()=>{
    const index=new Map<string,Station[]>();
    for(const s of catalog?.stations??[]){const entries=index.get(s.country)??[];entries.push(s);index.set(s.country,entries);}
    return index;
  },[catalog]);
  const stations=useMemo(()=>countryIndex.get(country)??[],[countryIndex,country]);
  const filtered=useMemo(()=>{const term=query.trim().toLocaleLowerCase();return term?stations.filter(s=>[s.name,s.region,...s.tags,...s.languages].join(' ').toLocaleLowerCase().includes(term)):stations;},[stations,query]);
  const pageCount=Math.max(1,Math.ceil(filtered.length/pageSize));
  const currentPage=Math.min(page,pageCount-1);
  const visibleStations=filtered.slice(currentPage*pageSize,(currentPage+1)*pageSize);
  const playing=playerState.station;
  const activeCountry=catalog?.countries.find(c=>c.code===playing?.country);
  const setSavedVolume=(next:number)=>{setVolume(next);player.current?.setVolume(next/100);try{localStorage.setItem('radio-atlas-volume',String(next));}catch{/* private browser storage */}};

  useEffect(()=>{
    player.current=new RadioPlayer(setPlayerState);
    player.current.setVolume(initialVolume.current/100);
    const controller=new AbortController();
    fetch('./data/catalog.json',{signal:controller.signal}).then(r=>{if(!r.ok) throw Error();return r.json();}).then((data:Catalog)=>{
      if(!Array.isArray(data.stations)||!data.stations.length||!Array.isArray(data.countries)) throw Error();
      setCatalog(data);catalogRef.current=data;
    }).catch(e=>{if(e.name!=='AbortError')setLoadError('The station catalog could not load. Check your connection and reload.');});
    return ()=>{controller.abort();player.current?.destroy();};
  },[]);

  function selectCountry(code:string){
    setCountry(code);setQuery('');setPage(0);
    const c=catalogRef.current?.countries.find(c=>c.code===code);
    const map=mapRef.current;
    if(!map)return;
    map.stop();
    if(!c){map.flyTo([22,12],2,{duration:0.8});return;}
    const bounds=shapes.current.get(code)?.getBounds();
    if(bounds?.isValid() && bounds.getEast()-bounds.getWest()<180)map.flyToBounds(bounds,{padding:[45,45],maxZoom:7,duration:0.8});
    else map.flyTo([c.lat,c.lon],code==='RU'?3:5,{duration:0.8});
  }
  function playStation(s:Station){
    player.current?.play(s); // Keep play inside the user's gesture for mobile.
    if(country!==s.country){
      selectCountry(s.country);
      const index=(countryIndex.get(s.country)??[]).findIndex(entry=>entry.id===s.id);
      changePage(Math.max(0,Math.floor(index/pageSize)));
    }else{
      const index=filtered.findIndex(entry=>entry.id===s.id);
      if(index>=0)changePage(Math.floor(index/pageSize));
      else{setQuery('');changePage(Math.max(0,Math.floor(stations.findIndex(entry=>entry.id===s.id)/pageSize)));}
    }
  }
  useLayoutEffect(()=>{selectRef.current=selectCountry;playRef.current=playStation;});
  function randomStation(){
    const pool=catalog?.stations.filter(s=>s.id!==playing?.id) ?? [];
    if(pool.length)playStation(pool[Math.floor(Math.random()*pool.length)]);
  }

  useEffect(()=>{
    if(!catalog || !mapNode.current)return;
    const map=L.map(mapNode.current,{center:[22,12],zoom:2,minZoom:2,maxZoom:10,zoomControl:false,attributionControl:true,worldCopyJump:false,maxBounds:[[-85,-210],[85,210]],maxBoundsViscosity:0.8});
    mapRef.current=map;
    const mapShapes=shapes.current;
    L.control.zoom({position:'bottomright'}).addTo(map);
    map.attributionControl.setPrefix(false);
    map.attributionControl.addAttribution('Map: <a href="https://www.naturalearthdata.com/" target="_blank" rel="noopener noreferrer">Natural Earth</a>');
    const grid=L.layerGroup().addTo(map);
    for(let lat=-60;lat<=75;lat+=15)L.polyline([[lat,-180],[lat,180]],{color:'#253847',weight:1,opacity:0.35,interactive:false}).addTo(grid);
    for(let lon=-180;lon<=180;lon+=30)L.polyline([[-85,lon],[85,lon]],{color:'#253847',weight:1,opacity:0.35,interactive:false}).addTo(grid);
    markers.current=L.layerGroup().addTo(map);
    let disposed=false;
    fetch('./data/world.geojson').then(r=>{if(!r.ok)throw Error();return r.json();}).then(data=>{
      if(disposed)return;
      for(const f of data.features){
        const code=f.properties.code;
        const layer=L.geoJSON(f,{style:{fillColor:'#203947',fillOpacity:0.94,color:'#4d6772',weight:0.7},onEachFeature:(_,l)=>{
          l.bindTooltip(safeText(f.properties.name),{sticky:true,className:'atlas-tooltip'});
          l.on('click',()=>selectRef.current(code));
        }}).addTo(map);
        mapShapes.set(code,layer);
      }
      setMapReady(true);
    }).catch(()=>{if(!disposed){setMapError(true);setMapReady(true);}});
    const observer=new ResizeObserver(()=>map.invalidateSize());observer.observe(mapNode.current);
    return ()=>{disposed=true;observer.disconnect();map.remove();mapRef.current=null;mapShapes.clear();};
  },[catalog]);

  useEffect(()=>{
    const map=mapRef.current, group=markers.current;
    if(!catalog||!map||!group||!mapReady)return;
    group.clearLayers();
    shapes.current.forEach((shape,code)=>shape.setStyle({fillColor:code===country?'#355f62':'#203947',color:code===country?'#a5e4b4':'#4d6772',weight:code===country?1.7:0.7}));
    if(!country){
      for(const c of catalog.countries){
        if(!c.stationCount)continue;
        const marker=L.marker([c.lat,c.lon],{icon:L.divIcon({className:'country-beacon',html:`<span>${c.stationCount}</span>`,iconSize:[30,30],iconAnchor:[15,15]}),title:`${c.name}: ${c.stationCount} stations`,keyboard:true});
        marker.bindTooltip(safeText(`${c.name} · ${c.stationCount} stations`),{className:'atlas-tooltip'}).on('click',()=>selectRef.current(c.code)).addTo(group);
      }
    }else{
      const countryStations=countryIndex.get(country)??[];
      const positions=new Map<string,Station[]>();
      for(const s of countryStations){
        if(s.lat===null||s.lon===null)continue;
        const key=`${s.lat.toFixed(3)},${s.lon.toFixed(3)}`;
        const entries=positions.get(key)??[];entries.push(s);positions.set(key,entries);
      }
      const stationList=(entries:Station[],heading:string,note='')=>{
        const list=document.createElement('div');list.className='map-station-list';
        const h=document.createElement('strong');h.textContent=heading;list.append(h);
        if(note){const p=document.createElement('p');p.textContent=note;list.append(p);}
        let offset=0;const more=document.createElement('button');
        const append=()=>{more.remove();for(const entry of entries.slice(offset,offset+50)){const b=document.createElement('button');b.textContent=`▶ ${entry.name}`;b.onclick=()=>playRef.current(entry);list.append(b);}offset+=50;if(offset<entries.length){more.textContent=`Show more (${entries.length-offset} remaining)`;list.append(more);}};
        more.onclick=append;append();
        return list;
      };
      for(const entries of positions.values()){
        const s=entries[0]; const isActive=entries.some(e=>e.id===playing?.id);
        const marker=L.marker([s.lat!,s.lon!],{icon:L.divIcon({className:`station-beacon ${isActive?'active':''}`,html:`<span>${entries.length>1?entries.length:'<i></i>'}</span>`,iconSize:[32,32],iconAnchor:[16,16]}),title:entries.length===1?s.name:`${entries.length} stations at this location`,keyboard:true}).addTo(group);
        if(entries.length===1)marker.bindTooltip(safeText(s.name),{className:'atlas-tooltip'}).on('click',()=>playRef.current(s));
        else marker.bindPopup(()=>stationList(entries,'Stations at this location'),{maxWidth:290});
      }
      const missing=countryStations.filter(s=>s.lat===null||s.lon===null);
      const c=catalog.countries.find(c=>c.code===country);
      if(c&&missing.length)L.marker([c.lat,c.lon],{icon:L.divIcon({className:'country-hub',html:`<span>+${missing.length}</span>`,iconSize:[40,30],iconAnchor:[20,15]}),title:`${missing.length} stations with country-level location`}).bindPopup(()=>stationList(missing,'Country-level location','Exact station coordinates are not available.'),{maxWidth:290}).addTo(group);
    }
  },[catalog,country,countryIndex,playing?.id,mapReady]);

  useEffect(()=>{
    const context=(document as Document & {modelContext?:{registerTool:(tool:unknown,options:unknown)=>Promise<void>|void}}).modelContext;
    if(!context?.registerTool || !catalog)return;
    const lifecycle=new AbortController();
    try{Promise.resolve(context.registerTool({name:'select_radio_country',description:'Select a country on the radio map and list stations. Does not start audio.',inputSchema:{type:'object',properties:{countryCode:{type:'string'}},required:['countryCode'],additionalProperties:false},annotations:{readOnlyHint:false,untrustedContentHint:true},execute:async(input:unknown)=>{
      const code=(input as {countryCode?:unknown})?.countryCode;
      if(typeof code!=='string'||!catalog.countries.some(c=>c.code===code))throw Error('Unknown country code');
      selectRef.current(code);await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
      return {countryCode:code,stations:catalog.stations.filter(s=>s.country===code).map(s=>({id:s.id,name:s.name}))};
    }},{signal:lifecycle.signal})).catch(()=>{});}catch{/* unsupported experimental API */}
    return ()=>lifecycle.abort();
  },[catalog]);

  const total=catalog?.metadata.stationCount.toLocaleString() ?? '…';
  return <main className="atlas">
    <a className="skip-link" href="#stations">Skip to stations</a>
    <header className="topbar">
      <button className="brand" onClick={()=>selectCountry('')} aria-label="Radio Atlas home"><span className="brand-mark"><Radio size={23}/></span><span>radio<span className="brand-light">atlas</span><sup>LIVE</sup></span></button>
      <div className="header-note"><span className="signal-dot"/>One planet. Thousands of frequencies.</div>
      <button className="random-button" onClick={randomStation} disabled={!catalog}><Shuffle size={18}/><span>Take me anywhere</span><ArrowUpRight size={18}/></button>
    </header>
    <div className="workspace">
      <aside className="sidebar" id="stations" tabIndex={-1}>
        <div className="sidebar-top"><p className="eyebrow">THE WORLD, ON AIR</p><h1>{chosen?chosen.name:'Find your next frequency.'}</h1><p className="intro">{chosen?`${chosen.stationCount} checked streams. Pick a station to tune in.`:'Pick a country on the map. Hear what’s playing there, right now.'}</p>
          <label htmlFor="country-select" id="country-label" className="field-label">Explore a country</label>
          <Select value={country||'world'} onValueChange={v=>selectCountry(v==='world'?'':v as string)}><SelectTrigger id="country-select" className="country-select" aria-labelledby="country-label"><Globe2 size={17}/><SelectValue>{chosen?`${flag(chosen.code)} ${chosen.name}`:'Everywhere on Earth'}</SelectValue></SelectTrigger><SelectContent className="country-options" alignItemWithTrigger={false}><SelectItem value="world">Everywhere on Earth</SelectItem>{catalog?.countries.map(c=><SelectItem key={c.code} value={c.code}>{flag(c.code)} {c.name} · {c.stationCount}</SelectItem>)}</SelectContent></Select>
        </div>
        <div className="station-scroll" ref={stationScroll}>
          {loadError?<div className="empty-state" role="alert"><p>{loadError}</p><button onClick={()=>location.reload()}>Reload catalog</button></div>:!catalog?<div className="empty-state"><LoaderCircle className="spin"/>Loading the world’s frequencies…</div>:chosen?<>
            <div className="list-heading"><span>STATIONS <small>{stations.length}</small></span><button onClick={()=>selectCountry('')}><ArrowLeft size={14}/>World</button></div>
            {stations.length>0&&<div className="station-search"><Input type="search" aria-label="Search stations in this country" placeholder="Station, genre, language or region" value={query} onChange={e=>{setQuery(e.target.value);setPage(0);}}/><output>{filtered.length.toLocaleString()} matching stations</output></div>}
            {stations.length>0&&filtered.length===0&&<div className="empty-state"><p>No stations match this search.</p><button onClick={()=>setQuery('')}>Clear search</button></div>}
            {stations.length===0?<div className="empty-state"><Radio/><h2>No verified streams yet</h2><p>We haven’t found a secure, directly playable stream for {chosen.name}. Try another country or take a random trip.</p><button onClick={randomStation}>Try somewhere new <Shuffle size={15}/></button></div>:visibleStations.map((s,index)=><button key={s.id} className={`station-card ${playing?.id===s.id?'selected':''}`} onClick={()=>playStation(s)} aria-label={`Play ${s.name}`} aria-pressed={playing?.id===s.id}><span className="station-number">{playing?.id===s.id&&playerState.status==='playing'?<span className="equalizer"><i/><i/><i/></span>:String(currentPage*pageSize+index+1).padStart(2,'0')}</span><span className="station-copy"><strong>{s.name}</strong><span>{s.tags.slice(0,2).map(titleCase).join(' / ')||s.languages.slice(0,2).map(titleCase).join(' / ')||'Live radio'}</span><small>{s.region||chosen.name}{s.locationSource==='country'?' · Country-level location':''}</small></span><Play size={16} className="card-play"/></button>)}
            {pageCount>1&&<Pagination className="station-pagination" aria-label="Station pages"><button disabled={currentPage===0} onClick={()=>changePage(currentPage-1)}>Previous</button><span aria-live="polite">{currentPage+1} / {pageCount}</span><button disabled={currentPage===pageCount-1} onClick={()=>changePage(currentPage+1)}>Next</button></Pagination>}
            {stations.length>0&&<p className="list-note">All checked feeds, ordered by Radio Browser popularity. No country limit. Streams may vary by location.</p>}
          </>:<><div className="list-heading"><span>START EXPLORING</span><span>{catalog.metadata.countriesWithStations} places</span></div>{['US','BR','GB','FR','JP','IN','NG','AU'].map(code=>catalog.countries.find(c=>c.code===code)).filter((c):c is Country=>!!c&&c.stationCount>0).map(c=><button className="country-card" key={c.code} onClick={()=>selectCountry(c.code)}><span className="country-flag">{flag(c.code)}</span><span><strong>{c.name}</strong><small>{c.stationCount} stations</small></span><ArrowUpRight size={18}/></button>)}<div className="discovery-note"><Headphones size={22}/><p>No sign-up. No subscriptions.<br/>Just press play and explore.</p></div></>}
        </div>
        <footer className="sidebar-footer"><span className="signal-dot"/>{total} checked streams <button onClick={()=>setAbout(!about)} aria-expanded={about}>About & sources</button></footer>
      </aside>
      <section className="map-section" aria-label="Interactive world radio map"><div ref={mapNode} className="world-map" aria-label="Choose a country or station. Drag to pan; use plus and minus to zoom."/><div className="map-heading"><span className="eyebrow">YOUR LISTENING MAP</span><div>{chosen?<>{flag(chosen.code)} {chosen.name}</>:'Everywhere is within earshot.'}</div></div><button className="world-reset" onClick={()=>selectCountry('')} aria-label="Show the whole world"><LocateFixed size={18}/><span>World view</span></button><div className="map-caption"><span className="map-key"/>{chosen?'Click a station dot to play. Dashed markers group unlocated stations.':'Click a country to explore its stations.'}</div>{mapError&&<div className="map-alert" role="alert">The map could not load. Choose countries and play stations from the list.</div>}
        {about&&<section className="about-panel" aria-label="About Radio Atlas"><button className="about-close" aria-label="Close about" onClick={()=>setAbout(false)}>×</button><p className="eyebrow">ABOUT RADIO ATLAS</p><h2>A world of independent signals.</h2><p>Free public streams play directly from the broadcaster. Your connection goes to that station when you press play.</p><p>The catalog checks all available entries from <a href="https://www.radio-browser.info/" target="_blank" rel="noreferrer">Radio Browser</a>, with no per-country limit. List order reflects directory clicks, not national audience ratings.</p><p>Each included stream returned secure audio data during our check{catalog?` on ${dateLabel(catalog.metadata.generatedAt)}`:''}. Availability can change or depend on your country. Playback starts after the station buffers.</p><p>Station dots use community-supplied coordinates. Dashed markers indicate a country-level location, not a studio address. Country coverage includes territories; some have no suitable streams. HTTPS checks do not certify broadcast content. HLS and other unsupported formats are excluded.</p><p>Map boundaries: <a href="https://www.naturalearthdata.com/" target="_blank" rel="noreferrer">Natural Earth</a>. <a href="./data/catalog.json" target="_blank" rel="noreferrer">Download catalog & check dates</a>. <a href="./THIRD-PARTY-NOTICES.txt" target="_blank" rel="noreferrer">Licenses & credits</a>.</p></section>}
      </section>
    </div>
    <section className={`player-bar ${playerState.status==='playing'?'is-playing':''}`} aria-label="Radio player"><div className="now-playing"><div className="record"><Radio size={24}/></div><div className="now-copy"><span className="eyebrow">{playing?(playerState.status==='playing'?'NOW PLAYING':playerState.status==='loading'?'TUNING IN':playerState.status==='paused'?'PAUSED':'CONNECTION STATUS'):'READY WHEN YOU ARE'}</span><strong>{playing?.name||'The world is waiting.'}</strong><small>{playing?`${flag(playing.country)} ${activeCountry?.name||playing.country} · ${playing.codec}${playing.bitrate?' · '+playing.bitrate+' kbps':''}`:'Choose a station. Let the sound take you somewhere.'}</small></div></div><div className="transport"><button className="play-button" disabled={!playing} aria-label={['playing','loading'].includes(playerState.status)?'Pause station':'Play station'} onClick={()=>['playing','loading'].includes(playerState.status)?player.current?.pause():playing&&player.current?.play(playing)}>{playerState.status==='loading'?<LoaderCircle className="spin"/>:playerState.status==='playing'?<Pause fill="currentColor" size={20}/>:<Play fill="currentColor" size={20}/>}</button><button className="shuffle-icon" onClick={randomStation} disabled={!catalog} aria-label="Play a random station on Earth"><Shuffle size={20}/></button></div><div className="player-right"><output className="playback-status" aria-live="polite">{playerState.message||'LIVE RADIO · NO BORDERS'}</output><div className="volume-control"><button aria-label={volume?'Mute':'Unmute'} onClick={()=>setSavedVolume(volume?0:75)}>{volume?<Volume2 size={19}/>:<VolumeX size={19}/>}</button><Slider aria-label="Volume" value={[volume]} onValueChange={v=>setSavedVolume(Array.isArray(v)?v[0]:v)} min={0} max={100}/></div></div></section>
  </main>;
}
