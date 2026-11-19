// desenha a capa usando as funções do d11.html (já carregado)
(() => {
  const c = ctx; const P = MODES.B;
  c.fillStyle = BK; c.fillRect(0, 0, 1080, 1920);
  let g = c.createRadialGradient(540, 1250, 50, 540, 1250, 1100); g.addColorStop(0, 'rgba(201,52,155,.38)'); g.addColorStop(.5, 'rgba(123,32,143,.22)'); g.addColorStop(1, 'rgba(59,20,107,0)'); c.fillStyle = g; c.fillRect(0, 0, 1080, 1920);
  c.fillStyle = OW; c.globalAlpha = .045; for (let x = 90; x < 1000; x += 60) for (let y = 330; y < 1700; y += 60) c.fillRect(x, y, 3, 3); c.globalAlpha = 1;
  // HUD
  c.save(); c.font = '400 26px "JetBrains Mono"'; c.fillStyle = OW; c.globalAlpha = .55; c.fillText('DIA 11 / 30', 96, 300); const h = '@cobaia.dev'; c.fillText(h, 984 - c.measureText(h).width, 300);
  c.globalAlpha = .9; c.font = '700 26px "JetBrains Mono"'; c.fillStyle = RD; const sg = 'ESPECIAL GTA VI'; c.fillText(sg, 540 - c.measureText(sg).width / 2, 300);
  c.globalAlpha = .45; c.strokeStyle = OW; c.lineWidth = 2; [[70, 260, 1, 1], [1010, 260, -1, 1], [70, 1690, 1, -1], [1010, 1690, -1, -1]].forEach(([x, y, sx, sy]) => { c.beginPath(); c.moveTo(x + 40 * sx, y); c.lineTo(x, y); c.lineTo(x, y + 40 * sy); c.stroke(); }); c.restore();
  // DIA 11/30
  c.font = '132px Anton'; const d = 'DIA 11'; const dw = c.measureText(d).width; c.font = '70px Anton'; const sw = c.measureText('/30').width; let x0 = 540 - (dw + sw) / 2;
  c.font = '132px Anton'; c.fillStyle = RD; c.fillText(d, x0, 480); c.font = '70px Anton'; c.fillStyle = 'rgba(255,243,232,.35)'; c.fillText('/30', x0 + dw + 6, 480);
  // gancho em duas linhas
  c.font = 'italic 104px "Instrument Serif"'; const a1 = 'a chance da', a2 = ' década'; let w1 = c.measureText(a1).width, w2 = c.measureText(a2).width; let x = 540 - (w1 + w2) / 2; c.fillStyle = OW; c.fillText(a1, x, 610); c.fillStyle = RD; c.fillText(a2, x + w1, 610);
  c.font = '120px Anton'; const b1 = 'CRESCER COM ', b2 = 'GTA VI'; w1 = c.measureText(b1).width; w2 = c.measureText(b2).width; x = 540 - (w1 + w2) / 2; c.fillStyle = OW; c.fillText(b1, x, 740);
  g = c.createLinearGradient(0, 640, 0, 740); g.addColorStop(0, YE); g.addColorStop(.5, ORG); g.addColorStop(1, RD); c.fillStyle = g; c.fillText(b2, x + w1, 740);
  // cartão 900x700 com leque
  const CX = 540, CY = 1150, CWd = 900, CH = 700;
  [[VP, 22, 5], [MG, 13, 6], [RD, 5, 8]].forEach(([col, o, lw]) => { c.save(); c.strokeStyle = col; c.lineWidth = lw; rr(c, CX - CWd / 2 - o, CY - CH / 2 - o, CWd + 2 * o, CH + 2 * o, 40 + o); c.stroke(); c.restore(); });
  c.save(); c.fillStyle = '#1C0D38'; rr(c, CX - CWd / 2, CY - CH / 2, CWd, CH, 40); c.fill(); c.restore(); glass(c, CX - CWd / 2, CY - CH / 2, CWd, CH, 40, P);
  [0, 1, 2].forEach(i => { c.fillStyle = 'rgba(255,243,232,.35)'; c.beginPath(); c.arc(CX - CWd / 2 + 50 + i * 26, CY - CH / 2 + 46, 7, 0, 7); c.fill(); });
  // sol e palmeiras ao fundo + 5 celulares em leque
  c.save(); rr(c, CX - CWd / 2, CY - CH / 2, CWd, CH, 40); c.clip();
  const sx = 540, sy = 1020; g = c.createLinearGradient(0, sy - 170, 0, sy + 170); g.addColorStop(0, YE); g.addColorStop(.5, ORG); g.addColorStop(1, RD); c.fillStyle = g; c.globalAlpha = .9; c.beginPath(); c.arc(sx, sy, 170, Math.PI, 0); c.fill(); c.globalAlpha = 1;
  c.fillStyle = 'rgba(255,243,232,.5)'; c.fillRect(CX - CWd / 2, sy, CWd, 3);
  palm(c, 170, 1020, .75, '#0A0418', .3, 1); palm(c, 920, 1020, .65, '#0A0418', -.4, -1);
  for (let i = 0; i < 5; i++) { const px = 540 + (i - 2) * 150, py = 1180 + Math.abs(i - 2) * 26, rot = (i - 2) * .12; c.save(); c.translate(px, py); c.rotate(rot); c.fillStyle = DV; rr(c, -72, -128, 144, 256, 22); c.fill(); g = c.createLinearGradient(0, -120, 0, 120); g.addColorStop(0, VP); g.addColorStop(.6, MG); g.addColorStop(1, ORG); c.fillStyle = g; rr(c, -64, -120, 128, 240, 17); c.fill();
    c.fillStyle = OW; rr(c, -42, 70, 84, 12, 6); c.fill(); c.fillStyle = YE; rr(c, -42, 70, 34, 12, 6); c.fill(); c.fillStyle = 'rgba(255,243,232,.9)'; c.beginPath(); c.moveTo(-13, -22); c.lineTo(20, 0); c.lineTo(-13, 22); c.closePath(); c.fill(); checkB(c, 52, -106, 1, GN, OW, 22); c.restore(); }
  c.restore();
  mono(c, '1 live  →  5 cortes  ·  menos de 15 min', CX - CWd / 2 + 50, CY + CH / 2 - 40, 'rgba(255,243,232,.6)', 28, 700);
  // ponto guia
  c.fillStyle = RD; c.beginPath(); c.arc(CX + CWd / 2 - 60, CY - CH / 2 + 48, 16, 0, 7); c.fill();
  // rodapé: foto + @cobaia.dev + comenta GTA
  const fy = 1610; c.save(); c.beginPath(); c.arc(150, fy, 56, 0, 7); c.save(); c.clip(); if (PHOTO) { const s = 112 / Math.min(PHOTO.width, PHOTO.height); c.drawImage(PHOTO, 150 - PHOTO.width * s / 2, fy - PHOTO.height * s / 2, PHOTO.width * s, PHOTO.height * s); } c.restore(); c.strokeStyle = OW; c.lineWidth = 4; c.stroke(); c.restore();
  c.fillStyle = RD; c.beginPath(); c.arc(192, fy + 42, 18, 0, 7); c.fill(); c.strokeStyle = OW; c.lineWidth = 4; c.lineCap = 'round'; c.beginPath(); c.moveTo(184, fy + 42); c.lineTo(200, fy + 42); c.moveTo(192, fy + 34); c.lineTo(192, fy + 50); c.stroke();
  mono(c, '@cobaia.dev', 230, fy + 12, OW, 36, 700);
  c.fillStyle = RD; rr(c, 800, fy - 34, 180, 68, 34); c.fill(); c.font = '44px Anton'; c.fillStyle = OW; c.fillText('GTA', 890 - c.measureText('GTA').width / 2, fy + 17);
  c.font = 'italic 52px "Instrument Serif"'; c.fillStyle = 'rgba(255,243,232,.7)'; c.fillText('comenta', 790 - c.measureText('comenta').width - 12, fy + 14);
  // barra da série
  c.fillStyle = 'rgba(255,243,232,.15)'; rr(c, 96, 1670, 888, 8, 4); c.fill(); c.fillStyle = RD; rr(c, 96, 1670, 888 * 11 / 30, 8, 4); c.fill();
  grain(c, 0, .05);
})();
