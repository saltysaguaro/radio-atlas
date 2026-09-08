import type {Station,PlayerState} from './types';

/** Separate audio elements prevent stale events from affecting the next stream. */
export class RadioPlayer {
  private audio:HTMLAudioElement|null=null;
  private timer:ReturnType<typeof setTimeout>|null=null;
  private generation=0;
  private volume=0.75;
  private station:Station|null=null;
  constructor(private emit:(state:PlayerState)=>void,private createAudio:()=>HTMLAudioElement=()=>new Audio()){}
  private clearTimer(){if(this.timer)clearTimeout(this.timer);this.timer=null;}
  private release(){
    this.generation++;this.clearTimer();
    if(this.audio){this.audio.pause();this.audio.removeAttribute('src');this.audio.load();this.audio=null;}
  }
  setVolume(value:number){this.volume=Math.max(0,Math.min(1,value));if(this.audio){this.audio.volume=this.volume;this.audio.muted=this.volume===0;}}
  play(station:Station){
    this.release();this.station=station;
    if(!/^https:\/\//i.test(station.url)){this.emit({status:'error',station,message:'This stream does not support secure playback.'});return;}
    const audio=this.createAudio();this.audio=audio;
    const token=this.generation;const current=()=>token===this.generation&&this.audio===audio;
    const fail=(message:string)=>{if(!current())return;this.release();this.emit({status:'error',station,message});this.mediaState('none');};
    const waiting=()=>{if(!current())return;this.emit({status:'loading',station,message:'Connecting to the station…'});if(!this.timer)this.timer=setTimeout(()=>fail('This station isn’t responding. Try another, or press play to retry.'),18000);};
    audio.preload='none';audio.volume=this.volume;audio.muted=this.volume===0;
    // Native audio can play cross-origin streams without CORS. Do not attach
    // crossOrigin or Web Audio, which would impose extra server requirements.
    audio.addEventListener('playing',()=>{if(current()){this.clearTimer();this.emit({status:'playing',station,message:'Live from '+station.name});this.mediaState('playing');}});
    audio.addEventListener('waiting',waiting);audio.addEventListener('stalled',waiting);
    audio.addEventListener('error',()=>fail('This station is unavailable here right now. Try another station.'));
    audio.addEventListener('ended',()=>fail('The station ended its stream. Press play to reconnect.'));
    audio.addEventListener('pause',()=>{if(current()){this.clearTimer();this.emit({status:'paused',station,message:'Paused'});this.mediaState('paused');}});
    audio.src=station.url;waiting();
    const result=audio.play();
    if(result)result.catch((error:Error)=>{if(current())fail(error.name==='NotAllowedError'?'Your browser needs another tap. Press play to listen.':'Unable to play this stream. Try another station.');});
    if(typeof navigator!=='undefined'&&'mediaSession'in navigator){
      try{
        navigator.mediaSession.metadata=new MediaMetadata({title:station.name,artist:station.country,album:'Radio Atlas'});
        navigator.mediaSession.setActionHandler('play',()=>this.station&&this.play(this.station));
        navigator.mediaSession.setActionHandler('pause',()=>this.pause());
        navigator.mediaSession.setActionHandler('stop',()=>this.pause());
      }catch{/* Optional browser integration. */}
    }
  }
  private mediaState(state:MediaSessionPlaybackState){if(typeof navigator!=='undefined'&&'mediaSession'in navigator)navigator.mediaSession.playbackState=state;}
  pause(){this.release();this.emit({status:'paused',station:this.station,message:'Paused'});this.mediaState('paused');}
  destroy(){this.release();this.mediaState('none');}
}
