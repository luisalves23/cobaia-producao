// =================== DIA 13 v2 · 6 s em diante: cenas novas a partir do roteiro ===================
const CTA_0 = 50.55, PURP_0 = 53.35, LOOP_0 = 55.05;
// ---------- utilidades ----------
const pop = (t, t0, f = 3, z = .5) => Math.max(0, spring(t - t0, f, z));
function badgeN(c, x, y, r, n, col, ink) { c.save(); c.translate(x, y); c.fillStyle = col; c.beginPath(); c.arc(0, 0, r, 0, 7); c.fill(); c.fillStyle = ink; c.font = `${Math.round(r * 1.35)}px Anton`; const w = c.measureText(n).width; c.fillText(n, -w / 2, r * .48); c.restore(); }
function glyphP(c, k, x, y, s, col) { // os 5 padrões de texto de IA, como desenho (nada legível)
  c.save(); c.translate(x, y); c.scale(s, s); c.fillStyle = col; c.strokeStyle = col; c.lineCap = 'round'; c.lineJoin = 'round';
  if (k === 0) { rr(c, -46, -9, 92, 18, 9); c.fill(); } // travessão
  if (k === 1) { c.lineWidth = 8; rr(c, -50, -36, 100, 62, 22); c.stroke(); c.beginPath(); c.moveTo(-20, 26); c.lineTo(-34, 44); c.lineTo(-2, 26); c.stroke(); [-22, 0, 22].forEach(px => { c.beginPath(); c.arc(px, -5, 6, 0, 7); c.fill(); }); } // frase de enchimento
  if (k === 2) { [-28, 0, 28].forEach(py => { c.beginPath(); c.arc(-36, py, 8, 0, 7); c.fill(); rr(c, -18, py - 6, 62, 12, 6); c.fill(); }); } // listas de três
  if (k === 3) { c.beginPath(); for (let i = 0; i < 8; i++) { const a = i * Math.PI / 4, r = i % 2 ? 14 : 44; c.lineTo(r * Math.cos(a), r * Math.sin(a)); } c.closePath(); c.fill(); } // brilhinho de efeito
  if (k === 4) { c.lineWidth = 9; c.beginPath(); c.moveTo(-50, 14); c.lineTo(-30, 14); c.lineTo(-30, -18); c.lineTo(-6, -18); c.lineTo(-6, 14); c.lineTo(18, 14); c.lineTo(18, -18); c.lineTo(40, -18); c.lineTo(40, 14); c.lineTo(52, 14); c.stroke(); } // tom de robô
  c.restore(); }
function pCard(c, k, x, y, s, rot, P, o = {}) { c.save(); c.translate(x, y); c.rotate(rot); c.scale(s, s); c.save(); c.shadowColor = 'rgba(0,0,0,.35)'; c.shadowBlur = 24; c.shadowOffsetY = 10; c.fillStyle = o.bg || OW; rr(c, -80, -100, 160, 200, 20); c.fill(); c.restore(); glyphP(c, k, 0, -6, 1, o.ink || BK); if (o.n) mono(c, '0' + (k + 1), -62, -68, o.ink ? o.ink : 'rgba(12,12,12,.5)', 24, 700); c.restore(); }
function approved(c, x, y, k, t0, t) { // carimbo de aprovado: verde, só no que é positivo
  if (k <= 0) return; c.save(); c.translate(x, y); c.rotate(-.13); const s = 1 + 1.2 * (1 - clamp(k)) + .06 * Math.sin((t - t0) * 30) * imp(t, t0 + .1, .1); c.scale(s * Math.min(1, k * 1.4), s * Math.min(1, k * 1.4)); c.globalAlpha *= clamp(k * 3);
  c.strokeStyle = GN; c.lineWidth = 12; rr(c, -250, -120, 500, 240, 30); c.stroke(); c.font = '104px Anton'; c.fillStyle = GN; let w = c.measureText('APROVADO').width; c.fillText('APROVADO', -w / 2, 10); c.font = '700 58px "JetBrains Mono"'; w = c.measureText('0% IA').width; c.fillText('0% IA', -w / 2, 84); c.restore(); }
function lensDraw(c, x, y, s, col, inner) { c.save(); c.translate(x, y); c.scale(s, s); c.strokeStyle = col; c.lineCap = 'round'; c.lineWidth = 22; c.beginPath(); c.arc(0, 0, 92, 0, 7); c.stroke(); c.lineWidth = 34; c.beginPath(); c.moveTo(70, 70); c.lineTo(150, 150); c.stroke(); if (inner) inner(c); c.restore(); }
function chatWin(c, x, y, w, h, P) { c.save(); c.shadowColor = 'rgba(0,0,0,.45)'; c.shadowBlur = 50; c.fillStyle = P.bg === BK ? '#18181C' : BK; rr(c, x - w / 2, y - h / 2, w, h, 40); c.fill(); c.restore(); c.strokeStyle = 'rgba(242,238,230,.14)'; c.lineWidth = 3; rr(c, x - w / 2, y - h / 2, w, h, 40); c.stroke(); [0, 1, 2].forEach(q => { c.fillStyle = 'rgba(242,238,230,.22)'; c.beginPath(); c.arc(x - w / 2 + 50 + q * 30, y - h / 2 + 46, 8, 0, 7); c.fill(); }); }
function wrapType(c, str, n, x, y, maxW, lh) { const words_ = str.slice(0, n).split(' '); let line = '', yy = y, last = [x, y]; words_.forEach((wd, i) => { const test = line ? line + ' ' + wd : wd; if (c.measureText(test).width > maxW && line) { c.fillText(line, x, yy); yy += lh; line = wd; } else line = test; }); c.fillText(line, x, yy); return [x + c.measureText(line).width, yy]; }

// ---------- CENA: vinheta, tubos de ensaio (Vídeo 13 de 30 experimentos) ----------
const TUBE = i => [215 + (i % 6) * 130, 690 + Math.floor(i / 6) * 172];
const DROP_T = 6.62;
function tubeLevel13(t) { return .7 * easeOutCubic(ap(t, DROP_T + .1, .5)); }
function sVinheta(c, t, P) {
  const zt = easeInOutCubic(ap(t, 7.6, 1.4)); const [zx, zy] = TUBE(12); c.save(); c.translate(lerp(540, 540, zt), 1060); c.scale(1 + .22 * zt, 1 + .22 * zt); c.translate(-lerp(540, zx + 140, zt * .6), -lerp(1060, zy + 120, zt * .4));
  for (let i = 0; i < 30; i++) { const t0 = i < 12 ? 6.36 + i * .018 : i === 12 ? 6.6 : 7.16 + (i - 13) * .016; const k = pop(t, t0, 3.2, .5); if (k <= 0) continue; const [x, y] = TUBE(i);
    c.save(); c.translate(x, y + 75); c.scale(k, k); c.translate(0, -75);
    const lv = i < 12 ? .62 : i === 12 ? tubeLevel13(t) : 0;
    if (lv > 0) { c.save(); c.beginPath(); rr(c, -30, 0, 60, 150, 30); c.clip(); c.fillStyle = i === 12 ? RD : 'rgba(12,12,12,.78)'; const wob = i === 12 ? 6 * Math.sin(t * 9) * imp(t, DROP_T + .1, .4) : 0; c.beginPath(); c.moveTo(-32, 150); c.lineTo(-32, 150 - 150 * lv + wob); c.lineTo(32, 150 - 150 * lv - wob); c.lineTo(32, 150); c.fill();
      if (i === 12 && t > 7.6) for (let q = 0; q < 6; q++) { const u = ((t - 7.6) * .9 + q / 6) % 1; c.fillStyle = 'rgba(242,238,230,.75)'; c.beginPath(); c.arc(-12 + 24 * noise1(q * 3.1, 2), 150 - 150 * lv * u, 4 + 3 * (q % 2), 0, 7); c.fill(); } c.restore(); }
    c.strokeStyle = P.fg; c.lineWidth = 6; rr(c, -30, 0, 60, 150, 30); c.stroke(); c.fillRect(-40, -6, 80, 8);
    mono(c, String(i + 1).padStart(2, '0'), -16, 186, i === 12 ? P.fg : 'rgba(12,12,12,.45)', 22, 700); c.restore(); }
  c.restore(); }
