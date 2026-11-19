// node render11.cjs d11.html outdir shardIndex shardCount
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [html, out, si, sn] = process.argv.slice(2); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGEERR', e.message));
  await p.goto('file://' + path.resolve(html)); await p.evaluate(() => window.ready);
  const NF = await p.evaluate(() => window.NFRAMES);
  for (let f = +si; f < NF; f += +sn) { await p.evaluate(t => draw(t), f / 30); await p.screenshot({ path: `${out}/f${String(f).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 93 }); }
  await b.close();
})();
