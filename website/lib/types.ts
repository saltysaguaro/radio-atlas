export type Station={id:string;name:string;country:string;url:string;tags:string[];languages:string[];region:string;lat:number|null;lon:number|null;locationSource:'directory'|'country';codec:string;bitrate:number;clicks:number;votes:number;sourceCheckedAt:string|null;verification:{checkedAt:string;contentType:string;sampleBytes:number}};
export type Country={code:string;name:string;lat:number;lon:number;region:string;stationCount:number};
export type Catalog={metadata:{generatedAt:string;stationCount:number;countriesWithStations:number;countriesAtTarget:number;totalCountriesAndTerritories:number};countries:Country[];stations:Station[]};
export type PlayerState={status:'idle'|'loading'|'playing'|'paused'|'error';station:Station|null;message:string};