// ---------- CENA: lupa procura vestígio de IA, não acha, texto aprovado 0% IA ----------
const LP = t => { const u = ap(t, 9.22, 1.15); const row = u * 4.2; return [540 + 160 * Math.sin(row * Math.PI * 1.02 - .6), 860 + 360 * u]; };
function magnify(c, x, y, t, P, pageArgs) { c.save(); c.beginPath(); c.arc(x, y, 88, 0, 7); c.clip(); c.fillStyle = OW; c.fillRect(x - 90, y - 90, 180, 180); c.translate(x, y); c.scale(1.7, 1.7); c.translate(-x, -y); sheet(c, ...pageArgs); c.restore(); c.save(); c.globalAlpha = .18; c.fillStyle = '#fff'; c.beginPath(); c.ellipse(x - 30, y - 34, 34, 16, -.6, 0, 7); c.fill(); c.restore(); }
function sScan(c, t, P) { const k = pop(t, 9.16, 2.8, .55); const st = imp(t, 10.46, .1); c.save(); c.translate(540, 1080); c.scale(.9 + .1 * k + .04 * st, .9 + .1 * k + .04 * st); c.translate(-540, -1080);
  sheet(c, 540, 1080, t, 5, P, { m: 1, rev: 1 });
  // rastro do que já foi varrido: linhas checadas ficam marcadas de leve
  const u = ap(t, 9.22, 1.15); if (t < 10.5) { c.save(); c.globalAlpha = .12; c.fillStyle = BK; c.fillRect(540 - 205, 860 - 30, 410, 360 * u + 30); c.restore(); }
  if (t > 9.2 && t < 10.44) { const [x, y] = LP(t); magnify(c, x, y, t, P, [540, 1080, t, 5, P, { m: 1, rev: 1 }]); }
  fan(c, rrPts(540, 1080, 540, 560, 24), 10.46, t);
  approved(c, 540, 1100, pop(t, 10.46, 3.4, .55), 10.46, t);
  c.restore(); }
// ---------- CENA: primeiro, o pedido ao Claude ----------
const REQ1 = 'humaniza meu texto daqui pra frente, sem soar como IA';
const REQ1_W = [[13.73, 8], [14.38, 12], [14.58, 18], [14.92, 24], [15.27, 28], [15.47, 35], [15.81, 39], [16.01, 44], [16.21, 49], [16.55, 53]];
const req1N = t => { let n = 0; REQ1_W.forEach(([tw, e], i) => { if (t >= tw) { const prev = i ? REQ1_W[i - 1][1] : 0; n = Math.round(lerp(prev, e, ap(t, tw, .16))); } }); return n; };
function sPedido(c, t, P) { if (t < 12.8) return; const k = pop(t, 12.83, 2.8, .55); c.save(); c.translate(540, 1080); c.scale(.85 + .15 * k, .85 + .15 * k); c.translate(-540, -1080); c.globalAlpha *= clamp(k * 2);
  chatWin(c, 540, 1080, 900, 820, P); mono(c, 'novo chat', 230, 727, 'rgba(242,238,230,.4)', 26, 700);
  if (t > 13.31) { const kc = pop(t, 13.36, 2.8, .45); claude(c, 186, 820, 90 * kc, (1 - clamp(kc)) * -3 + .15 * Math.sin(t * 4), 1); }
  // caixa de mensagem grande
  c.fillStyle = '#26262B'; rr(c, 140, 900, 800, 440, 36); c.fill(); c.strokeStyle = 'rgba(242,238,230,.18)'; c.lineWidth = 3; c.stroke();
  const sent = t > 16.72; const n = req1N(t); c.font = '900 58px Inter'; c.fillStyle = OW; c.globalAlpha *= sent ? 1 - ap(t, 16.72, .2) : 1;
  const [cx_, cy_] = wrapType(c, REQ1, n, 190, 990, 690, 76); if (!sent && n < REQ1.length && Math.floor(t * 7) % 2 === 0 || (n > 0 && n < REQ1.length)) { c.fillRect(cx_ + 6, cy_ - 46, 5, 58); }
  c.globalAlpha = clamp(k * 2);
  if (sent) { const q = pop(t, 16.78, 3, .5); checkB(c, 300, 820, q, GN, OW, 34); c.font = '900 40px Inter'; c.fillStyle = OW; c.globalAlpha *= clamp(q * 2); c.fillText('combinado', 350, 834); }
  c.restore(); }
const SEND1 = [880, 1280];
// ---------- CENA: pesquisa profunda e os padrões ----------
const DIVE0 = 18.9;
function sPesquisa(c, t, P) {
  if (t < 19.9) { // mergulho: folhas passando pela câmera, cada vez mais fundo
    const sp_ = t < 19.35 ? (t - 17.1) * .7 : (19.35 - 17.1) * .7 + (t - 19.35) * 2.6;
    const R_ = rng(77); const items = [];
    for (let i = 0; i < 22; i++) { const bx = (R_() - .5) * 1400, by = (R_() - .5) * 1500, z0 = R_() * 6; const z = ((z0 - sp_) % 6 + 6) % 6 + .35; items.push([bx, by, z, R_()]); }
    items.sort((a, b) => b[2] - a[2]);
    items.forEach(([bx, by, z, r]) => { const s = 1 / z; const x = 540 + bx * s * .5, y = 1080 + by * s * .45; if (s > 2.4) return; c.save(); c.globalAlpha *= clamp((6 - z) / 2) * clamp(2.6 - s); c.translate(x, y); c.rotate((r - .5) * .6); c.scale(s * .45, s * .45); c.fillStyle = P.bg === BK ? OW : '#DCD6CB'; rr(c, -110, -140, 220, 280, 14); c.fill(); c.fillStyle = 'rgba(12,12,12,.35)'; for (let q = 0; q < 6; q++) c.fillRect(-80, -100 + q * 36, 160 - (q % 3) * 30, 12); c.restore(); });
    // régua de profundidade
    c.save(); c.globalAlpha *= .8; c.strokeStyle = P.fg; c.lineWidth = 3; c.beginPath(); c.moveTo(960, 640); c.lineTo(960, 1500); c.stroke(); for (let q = 0; q <= 10; q++) { c.beginPath(); c.moveTo(960, 640 + q * 86); c.lineTo(q % 5 ? 945 : 930, 640 + q * 86); c.stroke(); } c.restore(); return; }
  // o gancho sobe trazendo os padrões, que se abrem em leque
  const up = easeOutCubic(ap(t, 20.2, .45)); const spread = pop(t, 20.54, 2.6, .55);
  for (let k = 0; k < 5; k++) { const a = (k - 2) * .22 * spread; const r = 520; const cx = 540 + r * Math.sin(a) * 1.2, cy = lerp(1650, 1220, up) - r * (Math.cos(a) - 1) * .9 - (1 - spread) * 0; const jit = t > 21.73 ? 6 * Math.sin(t * 40 + k) * imp(t, 21.73, .5) : 0;
    pCard(c, k, cx + jit, cy, .95 + .1 * imp(t, 21.0 + k * .08, .1), a * .9, P, { n: t > 21.0 + k * .08 }); }
  if (t < 20.62) { c.save(); c.strokeStyle = P.fg; c.lineWidth = 6; c.beginPath(); c.moveTo(540, 560); c.lineTo(540, hookY(t) - 40); c.stroke(); c.restore(); }
}
const hookY = t => t < 20.2 ? lerp(560, 1500, easeInCubic(ap(t, 19.9, .3))) : lerp(1500, 1040, easeOutCubic(ap(t, 20.2, .45)));
// ---------- CENA: nunca repetir nenhum: os padrões vão pra fragmentadora ----------
const SHT = [22.86, 23.22, 23.5, 23.76, 23.92];
function cardShred(k, t) { const t0 = SHT[k]; const x0 = 220 + k * 160, y0 = 860; if (t < t0) return [x0, y0 + 8 * Math.sin(t * 6 + k), 1, 0]; const u = ap(t, t0, .3); return [lerp(x0, 540, easeInOutCubic(u)), lerp(y0, 1250, easeInCubic(u)), lerp(.75, .7, u), u]; }
function sNunca(c, t, P) { const k0 = pop(t, 22.62, 3, .5);
  // fragmentadora
  c.save(); c.translate(540, 1400); c.scale(k0, k0); c.fillStyle = BK; rr(c, -330, -140, 660, 280, 34); c.fill(); c.fillStyle = '#2A2A2E'; rr(c, -250, -150, 500, 26, 13); c.fill(); for (let q = 0; q < 9; q++) { c.fillStyle = 'rgba(242,238,230,.12)'; c.fillRect(-280 + q * 70, 40, 40, 10); } c.restore();
  // tiras caindo
  SHT.forEach((t0, k) => { if (t < t0 + .25) return; const lt = t - t0 - .25; for (let q = 0; q < 8; q++) { const y = 1540 + lt * 700 + 30 * Math.sin(q * 3); if (y > 1900) continue; c.save(); c.globalAlpha *= clamp(1 - lt * .7); c.fillStyle = OW; c.translate(330 + q * 52 + 10 * Math.sin(lt * 9 + q), y); c.rotate(.2 * Math.sin(lt * 7 + q * 2)); c.fillRect(-7, 0, 14, 90 + 20 * (q % 3)); c.restore(); } });
  // cartões entrando um a um
  for (let k = 4; k >= 0; k--) { const [x, y, s, u] = cardShred(k, t); if (u >= 1) continue; c.save(); if (u > .55) { c.beginPath(); c.rect(0, 0, 1080, 1255); c.clip(); } pCard(c, k, x, y, s * pop(t, 22.6 + k * .04, 3, .5), (1 - u) * (k - 2) * .05, P, { bg: OW }); c.restore(); }
  // a boca da fragmentadora por cima
  c.save(); c.translate(540, 1400); c.scale(k0, k0); c.fillStyle = BK; rr(c, -260, -150, 520, 30, 12); c.fill(); c.restore(); }
