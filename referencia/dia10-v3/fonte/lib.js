// Shared motion lib: deterministic, everything is a function of t (seconds).
const FPS = 30, END = 14, W_ = 1080, H_ = 1920;
// word times (video timeline, seconds)
const W = { uma:1.00, ideia:1.22, solta:1.55, vira1:2.28, um:2.96, plano1:3.10, o:4.04, plano2:4.22,
  vira2:4.79, codigo1:5.22, eo:6.05, codigo2:6.36, ganha:8.12, vida:8.45 };
const BREAK = 7.0, DROP = 8.0;

const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, k) => a + (b - a) * k;
const inv = (a, b, x) => clamp((x - a) / (b - a));
// damped spring 0->1, f = Hz, z = damping ratio (<1 overshoots)
function spring(t, f = 2.2, z = 0.38) {
  if (t <= 0) return 0;
  const w = 2 * Math.PI * f, wd = w * Math.sqrt(1 - z * z);
  return 1 - Math.exp(-z * w * t) * (Math.cos(wd * t) + (z * w / wd) * Math.sin(wd * t));
}
// velocity of the spring (for squash/stretch)
function springV(t, f = 2.2, z = 0.38) { const h = 1 / 240; return (spring(t + h, f, z) - spring(t - h, f, z)) / (2 * h); }
const easeOutCubic = k => 1 - Math.pow(1 - clamp(k), 3);
const easeInOutCubic = k => { k = clamp(k); return k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2; };
const easeInCubic = k => Math.pow(clamp(k), 3);
const easeOutExpo = k => k >= 1 ? 1 : 1 - Math.pow(2, -10 * clamp(k));
function rng(seed) { let s = seed >>> 0 || 1; return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 100000) / 100000; }; }
// smooth value noise 1D
function noise1(x, seed = 1) { const i = Math.floor(x), f = x - i, h = n => { let v = Math.sin((n + seed * 131.7) * 12.9898) * 43758.5453; return v - Math.floor(v); }; const u = f * f * (3 - 2 * f); return lerp(h(i), h(i + 1), u) * 2 - 1; }

const cv = document.getElementById('c');
cv.width = W_; cv.height = H_;
const ctx = cv.getContext('2d');
function mk(w = W_, h = H_) { const c = document.createElement('canvas'); c.width = w; c.height = h; return [c, c.getContext('2d')]; }

function rr(c, x, y, w, h, r) { w = Math.max(0, w); h = Math.max(0, h); r = Math.max(0, Math.min(r, w / 2, h / 2)); c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
// text with per-letter spring entrance. opts: font, color, x(center), y(baseline), t0, stagger, f, z, dy, scale0, align
function springText(c, str, t, o) {
  c.save(); c.font = o.font; c.fillStyle = o.color || '#000'; c.textBaseline = 'alphabetic';
  const ls = o.ls || 0;
  const widths = [...str].map(ch => c.measureText(ch).width + ls);
  const total = widths.reduce((a, b) => a + b, 0) - ls;
  let x = (o.align === 'left') ? o.x : o.x - total / 2;
  [...str].forEach((ch, i) => {
    const k = spring(t - o.t0 - i * (o.stagger ?? 0.03), o.f ?? 2.4, o.z ?? 0.42);
    const v = springV(t - o.t0 - i * (o.stagger ?? 0.03), o.f ?? 2.4, o.z ?? 0.42);
    if (k > 0.001) {
      c.save();
      const cx = x + widths[i] / 2;
      c.translate(cx, o.y + (1 - k) * (o.dy ?? 80));
      const s = lerp(o.scale0 ?? 0.4, 1, k);
      const st = clamp(v * (o.stretch ?? 0.04), -0.35, 0.35); // squash/stretch from velocity
      c.scale(s * (1 - st * 0.5), s * (1 + st));
      if (o.rot) c.rotate((1 - k) * o.rot);
      c.globalAlpha = clamp(k * 3) * (o.alpha ?? 1);
      c.fillText(ch, -widths[i] / 2 + ls / 2, 0);
      c.restore();
    }
    x += widths[i];
  });
  c.restore();
  return total;
}
function textW(c, font, s) { c.save(); c.font = font; const w = c.measureText(s).width; c.restore(); return w; }
// resample a polyline to n points by arc length
function resample(pts, n, closed = false) {
  const P = closed ? [...pts, pts[0]] : pts; const L = [0];
  for (let i = 1; i < P.length; i++) L.push(L[i - 1] + Math.hypot(P[i][0] - P[i - 1][0], P[i][1] - P[i - 1][1]));
  const tot = L[L.length - 1], out = []; let j = 1;
  for (let i = 0; i < n; i++) { const d = tot * i / (n - 1); while (j < L.length - 1 && L[j] < d) j++; const k = (d - L[j - 1]) / ((L[j] - L[j - 1]) || 1); out.push([lerp(P[j - 1][0], P[j][0], k), lerp(P[j - 1][1], P[j][1], k)]); }
  return out;
}
function grain(c, t, a = 0.035) {
  if (!grain.tiles) { grain.tiles = []; for (let s = 0; s < 4; s++) { const [g, gc] = mk(256, 256); const im = gc.createImageData(256, 256); const r = rng(s + 7); for (let i = 0; i < im.data.length; i += 4) { const v = r() * 255; im.data[i] = im.data[i + 1] = im.data[i + 2] = v; im.data[i + 3] = 255; } gc.putImageData(im, 0, 0); grain.tiles.push(g); } }
  c.save(); c.globalAlpha = a; c.globalCompositeOperation = 'overlay'; c.fillStyle = c.createPattern(grain.tiles[Math.floor(t * 30) % 4], 'repeat'); c.fillRect(0, 0, W_, H_); c.restore();
}
window.ready = document.fonts.ready.then(() => Promise.all(['900 40px Inter','800 40px Inter','400 40px Inter','40px Anton','italic 40px "Instrument Serif"','40px "Instrument Serif"','700 40px "JetBrains Mono"','400 40px "JetBrains Mono"','40px "Permanent Marker"','40px "Dela Gothic One"'].map(f => document.fonts.load(f))));
