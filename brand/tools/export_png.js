// node brand/tools/export_png.js  -> renders every SVG in brand/logo to PNG (transparent, 4x) in brand/logo/png
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.join(__dirname, '..', 'logo'), out = path.join(dir, 'png');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.svg'))) {
    const svg = fs.readFileSync(path.join(dir, f), 'utf8');
    const m = svg.match(/viewBox="0 0 (\d+) (\d+)"/); const w = +m[1], h = +m[2];
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 4 });
    await p.setContent(`<body style="margin:0;background:transparent">${svg}</body>`);
    await p.screenshot({ path: path.join(out, f.replace('.svg', '.png')), omitBackground: true, clip: { x: 0, y: 0, width: w, height: h } });
    await p.close();
  }
  await b.close();
})();