// ---------- CENA: sinais óbvios: placas de proibido ----------
const SGN = [[220, 26.6], [540, 27.6], [860, 28.6]];
function sSinais(c, t, P) { SGN.forEach(([x, ts], i) => { const k = pop(t, 25.89 + i * .07, 2.6, .45); if (k <= 0) return; const wob = .06 * Math.sin((t - 26.17) * 14) * imp(t, 26.17, .3);
  c.save(); c.translate(x, 1480); c.rotate(wob); c.scale(1, k); c.fillStyle = P.fg; c.fillRect(-10, -460, 20, 460); c.translate(0, -520);
  c.fillStyle = OW; c.beginPath(); c.arc(0, 0, 128, 0, 7); c.fill(); c.strokeStyle = P.fg; c.lineWidth = 22; c.beginPath(); c.arc(0, 0, 118, 0, 7); c.stroke();
  glyphP(c, [0, 1, 4][i], 0, 0, 1.35, BK);
  if (t > ts + .3) { c.save(); c.strokeStyle = P.fg; c.lineWidth = 22; c.lineCap = 'round'; c.beginPath(); c.moveTo(-82, -82); c.lineTo(82, 82); c.stroke(); c.restore(); }
  c.restore(); if (t > ts - .02) fan(c, circPts(x, 960, 146), ts, t); }); }
// ---------- CENA: o truque: a carta vira a barra; no mesmo chat, menu, skill creator ----------
function cardBack(c, x, y, s, rot, P, face) { c.save(); c.translate(x, y); c.rotate(rot); c.scale(s, 1); c.save(); c.shadowColor = 'rgba(0,0,0,.4)'; c.shadowBlur = 30; c.fillStyle = face ? OW : '#2A2A2E'; rr(c, -120, -170, 240, 340, 22); c.fill(); c.restore();
  if (!face) { c.strokeStyle = 'rgba(242,238,230,.25)'; c.lineWidth = 4; rr(c, -100, -150, 200, 300, 14); c.stroke(); for (let q = -3; q <= 3; q++) { c.beginPath(); c.moveTo(-100, q * 40); c.lineTo(100, q * 40 + 60); c.stroke(); } }
  c.restore(); }
const MENU = [['', 260], ['', 200], ['skill creator', 0], ['', 230]];
function sTruque(c, t, P) {
  if (t < 30.48) { // embaralha e vira
    for (let i = 0; i < 3; i++) { const ph = (t - 29.35) * 9 + i * 2.1; const sh = t < 29.94 ? 1 : 0; const x = 540 + (i - 1) * 270 * (t < 29.94 ? Math.cos(ph * .5) : 1 - .0) * (t < 29.94 ? 1 : 1); const y = 1080 - (t < 29.94 ? 60 * Math.abs(Math.sin(ph)) : 0);
      if (i === 1 && t >= 29.94) { const f = ap(t, 29.94, .16); const sc = Math.abs(Math.cos(Math.PI * f)); cardBack(c, 540, 1080, Math.max(.02, sc) * (1 + .15 * imp(t, 30.1, .1)), 0, P, f > .5); }
      else if (i !== 1 || t < 29.94) cardBack(c, i === 1 ? 540 + 40 * Math.sin(ph) * sh : x, y, 1, (i - 1) * .08 * sh, P, false); }
    return; }
  const k = pop(t, 30.48, 2.8, .55); c.save(); c.globalAlpha *= clamp(k * 2); c.translate(540, 1080); c.scale(.9 + .1 * k, .9 + .1 * k); c.translate(-540, -1080);
  chatWin(c, 540, 1080, 900, 820, P); claude(c, 186, 760, 70, .1 * Math.sin(t * 3), .8);
  c.fillStyle = '#26262B'; rr(c, 140, 1300, 800, 112, 56); c.fill(); c.strokeStyle = 'rgba(242,238,230,.18)'; c.lineWidth = 3; c.stroke();
  if (t > 31.97) { c.font = '700 60px "JetBrains Mono"'; c.fillStyle = OW; c.fillText('/', 196, 1376); if (Math.floor(t * 6) % 2 === 0) c.fillRect(240, 1326, 5, 58); }
  // tecla gigante da barra
  if (t > 30.9 && t < 32.4) { const kk = pop(t, 30.95, 3, .5) * (1 - ap(t, 32.15, .2)); const pr = Math.exp(-Math.pow((t - 31.95) / .06, 2)); c.save(); c.translate(540, 960 + 20 * pr); c.scale(kk, kk);
    c.fillStyle = '#8E1B1F'; rr(c, -150, -120, 300, 260, 40); c.fill(); c.fillStyle = RD; rr(c, -150, -140 + 18 * pr, 300, 240, 40); c.fill(); c.font = '170px Anton'; c.fillStyle = OW; const w = c.measureText('/').width; c.fillText('/', -w / 2, 50 + 18 * pr); c.restore(); }
  // menu de comandos
  if (t > 32.35) { const km = pop(t, 32.4, 3, .55); c.save(); c.translate(540, 1270); c.scale(1, km); c.translate(-540, -1270); c.fillStyle = '#222227'; rr(c, 160, 840, 640, 420, 28); c.fill(); c.strokeStyle = 'rgba(242,238,230,.16)'; c.stroke();
    MENU.forEach(([lab, w], i) => { const y = 900 + i * 96; const sel = i === 2 && t > 33.18; if (sel) { c.fillStyle = 'rgba(242,238,230,.1)'; rr(c, 180, y - 30, 600, 80, 18); c.fill(); }
      c.fillStyle = 'rgba(242,238,230,.3)'; rr(c, 210, y - 8, 46, 46, 10); c.fill(); if (lab) { c.font = '900 46px Inter'; c.fillStyle = OW; c.fillText(lab, 280, y + 30); } else { c.fillStyle = 'rgba(242,238,230,.28)'; rr(c, 280, y + 6, w, 18, 9); c.fill(); } }); c.restore();
    if (t > 32.6 && t < 33.95) { const e = easeInOutCubic(ap(t, 32.6, .5)); cursor(c, lerp(860, 600, e), lerp(1500, 1110, e), Math.exp(-Math.pow((t - 33.42) / .05, 2))); } }
  c.restore(); }
