// node render.cjs u1.html outdir [frames...]
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [html, out, ...only] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGEERR', e.message)); p.on('console', m => { if (m.type() === 'error') console.error('CONSOLE', m.text()); });
  await p.goto('file://' + path.resolve(html)); await p.evaluate(() => window.ready); await p.evaluate(() => window.init && window.init());
  const NF = await p.evaluate(() => window.NFRAMES || 420); const frames = only.length ? only.map(Number) : [...Array(NF).keys()];
  for (const f of frames) { await p.evaluate(t => draw(t), f / 30); await p.screenshot({ path: `${out}/f${String(f).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 93 }); }
  await b.close();
})();
