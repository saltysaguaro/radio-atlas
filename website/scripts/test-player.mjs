import {readFile} from 'node:fs/promises';
import {transform} from 'esbuild';
import assert from 'node:assert/strict';
import test from 'node:test';
const source=await readFile(new URL('../lib/radio-player.ts',import.meta.url),'utf8');
const {code}=await transform(source,{loader:'ts',format:'esm'});
const {RadioPlayer}=await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
class AudioDouble extends EventTarget{
  volume=1;src='';paused=true;removed=false;loads=0;reject=null;
  play(){this.paused=false;return this.reject?Promise.reject(this.reject):Promise.resolve();}
  pause(){this.paused=true;this.dispatchEvent(new Event('pause'));}
  removeAttribute(name){if(name==='src'){this.src='';this.removed=true;}}
  load(){this.loads++;}
  event(name){this.dispatchEvent(new Event(name));}
}
const station=id=>({id,name:`Station ${id}`,url:`https://radio.example/${id}`,country:'US'});
function setup(){const states=[],audios=[];const player=new RadioPlayer(s=>states.push(s),()=>{const a=new AudioDouble();audios.push(a);return a;});return {player,states,audios};}
test('switching stops and unloads the old stream before starting the new one',()=>{
  const {player,states,audios}=setup();player.play(station('a'));audios[0].event('playing');player.play(station('b'));
  assert.equal(audios[0].paused,true);assert.equal(audios[0].removed,true);assert.equal(audios[0].loads,1);
  assert.equal(audios[1].paused,false);assert.equal(states.at(-1).station.id,'b');
  audios[0].event('error');audios[0].event('playing');assert.equal(states.at(-1).station.id,'b');
  audios[1].event('playing');assert.equal(states.at(-1).status,'playing');player.destroy();
});
test('pause unloads live audio and play reconnects instead of resuming buffered history',()=>{
  const {player,states,audios}=setup();player.play(station('a'));player.pause();assert.equal(audios[0].src,'');assert.equal(states.at(-1).status,'paused');player.play(station('a'));assert.equal(audios.length,2);player.destroy();
});
test('stream errors stop network playback and expose retry state',()=>{
  const {player,states,audios}=setup();player.play(station('a'));audios[0].event('error');assert.equal(states.at(-1).status,'error');assert.equal(audios[0].paused,true);assert.equal(audios[0].src,'');player.destroy();
});
test('autoplay rejection exposes a gesture prompt',async()=>{
  const states=[];const audio=new AudioDouble();audio.reject=Object.assign(new Error(),{name:'NotAllowedError'});
  const player=new RadioPlayer(s=>states.push(s),()=>audio);player.play(station('a'));await Promise.resolve();assert.equal(states.at(-1).status,'error');assert.match(states.at(-1).message,/tap/);player.destroy();
});
test('insecure catalog input never opens a stream',()=>{
  const {player,states,audios}=setup();player.play({...station('a'),url:'http://radio.example/a'});assert.equal(audios.length,0);assert.equal(states.at(-1).status,'error');player.destroy();
});
test('volume is clamped, applied and muted across station switches',()=>{
  const {player,audios}=setup();player.setVolume(0);player.play(station('a'));assert.equal(audios[0].muted,true);player.setVolume(2);assert.equal(audios[0].volume,1);assert.equal(audios[0].muted,false);player.play(station('b'));assert.equal(audios[1].volume,1);player.destroy();
});
test('repeated stalled events cannot postpone the connection deadline indefinitely',()=>{
  const realSet=globalThis.setTimeout,realClear=globalThis.clearTimeout;const callbacks=[],cleared=[];
  globalThis.setTimeout=(fn,ms)=>{assert.equal(ms,18000);callbacks.push(fn);return callbacks.length;};globalThis.clearTimeout=id=>cleared.push(id);
  try{const {player,audios,states}=setup();player.play(station('a'));audios[0].event('stalled');audios[0].event('waiting');assert.equal(callbacks.length,1);callbacks[0]();assert.equal(states.at(-1).status,'error');assert.equal(audios[0].src,'');player.destroy();}finally{globalThis.setTimeout=realSet;globalThis.clearTimeout=realClear;}
});