// ---------- CENA: pede: o Anti-Robô nasce ----------
const CARD = { x: 540, y: 1040, w: 600, h: 720 };
const CARDP = rrPts(CARD.x, CARD.y, CARD.w, CARD.h, 40);
const CARDR = resample(CARDP.concat([CARDP[0]]), 300);
const drawK = t => easeInOutCubic(ap(t, 34.66, 1.2));
function sPede(c, t, P) { const dk = drawK(t); const sq = t > 38.5 ? easeInOutCubic(ap(t, 38.5, .4)) : 0;
  c.save(); c.translate(540, 1040); c.scale(1 - .35 * sq, 1 - .35 * sq); c.translate(-540 + 0, -1040 - 520 * sq * 0); c.translate(0, -360 * sq);
  // contorno sendo desenhado e depois o cartão preenchido
  if (dk > .97) { c.save(); c.shadowColor = 'rgba(0,0,0,.35)'; c.shadowBlur = 40; c.fillStyle = BK; rr(c, CARD.x - CARD.w / 2, CARD.y - CARD.h / 2, CARD.w, CARD.h, 40); c.fill(); c.restore(); }
  c.strokeStyle = BK; c.lineWidth = 8; c.lineJoin = 'round'; c.beginPath(); const n = Math.floor(dk * (CARDR.length - 1)); for (let i = 0; i <= n; i++) i ? c.lineTo(...CARDR[i]) : c.moveTo(...CARDR[i]); c.stroke();
  if (dk > .97) {
    // digital (texto pessoal)
    const fk = ap(t, 36.02, .5); c.save(); c.strokeStyle = 'rgba(242,238,230,.5)'; c.lineWidth = 5; c.lineCap = 'round'; for (let q = 0; q < 5; q++) { c.beginPath(); c.arc(540, 820, 18 + q * 16, Math.PI * (1.1 - .05 * q), Math.PI * (1.1 - .05 * q) + Math.PI * 1.4 * fk); c.stroke(); } c.restore();
    if (t > 36.89) { const kl = pop(t, 36.89, 3.2, .5); c.save(); c.translate(540, 990); c.scale(kl, kl); c.font = '118px Anton'; c.fillStyle = OW; const w = c.measureText('Anti-Robô').width; c.fillText('Anti-Robô', -w / 2, 40); c.restore(); }
    for (let k = 0; k < 5; k++) { const t0 = 37.55 + k * .1; if (t < t0) continue; const u = easeOutCubic(ap(t, t0, .3)); const x = lerp(-150, 330 + (k % 5) * 105, u), y = lerp(1300, 1190 + 0 * k, u); c.save(); c.translate(x, y); c.scale(.42, .42); c.fillStyle = 'rgba(242,238,230,.12)'; rr(c, -110, -110, 220, 220, 30); c.fill(); glyphP(c, k, 0, 0, 1.2, OW); c.restore(); } }
  c.restore();
  // nunca mais explicar: o balão de explicação é fechado com um zíper
  if (t > 38.6) { const kb = pop(t, 38.62, 3, .55); c.save(); c.translate(540, 1300); c.scale(kb, kb); c.fillStyle = P.fg; rr(c, -330, -130, 660, 260, 60); c.fill(); c.beginPath(); c.moveTo(-200, 120); c.lineTo(-250, 200); c.lineTo(-120, 120); c.fill();
    const z = zipX(t) - 540; c.fillStyle = P.bg; [-60, 0, 60].forEach((yy, q) => { rr(c, -250, yy - 12, [430, 380, 300][q], 24, 12); c.fill(); });
    c.save(); c.beginPath(); c.rect(-340, -140, z + 340, 280); c.clip(); c.fillStyle = P.fg; c.fillRect(-340, -140, 680, 280); c.strokeStyle = P.bg; c.lineWidth = 6; c.beginPath(); for (let q = -300; q < 300; q += 22) { c.moveTo(q, -10); c.lineTo(q + 11, 10); c.lineTo(q + 22, -10); } c.stroke(); c.restore(); c.restore(); } }
const zipX = t => lerp(230, 870, easeInOutCubic(ap(t, 38.94, .62)));
// ---------- CENA: o Claude cria a SUA skill; é só instalar ----------
function sCria(c, t, P) { const kb = pop(t, 40.14, 2.8, .5); const drop = easeInCubic(ap(t, 42.44, .25)); const land = imp(t, 42.69, .08);
  const by = lerp(1010, 1200, drop); c.save(); c.translate(540, by); c.scale(kb * (1 + .2 * land), kb * (1 - .15 * land));
  // caixa (a skill embalada)
  const lid = easeOutCubic(ap(t, 40.3, .5)); c.fillStyle = P.bg === RD ? BK : OW; rr(c, -230, -170, 460, 340, 26); c.fill(); c.fillStyle = P.bg === RD ? '#222' : '#DAD4C9'; c.save(); c.translate(0, -170); c.rotate(-1.2 * (1 - lid)); rr(c, -250, -40, 500, 70, 20); c.fill(); c.restore();
  if (t > 40.6) claude(c, 0, 30, 120 * pop(t, 40.6, 3, .5), .1 * Math.sin(t * 3), .6);
  c.restore();
  // plataforma de instalação com anel de progresso
  if (t > 42.3) { const kp = pop(t, 42.3, 3, .55); c.save(); c.translate(540, 1420); c.scale(kp, kp); c.fillStyle = P.bg === RD ? BK : '#2A2A2E'; c.beginPath(); c.ellipse(0, 0, 320, 60, 0, 0, 7); c.fill(); c.restore();
    const pr = easeInOutCubic(ap(t, 42.6, .4)); if (pr > 0 && t < 43.1) { c.save(); c.strokeStyle = OW; c.lineWidth = 10; c.lineCap = 'round'; c.beginPath(); c.ellipse(540, 1420, 340, 74, 0, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * pr); c.stroke(); c.restore(); }
    if (t > 42.98) checkB(c, 800, 1010, pop(t, 42.98, 3.2, .5), GN, OW, 52); } }
// ---------- CENA: antes de escrever, digita /anti-robô ----------
const CMD = '/anti-robô';
const cmdN = t => t < 44.6 ? 0 : t < 44.94 ? 1 : Math.min(CMD.length, 1 + Math.floor((t - 44.94) / .06) + 1);
function sComando(c, t, P) { const kp = pop(t, 43.08, 2.8, .55);
  c.save(); c.translate(540, 830); c.scale(.62 * kp, .62 * kp); c.translate(-540, -830); c.fillStyle = OW; c.shadowColor = 'rgba(0,0,0,.4)'; c.shadowBlur = 40; rr(c, 540 - 260, 830 - 270, 520, 540, 20); c.fill(); c.restore();
  // a caneta para no ar: antes de escrever
  if (t < 44.3) { const hv = 10 * Math.sin(t * 5); c.save(); c.translate(700, 720 + hv); c.rotate(.7); c.fillStyle = P.fg; rr(c, -14, -150, 28, 150, 8); c.fill(); c.beginPath(); c.moveTo(-14, 0); c.lineTo(14, 0); c.lineTo(0, 30); c.fill(); c.restore(); }
  const ki = pop(t, 44.1, 3, .55); c.save(); c.translate(540, 1300); c.scale(ki, ki); c.fillStyle = '#1F1F24'; rr(c, -420, -80, 840, 160, 80); c.fill(); c.strokeStyle = 'rgba(242,238,230,.22)'; c.lineWidth = 4; c.stroke();
  const n = cmdN(t); c.font = '700 76px "JetBrains Mono"'; c.fillStyle = OW; c.fillText(CMD.slice(0, n), -360, 26); c.restore(); }
