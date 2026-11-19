const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGEERR', e.message));
  await p.goto('file://' + path.resolve('d11.html')); await p.evaluate(() => window.ready);
  await p.evaluate(fs.readFileSync('capa.js', 'utf8')); await p.screenshot({ path: process.argv[2], type: 'jpeg', quality: 92 }); await b.close(); })();
