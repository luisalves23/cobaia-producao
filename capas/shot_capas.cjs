const { chromium } = require('playwright'); const path=require('path'),fs=require('fs');
(async()=>{const out=process.argv[2];fs.mkdirSync(out,{recursive:true});const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.error('ERR',e.message));
await p.goto('file://'+path.resolve('capas.html'));await p.evaluate(()=>window.ready);
for(const n of (process.env.DIAS||"10").split(",").map(Number)){await p.evaluate(n=>capa(n),n);await p.locator('canvas').screenshot({path:`${out}/capa-dia${String(n).padStart(2,'0')}.jpg`,type:'jpeg',quality:94});}
for(const k of []){await p.evaluate(k=>destaque(k),k);await p.locator('canvas').screenshot({path:`${out}/destaque-${k}.jpg`,type:'jpeg',quality:94});}
await b.close();})();