const cmdCur = t => [540 - 360 + textW(tc, '700 76px "JetBrains Mono"', CMD.slice(0, cmdN(t))) + 26, 1300];
// ---------- CENA: o texto volta com 0% de IA, toda vez ----------
function pageBack(t) { const u = easeOutCubic(ap(t, 45.8, .5)); return [lerp(1350, 540, u) + 0, 1080 - 240 * Math.sin(Math.PI * u), 6.283 * (1 - u)]; }
const LP2 = t => { const u = ap(t, 46.2, .7); return [540 + 150 * Math.sin(u * Math.PI * 3), 880 + 340 * u]; };
const TV = [48.4, 48.62, 48.84];
function sVolta(c, t, P) {
  const shr = easeInOutCubic(ap(t, 48.2, .25));
  const [x, y, r] = pageBack(t); c.save(); c.translate(lerp(x, 200, shr), lerp(y, 1120, shr)); c.rotate(r * .5); c.scale(lerp(1, .46, shr), lerp(1, .46, shr)); c.translate(-x, -y);
  sheet(c, x, y, t, 6, P, { m: 1, rev: ap(t, 46.13, .5) }); if (t > 46.2 && t < 46.92 && shr === 0) { const [lx, ly] = LP2(t); magnify(c, lx, ly, t, P, [x, y, t, 6, P, { m: 1, rev: 1 }]); }
  fan(c, rrPts(540, 1080, 540, 560, 24), 46.95, t);
  approved(c, 540, 1100, pop(t, 46.95, 3.4, .55), 46.95, t); c.restore();
  [540, 880].forEach((px, i) => { const k = pop(t, 48.3 + i * .08, 3, .5); if (k <= 0) return; c.save(); c.translate(px, 1120); c.scale(.46 * k, .46 * k); sheet(c, 0, 0, t, 7 + i, P, { m: 1, rev: 1 }); c.restore(); });
  TV.forEach((tv, i) => { if (t > tv) checkB(c, [200, 540, 880][i] + 80, 960, pop(t, tv, 3.2, .5), GN, OW, 40); }); }
// ---------- CENA: quer o guia passo a passo? ----------
const FLIPS = [49.69, 49.96, 50.12];
function sGuia(c, t, P) { const ko = easeOutCubic(ap(t, 49.3, .3)); const k = pop(t, 49.24, 3, .55); c.save(); c.translate(540, 1080); c.scale(k, k);
  c.fillStyle = BK; rr(c, -400 * ko - 10, -300, 800 * ko + 20, 600, 24); c.fill();
  c.fillStyle = OW; rr(c, -380 * ko, -280, 380 * ko, 560, 12); c.fill(); rr(c, 0, -280, 380, 560, 12); c.fill(); c.fillStyle = 'rgba(12,12,12,.2)'; c.fillRect(-3, -280, 6, 560);
  let pg = 0; FLIPS.forEach((f, i) => { if (t >= f) pg = i + 1; });
  if (ko > .5) { for (let q = 0; q < 6; q++) { c.fillStyle = 'rgba(12,12,12,.25)'; c.fillRect(-330 * ko, -200 + q * 60, 260 * ko - (q % 2) * 50, 14); } }
  if (pg > 0) { c.font = '300px Anton'; c.fillStyle = BK; const s = String(pg); const w = c.measureText(s).width; const kk = pop(t, FLIPS[pg - 1] + .08, 3.2, .5); c.save(); c.translate(190, 0); c.scale(kk, kk); c.fillText(s, -w / 2, 105); c.restore(); }
  FLIPS.forEach(f => { const u = ap(t, f, .16); if (u <= 0 || u >= 1) return; const sx = Math.cos(Math.PI * u); c.save(); c.scale(sx, 1); c.fillStyle = u < .5 ? OW : '#E8E2D7'; rr(c, 0, -280, 380, 560, 12); c.fill(); c.restore(); });
  c.restore(); }
// ---------- chamada final: segue, curte, comenta HUMANO ----------
const WORD = 'HUMANO';
const AVY = t => lerp(980, 800, easeInOutCubic(ap(t, 51.5, .3))), AVS = t => lerp(1, .62, easeInOutCubic(ap(t, 51.5, .3)));
function ctaScene2(t, P) { const c = ctx;
  const cap = t < 51.55 ? [['segue o ', 'inter', P.fg], ['cobaia', 'anton', RD]] : t < 51.93 ? [['curte', 'anton', RD]] : [['comenta ', 'inter', P.fg], [WORD, 'anton', RD]];
  const ck = sp(t, t < 51.55 ? 50.55 : t < 51.93 ? 51.55 : 51.93, 3, .5); c.save(); c.globalAlpha = clamp(ck * 2); let tot = 0; cap.forEach(([s, f]) => { c.font = FONTS[f](f === 'anton' ? 150 : 120); tot += c.measureText(s).width; }); const sc = Math.min(1, 900 / tot); let x = 540 - tot * sc / 2; c.translate(0, (1 - ck) * 30);
  cap.forEach(([s, f, col]) => { c.font = FONTS[f](Math.floor((f === 'anton' ? 150 : 120) * sc)); c.fillStyle = col; c.fillText(s, x, 470); x += c.measureText(s).width; }); c.restore();
  const ay = AVY(t), as = AVS(t); fan(c, circPts(540, 980, 172), 50.58, t);
  c.save(); c.translate(540, ay); c.scale(as, as); const bk = sp(t, 50.6, 2.4, .5); if (bk > 0) { c.save(); c.globalAlpha = clamp(bk * 2); c.beginPath(); c.arc(0, 0, 170, 0, 7); c.save(); c.clip(); if (PHOTO) { const s = 340 / Math.min(PHOTO.width, PHOTO.height); c.drawImage(PHOTO, -PHOTO.width * s / 2, -PHOTO.height * s / 2, PHOTO.width * s, PHOTO.height * s); } else { c.fillStyle = GR; c.fillRect(-170, -170, 340, 340); } c.restore(); c.strokeStyle = OW; c.lineWidth = 6; c.stroke();
    c.globalAlpha = ap(t, 50.7, .2); c.font = '900 64px Inter'; c.fillStyle = OW; const h = '@cobaia.dev'; c.fillText(h, -c.measureText(h).width / 2, 320); c.restore(); } c.restore();
  if (t > 50.7 && t < 51.3) { const e = easeInOutCubic(ap(t, 50.7, .35)); cursor(c, lerp(900, 545, e), lerp(1500, 1160, e), Math.exp(-Math.pow((t - 51.09) / .05, 2))); }
  // curte: coração (contorno; o vermelho chega pelo elemento único)
  if (t > 51.55) { const kh = pop(t, 51.6, 3, .5); c.save(); c.globalAlpha *= clamp(kh * 2) * (1 - ap(t, 51.95, .15)); heart(c, 540, 1180, 1.6 * kh, null, OW); c.restore(); }
  if (t > 51.93) { const bk2 = sp(t, 51.95, 2.8, .5), sent = t > 52.8; c.save(); c.globalAlpha = clamp(bk2 * 2); c.translate(0, (1 - bk2) * 60);
    if (!sent || t < 53.0) { const fy = sent ? lerp(1180, 1110, easeOutCubic(ap(t, 52.8, .2))) : 1180; c.globalAlpha *= sent ? 1 - ap(t, 52.8, .2) : 1; c.fillStyle = '#1A1A1E'; rr(c, 120, fy - 60, 840, 120, 60); c.fill(); c.strokeStyle = 'rgba(242,238,230,.25)'; c.lineWidth = 3; c.stroke();
      const n = Math.min(WORD.length, Math.max(0, Math.floor((t - 52.28) / .06) + 1)); c.font = '900 56px Inter'; c.fillStyle = n ? OW : 'rgba(242,238,230,.35)'; c.fillText(n ? WORD.slice(0, n) : 'adicione um comentário', 170, fy + 20); if (n < WORD.length && Math.floor(t * 6) % 2 === 0) { c.fillStyle = RD; c.fillRect(170 + (n ? c.measureText(WORD.slice(0, n)).width : 0) + 4, fy - 30, 5, 60); } }
    c.restore(); c.save(); c.globalAlpha = 1;
    if (sent) { const q = pop(t, 52.85, 2.8, .5); c.translate(0, (1 - q) * 80 + 1140); c.globalAlpha = clamp(q * 2); c.fillStyle = GR; c.beginPath(); c.arc(170, 0, 36, 0, 7); c.fill(); mono(c, 'você', 222, -12, 'rgba(242,238,230,.55)', 26); c.font = '900 52px Inter'; c.fillStyle = OW; c.fillText(WORD, 222, 40); }
    c.restore(); }
  if (t > 52.95) { const k = sp(t, 52.97, 2.8, .5); fan(c, rrPts(540, 1340, 820, 170, 30), 52.92, t); c.save(); c.globalAlpha = clamp(k * 2); c.translate(540, 1340 + (1 - k) * 60); c.fillStyle = OW; rr(c, -410, -85, 820, 170, 30); c.fill(); c.font = '900 48px Inter'; c.fillStyle = BK; c.fillText('guia completo', -250, -4); mono(c, 'Anti-Robô passo a passo', -250, 40, 'rgba(12,12,12,.55)', 28, 700); c.restore(); }
}
function purple2(t) { ctx.fillStyle = PU; ctx.fillRect(0, 0, W_, H_); const lt = t - PURP_0; const p = .85 + .15 * Math.sin(lt * 5);
  ctx.save(); ctx.font = '800 96px Inter'; ctx.fillStyle = OW; ctx.globalAlpha = clamp(lt / .06); const s1 = 'comenta'; ctx.fillText(s1, 540 - ctx.measureText(s1).width / 2, 820); ctx.restore();
  if (lt > .28) { ctx.save(); ctx.font = 'italic 250px "Instrument Serif"'; const s = WORD; const w = ctx.measureText(s).width; const k = clamp((lt - .28) / .05); const flick = lt < .5 ? (Math.floor(lt * 40) % 3 ? 1 : .55) : 1; ctx.globalAlpha = k * flick;
    ctx.shadowColor = '#FF2D2D'; ctx.shadowBlur = 90 * p; ctx.fillStyle = '#FF5A4F'; ctx.fillText(s, 540 - w / 2, 1120); ctx.shadowBlur = 40 * p; ctx.fillText(s, 540 - w / 2, 1120); ctx.shadowColor = '#FFB3AA'; ctx.shadowBlur = 12; ctx.fillStyle = '#FFF1EE'; ctx.fillText(s, 540 - w / 2, 1120); ctx.restore(); } }

