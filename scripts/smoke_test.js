// Headless smoke test for the Communication Field Guide.
// Usage: (cd artifact && python3 -m http.server 8765 &) ; node scripts/smoke_test.js http://localhost:8765/index.html
const { chromium } = require('playwright');
const url = process.argv[2] || 'http://localhost:8765/index.html';
(async () => {
  const b = await chromium.launch(); const errs = []; let fail = false;
  for (const [w, h, name, scheme] of [[1280, 860, 'desktop', 'light'], [390, 844, 'phone', 'dark']]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, colorScheme: scheme });
    p.on('pageerror', e => errs.push(name + ': ' + e.message));
    p.on('console', m => { if (m.type() === 'error') errs.push(name + ' console: ' + m.text()); });
    await p.goto(url); await p.waitForSelector('#home-main .row, #home-main .card');
    const lib = await p.evaluate(() => fetch('library.json').then(r => r.json()));
    await p.fill('#home-q', 'difficult conversation'); await p.waitForTimeout(150);
    const homeHits = await p.$$eval('#home-main .row', x => x.length);
    await p.goto(url.split('#')[0] + '#library'); await p.waitForTimeout(250);
    const rows = parseInt((await p.textContent('#lib-count')) || '0', 10);  // rows are paged; the count covers all entries
    await p.click('#lib-rows .row'); await p.waitForSelector('#reader:not([hidden])');
    await p.keyboard.press('Escape');
    await p.goto(url.split('#')[0] + '#sources'); await p.waitForTimeout(250);
    const cards = await p.$$eval('#sources-body .card', x => x.length);
    await p.goto(url.split('#')[0] + '#situations'); await p.waitForTimeout(250);
    const sits = await p.$$eval('#sit-cards .card', x => x.length);
    await p.goto(url.split('#')[0] + '#path'); await p.waitForTimeout(250);
    const stages = await p.$$eval('.stage', x => x.length);
    const over = await p.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
    const ok = rows === lib.insights.length && cards === lib.sources.length && sits === lib.situations.length && homeHits > 0 && !over;
    if (!ok) fail = true;
    console.log(name, { insights: lib.insights.length, rows, sources: lib.sources.length, cards, situations: lib.situations.length, sits, stages, homeHits, overflow: over, ok });
  }
  console.log('errors', errs); await b.close();
  if (fail || errs.length) process.exit(1);
})();
