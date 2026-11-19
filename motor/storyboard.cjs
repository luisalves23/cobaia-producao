const { chromium } = require('playwright'); const path = require('path'); const fs=require('fs');
(async () => { const [html, out, ...ts] = process.argv.slice(2); fs.mkdirSync(out,{recursive:true});
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGEERR', e.message)); p.on('console', m => { if (m.type() === 'error') console.error('CONSOLE', m.text()); });
  await p.goto('file://' + path.resolve(html)); await p.evaluate(() => window.ready);
  for (const t of ts) { await p.evaluate(t => draw(t), +t); await p.screenshot({ path: `${out}/t${(+t).toFixed(2).padStart(6,'0')}.jpg`, type: 'jpeg', quality: 85 }); }
  await b.close(); })();