// ================= O ELEMENTO VERMELHO (de 6 s em diante): sempre vira bola e vira a próxima coisa =================
let HC = RD, HI = OW;
const ball2 = (r) => (c, t, x, y, g) => { c.fillStyle = HC; c.beginPath(); c.arc(x, y, r * g, 0, 7); c.fill(); };
const HS2 = [
  { t0: 5.96, t1: 6.36, at: t => [BEAC[0], BEAC[1] - 20], draw: ball2(34) },
  { t0: 6.5, t1: DROP_T + .12, at: t => { const u = easeInCubic(ap(t, 6.5, DROP_T - 6.5)); const [x, y] = TUBE(12); return [x, lerp(560, y + 150 - 20, u)]; }, draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g * .8, g * 1.15); c.fillStyle = HC; c.beginPath(); c.moveTo(0, -30); c.bezierCurveTo(22, -4, 22, 22, 0, 24); c.bezierCurveTo(-22, 22, -22, -4, 0, -30); c.fill(); c.restore(); } },
  { t0: DROP_T + .14, t1: 9.0, at: t => { const [x, y] = TUBE(12); const zt = easeInOutCubic(ap(t, 7.6, 1.4)); const s = 1 + .22 * zt; const ox = lerp(540, 540 + 140, zt * .6), oy = lerp(1060, TUBE(12)[1] + 120, zt * .4); const lx = x, ly = y + 150 - 150 * tubeLevel13(t) - 14; return [540 + (lx - ox) * s, 1060 + (ly - oy) * s]; }, draw: (c, t, x, y, g) => { c.fillStyle = HC; c.beginPath(); c.arc(x, y, 9 * g, 0, 7); c.fill(); } },
  { t0: 9.22, t1: 10.42, at: LP, draw: (c, t, x, y, g) => lensDraw(c, x, y, g, HC) },
  { t0: 10.6, t1: 12.0, at: t => [830, 790 + 8 * Math.sin(t * 4)], draw: (c, t, x, y, g) => lensDraw(c, x, y, .62 * g, HC, c2 => { c2.save(); c2.strokeStyle = GN; c2.lineWidth = 16; c2.lineCap = 'round'; c2.lineJoin = 'round'; c2.beginPath(); c2.moveTo(-34, 0); c2.lineTo(-8, 26); c2.lineTo(38, -26); c2.stroke(); c2.restore(); }) },
  { t0: 12.2, t1: 12.8, at: t => [540, 1060], draw: (c, t, x, y, g) => badgeN(c, x, y, 150 * g, '1', HC, HI) },
  { t0: 13.0, t1: 16.78, at: t => { const k = pop(t, 12.83, 2.8, .55); const s = .85 + .15 * k; return [540 + (SEND1[0] - 540) * s, 1080 + (SEND1[1] - 1080) * s]; }, draw: (c, t, x, y, g) => { const pr = Math.exp(-Math.pow((t - 16.62) / .05, 2)); const pulse = 1 + .1 * Math.max(0, Math.sin(t * 22)) * (t > 16.2 && t < 16.6 ? 1 : 0); c.save(); c.translate(x, y); c.scale(g * pulse * (1 - .2 * pr), g * pulse * (1 - .2 * pr)); c.fillStyle = HC; c.beginPath(); c.arc(0, 0, 48, 0, 7); c.fill(); c.strokeStyle = HI; c.lineWidth = 9; c.lineCap = 'round'; c.lineJoin = 'round'; c.beginPath(); c.moveTo(0, 18); c.lineTo(0, -18); c.moveTo(-15, -3); c.lineTo(0, -18); c.lineTo(15, -3); c.stroke(); c.restore(); } },
  { t0: 17.08, t1: 17.7, at: t => [540, 1060], draw: (c, t, x, y, g) => badgeN(c, x, y, 150 * g, '2', HC, HI) },
  { t0: 17.9, t1: 19.85, at: t => { const d = t < 19.35 ? (t - 17.9) * .25 : .36 + (t - 19.35) * 1.1; return [930, 640 + 860 * clamp(d)]; }, draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; c.beginPath(); c.moveTo(0, 0); c.lineTo(-40, -24); c.lineTo(-40, 24); c.closePath(); c.fill(); c.restore(); } },
  { t0: 19.92, t1: 22.45, at: t => [540, t < 20.62 ? hookY(t) : lerp(1040, 760, easeInOutCubic(ap(t, 20.62, .3)))], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.strokeStyle = HC; c.lineWidth = 18; c.lineCap = 'round'; c.beginPath(); c.moveTo(0, -60); c.lineTo(0, 0); c.arc(-28, 0, 28, 0, Math.PI * .95); c.stroke(); c.fillStyle = HC; c.beginPath(); c.arc(0, -70, 20, 0, 7); c.fill(); c.restore(); } },
  { t0: 22.66, t1: 24.6, at: t => [810, 1310], draw: (c, t, x, y, g) => { const on = t > 22.82; c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; c.beginPath(); c.arc(0, 0, 34, 0, 7); c.fill(); c.strokeStyle = HI; c.lineWidth = 7; c.lineCap = 'round'; c.beginPath(); c.arc(0, 2, 15, -Math.PI * .3, Math.PI * 1.3); c.moveTo(0, -18); c.lineTo(0, 0); c.stroke(); if (on) { c.globalAlpha = .4 + .4 * Math.sin(t * 20); c.strokeStyle = HC; c.lineWidth = 4; c.beginPath(); c.arc(0, 0, 48, 0, 7); c.stroke(); } c.restore(); } },
  ...SGN.map(([x, ts], i) => ({ t0: ts, t1: i < 2 ? SGN[i + 1][1] - .32 : 29.2, at: t => [x, 960], draw: (c, t, x_, y_, g) => { const u = easeOutCubic(ap(t, ts, .16)); c.save(); c.translate(x_, y_); c.scale(g, g); c.strokeStyle = HC; c.lineWidth = 24; c.lineCap = 'round'; c.beginPath(); c.arc(0, 0, 118, 0, 7); c.stroke(); c.beginPath(); c.moveTo(-82 * u, -82 * u); c.lineTo(82 * u, 82 * u); c.stroke(); c.restore(); } })),
  { t0: 30.08, t1: 30.42, at: t => [540, 1080], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g * (1 + .15 * imp(t, 30.1, .1)), g * (1 + .15 * imp(t, 30.1, .1))); c.font = '230px Anton'; c.fillStyle = RD; const w = c.measureText('/').width; c.fillText('/', -w / 2, 80); c.restore(); }, col: RD },
  { t0: 30.62, t1: 30.9, at: t => [540, 960], draw: ball2(40) },
  { t0: 32.42, t1: 34.0, at: t => [205, 1092 + 0 * t], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; rr(c, -23, -23, 46, 46, 10); c.fill(); c.restore(); } },
  { t0: 34.66, t1: 36.0, at: t => CARDR[Math.floor(drawK(t) * (CARDR.length - 1))], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.rotate(.7); c.scale(g, g); c.fillStyle = HC; rr(c, -14, -120, 28, 100, 8); c.fill(); c.beginPath(); c.moveTo(-14, -20); c.lineTo(14, -20); c.lineTo(0, 8); c.closePath(); c.fill(); c.restore(); } },
  { t0: 36.1, t1: 38.35, at: t => [790, 700 + 6 * Math.sin(t * 5)], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; c.beginPath(); c.moveTo(-26, -30); c.lineTo(26, -30); c.lineTo(26, 40); c.lineTo(0, 22); c.lineTo(-26, 40); c.closePath(); c.fill(); c.restore(); } },
  { t0: 38.7, t1: 39.95, at: t => [zipX(t), 1300], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; rr(c, -26, -34, 52, 68, 12); c.fill(); rr(c, -12, 26, 24, 50, 10); c.fill(); c.restore(); } },
  { t0: 40.2, t1: 41.3, at: t => [lerp(330, 750, easeInOutCubic(ap(t, 40.3, .8))), 840], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; rr(c, -40, -20, 80, 40, 8); c.fill(); c.restore(); } },
  { t0: 41.42, t1: 42.98, at: t => [540, lerp(1010, 1200, easeInCubic(ap(t, 42.44, .25))) - 230], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; [-1, 1].forEach(s => { c.beginPath(); c.ellipse(s * 52, -10, 54, 30, s * -.4, 0, 7); c.fill(); }); c.beginPath(); c.arc(0, 0, 24, 0, 7); c.fill(); c.restore(); } },
  { t0: 44.12, t1: 45.72, at: cmdCur, draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; c.fillRect(-18, -42, 36, 80); c.restore(); } },
  { t0: 46.2, t1: 46.92, at: LP2, draw: (c, t, x, y, g) => lensDraw(c, x, y, g, HC) },
  { t0: 47.05, t1: 48.25, at: t => [830, 790 + 8 * Math.sin(t * 4)], draw: (c, t, x, y, g) => lensDraw(c, x, y, .62 * g, HC, c2 => { c2.save(); c2.strokeStyle = GN; c2.lineWidth = 16; c2.lineCap = 'round'; c2.lineJoin = 'round'; c2.beginPath(); c2.moveTo(-34, 0); c2.lineTo(-8, 26); c2.lineTo(38, -26); c2.stroke(); c2.restore(); }) },
  { t0: 48.32, t1: 49.15, at: t => { let i = 0; TV.forEach((v, j) => { if (t >= v - .1) i = j; }); const xs = [200, 540, 880]; const u = ap(t, TV[i] - .1, .1); const xp = i ? xs[i - 1] : xs[0]; return [lerp(xp, xs[i], easeInOutCubic(u)), 940 - 120 * Math.sin(Math.PI * u) - 20 * Math.abs(Math.sin((t - TV[i]) * 9)) * (t > TV[i] ? imp(t, TV[i], .3) : 0)]; }, draw: ball2(24) },
  { t0: 49.35, t1: 50.45, at: t => [540 + 220, 1080 - 300 + 0 * t], draw: (c, t, x, y, g) => { const k = pop(t, 49.24, 3, .55); c.save(); c.translate(540 + (x - 540) * k, 1080 + (y - 1080) * k); c.scale(g * k, g * k); c.fillStyle = HC; c.beginPath(); c.moveTo(-26, -30); c.lineTo(26, -30); c.lineTo(26, 150 + 8 * Math.sin(t * 4)); c.lineTo(0, 128 + 8 * Math.sin(t * 4)); c.lineTo(-26, 150 + 8 * Math.sin(t * 4)); c.closePath(); c.fill(); c.restore(); } },
  { t0: 50.62, t1: 51.42, at: t => [540, AVY(t) + 172 * AVS(t)], draw: (c, t, x, y, g) => { const fol = t > 51.09; c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = BK; c.beginPath(); c.arc(0, 0, 54, 0, 7); c.fill(); c.fillStyle = HC; c.beginPath(); c.arc(0, 0, 46, 0, 7); c.fill(); c.strokeStyle = HI; c.lineWidth = 10; c.lineCap = 'round'; c.lineJoin = 'round'; c.beginPath(); if (!fol) { c.moveTo(-18, 0); c.lineTo(18, 0); c.moveTo(0, -18); c.lineTo(0, 18); } else { c.moveTo(-18, 2); c.lineTo(-5, 15); c.lineTo(18, -12); } c.stroke(); c.restore(); } },
  { t0: 51.66, t1: 51.98, at: t => [540, 1180], draw: (c, t, x, y, g) => heart(c, x, y, 1.6 * g * (1 + .15 * imp(t, 51.7, .1)), HC, null) },
  { t0: 52.12, t1: 53.0, at: t => [890, 1180], draw: (c, t, x, y, g) => { const press = Math.exp(-Math.pow((t - 52.8) / .05, 2)); c.save(); c.translate(x, y); c.scale(g * (1 - .1 * press), g * (1 - .1 * press)); c.fillStyle = HC; c.beginPath(); c.arc(0, 0, 44, 0, 7); c.fill(); c.fillStyle = HI; c.beginPath(); c.moveTo(-14, -20); c.lineTo(22, 0); c.lineTo(-14, 20); c.lineTo(-8, 0); c.closePath(); c.fill(); c.restore(); } },
  { t0: 53.1, t1: 53.32, at: t => [213, 1340], draw: (c, t, x, y, g) => { c.save(); c.translate(x, y); c.scale(g, g); c.fillStyle = HC; rr(c, -43, -55, 86, 110, 12); c.fill(); c.fillStyle = HI; c.fillRect(-25, -28, 50, 7); c.fillRect(-25, -10, 50, 7); c.fillRect(-25, 8, 34, 7); c.restore(); } },
];
function hero2(t, P) {
  if (t < 5.96 || t >= PURP_0) return; const c = ctx; HC = P.bg === RD ? OW : RD; HI = P.bg === RD ? RD : OW;
  for (let i = 0; i < HS2.length; i++) { const h = HS2[i], nx = HS2[i + 1];
    if (t >= h.t0 && t < h.t1) { const [x, y] = h.at(t); const grow = i === 0 ? 1 : spring(t - h.t0, 3.2, .5); const cp = ap(t, h.t1 - .16, .16); const g = Math.max(0, grow * (1 - .7 * easeInCubic(cp)));
      c.save(); c.globalAlpha = 1 - cp * .85; if (h.col) HC = h.col; h.draw(c, t, x, y, g); HC = P.bg === RD ? OW : RD; c.restore();
      const br = i === 0 ? 0 : 24 * (1 - ap(t, h.t0, .12)); const bc_ = 24 * easeInCubic(cp); const r = Math.max(br, bc_); if (r > .5) blobAt(c, t, x, y, r, h.col || HC, 0, 0, i);
      return; }
    if (nx && t >= h.t1 && t < nx.t0) { const A = h.at(h.t1), B = nx.at(nx.t0); const D = nx.t0 - h.t1; const pos = tt_ => { const u = easeInOutCubic(clamp((tt_ - h.t1) / D)); const th = 6.2832 * clamp((u - .25) / .5); const lr = Math.min(70, 30 + Math.hypot(B[0] - A[0], B[1] - A[1]) * .12);
        return [lerp(A[0], B[0], u) + lr * Math.sin(th), Math.max(560, lerp(A[1], B[1], u) - lr * (1 - Math.cos(th)) - 140 * Math.sin(Math.PI * u))]; };
      const [x, y] = pos(t), [x2, y2] = pos(t + 1 / 60); const vx = (x2 - x) * 60, vy = (y2 - y) * 60;
      for (let q = 1; q <= 4; q++) { const [gx, gy] = pos(t - q * .022); c.save(); c.globalAlpha = .16 * (1 - q / 5); blobAt(c, t, gx, gy, 24 * (1 - q * .13), HC, 0, 0, i); c.restore(); }
      blobAt(c, t, x, y, 24, HC, vx, vy, i); spray(c, x, y, 24, HC, Math.hypot(vx, vy) > 600 ? .7 : 0, 99 + Math.floor(t * 30)); return; }
  }
}
// ---------- montagem: cenas com corte de câmera da direita para a esquerda ----------
const SC2 = [[0, (c, t, P) => scene(t, P, c)], [6.32, sVinheta], [9.16, sScan], [12.15, sPedido], [17.03, sPesquisa], [22.6, sNunca], [24.75, sSinais], [29.35, sTruque], [34.09, sPede], [40.11, sCria], [43.06, sComando], [45.77, sVolta], [49.22, sGuia], [CTA_0, null]];
const TRD = .24;
function scenes2(t, P) {
  for (let i = 0; i < SC2.length; i++) { const [t0, fn] = SC2[i]; const t1 = i + 1 < SC2.length ? SC2[i + 1][0] : 1e9; if (!fn || t < t0 || t > t1 + TRD) continue;
    let dx = 0, bl = 0; if (i > 0 && t < t0 + TRD) { const u = easeOutCubic(ap(t, t0, TRD)); dx = 1080 * (1 - u); bl = 1 - u; } if (t > t1) { const u = easeInCubic(ap(t, t1, TRD)); dx = -1080 * u; bl = u; }
    ctx.save(); ctx.translate(dx, 0); if (bl > .05) ctx.filter = `blur(${(10 * Math.sin(Math.PI * Math.min(1, bl))).toFixed(1)}px)`; if (i === 0) cam(t); fn(ctx, t, P); ctx.filter = 'none'; ctx.restore(); }
}
function sceneCam(t) { // socos de câmera nos picos da fala e da trilha
  const H = [[10.46, .07], [12.15, .05], [17.03, .05], [19.35, .05], [22.82, .04], [23.74, .05], [26.6, .04], [27.6, .04], [28.6, .04], [29.96, .08], [31.95, .05], [34.09, .04], [36.89, .05], [40.11, .04], [41.4, .05], [42.69, .05], [46.95, .07], [48.34, .05], [50.58, .04]];
  const z = 1 + H.reduce((a, [h, v]) => a + v * imp(t, h, .14), 0); const sh = H.reduce((a, [h, v]) => a + 160 * v * imp(t, h, .08), 0);
  ctx.translate(540, 1080); ctx.scale(z, z); ctx.translate(-540 + sh * Math.sin(t * 90), -1080 + sh * .6 * Math.cos(t * 77)); }
function hud2(t, P) { ctx.save(); ctx.font = '400 24px "JetBrains Mono"'; ctx.fillStyle = P.fg; ctx.globalAlpha = .55; const fr = Math.floor(t * 30);
  ctx.fillText('DIA 13 / 30', 90, 230); const tc_ = `00:${String(Math.floor(t)).padStart(2, '0')}:${String(fr % 30).padStart(2, '0')}`; ctx.fillText(tc_, 990 - ctx.measureText(tc_).width, 230); const s2 = '@cobaia.dev'; ctx.fillText(s2, 990 - ctx.measureText(s2).width, 264);
  ctx.globalAlpha = .4; ctx.strokeStyle = P.fg; ctx.lineWidth = 2; [[70, 195, 1, 1], [1010, 195, -1, 1], [70, 1760, 1, -1], [1010, 1760, -1, -1]].forEach(([x, y, sx, sy]) => { ctx.beginPath(); ctx.moveTo(x + 40 * sx, y); ctx.lineTo(x, y); ctx.lineTo(x, y + 40 * sy); ctx.stroke(); });
  const K = Math.log(25), uu = t / TEND, pw = 850 * (1 - Math.exp(-K * uu)) / (1 - Math.exp(-K)); ctx.globalAlpha = .18; ctx.fillStyle = P.fg; rr(ctx, 90, 1722, 850, 8, 4); ctx.fill(); ctx.globalAlpha = 1; ctx.fillStyle = P.bg === RD ? OW : RD; rr(ctx, 90, 1722, pw, 8, 4); ctx.fill(); ctx.restore(); }
function draw(t) {
  if (t >= LOOP_0) { // loop: o primeiro quadro volta
    const u = easeOutCubic(ap(t, LOOP_0, .3)); ctx.fillStyle = BK; ctx.fillRect(0, 0, W_, H_); ctx.save(); ctx.globalAlpha = u; ctx.translate(540, 1000); ctx.scale(lerp(.8, 1, u), lerp(.8, 1, u)); ctx.translate(-540, -1000); const P = pal(0); cam(0); words(0, P); scene(0, P); ctx.restore(); hud2(0, pal(0)); grain(ctx, t, .07); return; }
  if (t >= PURP_0) { purple2(t); grain(ctx, t, .06); return; }
  const P = pal(t); ctx.fillStyle = P.bg; ctx.fillRect(0, 0, W_, H_);
  ctx.fillStyle = P.fg; ctx.globalAlpha = .04; for (let x = 90; x < 1000; x += 60) for (let y = 560; y < 1700; y += 60) ctx.fillRect(x, y, 3, 3); ctx.globalAlpha = 1;
  if (t < 6.32) { ctx.save(); cam(t); words(t, P); ctx.restore(); } else words(t, P);
  ctx.save(); if (t >= 6.32) sceneCam(t);
  if (t >= CTA_0) ctaScene2(t, P); else scenes2(t, P);
  hero2(t, P); ctx.restore();
  const fl = .22 * imp(t, TB, .07) + .18 * imp(t, 10.46, .07) + .18 * imp(t, 29.96, .07) + .18 * imp(t, 46.95, .07); if (fl > .01) { ctx.save(); ctx.globalAlpha = fl; ctx.fillStyle = OW; ctx.fillRect(0, 0, 1080, 1920); ctx.restore(); }
  hud2(t, P); grain(ctx, t, .07);
}
