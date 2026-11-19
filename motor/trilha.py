# Trilha "montanha-russa": a música segue o roteiro em vez de ficar numa linha reta.
# Você descreve a narrativa (curva de energia + drops + paradas + impactos) e escolhe um estilo;
# o motor decide quais camadas tocam a cada semicolcheia, abre e fecha o filtro, faz riser
# que termina exatamente no corte, buraco de silêncio antes do drop, sobe o tom no clímax.
#
#   import trilha
#   NARR = trilha.Narr(energia=[(0,.9),(4.1,.25),...], drops=[13.72, 26.77, 54.28], paradas=[(24.2,.45)],
#                      impactos=[3.35, 38.58], subida_tom=45.55, fim=57.78)
#   mus = trilha.render('electro', NARR, dur=59.9)        # estilos: electro, dnb, futurebass
#
# Tudo sintetizado aqui (música própria, sem licença de terceiros).
import numpy as np
from scipy.signal import butter, sosfilt, sosfilt_zi
SR = 48000
R = np.random.default_rng(11)

def tt(d): return np.arange(int(d * SR)) / SR
def midi(n): return 440 * 2 ** ((n - 69) / 12)
def add(b, s, t, g=1.0):
    i = int(t * SR)
    if i >= len(b) or i + len(s) <= 0: return
    j = max(0, -i); s = s[j:]; i = max(0, i); n = min(len(s), len(b) - i); b[i:i + n] += s[:n] * g
def lp(x, f, o=2): return sosfilt(butter(o, min(f, SR / 2 - 100), 'lowpass', fs=SR, output='sos'), x).astype(np.float32)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x).astype(np.float32)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x).astype(np.float32)
def noise(d): return R.standard_normal(int(d * SR)).astype(np.float32)
def adsr(d, a=.005, dec=.2, sus=0., rel=.05):
    t = tt(d); e = np.minimum(1, t / max(a, 1e-4)); e = e * (sus + (1 - sus) * np.exp(-np.maximum(0, t - a) / max(dec, 1e-4)))
    r = int(rel * SR);
    if r and r < len(e): e[-r:] *= np.linspace(1, 0, r)
    return e.astype(np.float32)

# ---------------- instrumentos ----------------
def saw(f, d, det=0.0, ph=None):
    t = tt(d); ph = R.random() if ph is None else ph
    return (2 * ((f * (1 + det) * t + ph) % 1) - 1).astype(np.float32)
def supersaw(f, d, n=7, spread=.012):
    return sum(saw(f, d, spread * (k - (n - 1) / 2) / ((n - 1) / 2)) for k in range(n)) / n
def kick(d=.42, f0=150, f1=45, punch=1., click=.6):
    t = tt(d); f = f1 + (f0 - f1) * np.exp(-t / .035); ph = 2 * np.pi * np.cumsum(f) / SR
    k = np.sin(ph) * np.exp(-t / .22) * punch + click * hp(noise(d), 3000) * np.exp(-t / .004)
    return np.tanh(k * 1.6).astype(np.float32)
def k808(f, d=.9, glide=0):
    t = tt(d); ff = f * (1 + glide * np.exp(-t / .06)); ph = 2 * np.pi * np.cumsum(ff) / SR
    return np.tanh(2.2 * np.sin(ph) * np.exp(-t / .5) * np.minimum(1, t / .002)).astype(np.float32)
def snare(d=.22, tone=190):
    t = tt(d); s = .55 * bp(noise(d), 1200, 9000) * np.exp(-t / .06) + .5 * np.sin(2 * np.pi * tone * t) * np.exp(-t / .03)
    return s.astype(np.float32)
def clap(d=.25):
    t = tt(d); e = np.zeros_like(t)
    for o in (0, .011, .022): e += np.exp(-np.maximum(0, t - o) / .008) * (t >= o)
    e += .6 * np.exp(-np.maximum(0, t - .03) / .07) * (t >= .03)
    return (bp(noise(d), 900, 6000) * e).astype(np.float32)
def hat(d=.05, dec=.015, f=8000): t = tt(d); return (hp(noise(d), f) * np.exp(-t / dec)).astype(np.float32)
def ohat(d=.25): t = tt(d); return (hp(noise(d), 7000) * np.exp(-t / .09)).astype(np.float32)
def crashlike(d=1.6):  # prato longo escuro, sem cara de efeito pronto
    t = tt(d); return (bp(noise(d), 3000, 12000) * np.exp(-t / .5) * .6 + lp(noise(d), 900) * np.exp(-t / .15) * .3).astype(np.float32)
def subdrop(d=1.4, f0=80, f1=26):
    t = tt(d); f = f1 + (f0 - f1) * np.exp(-t / .35); return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .6)).astype(np.float32)
def pluck(f, d=.35, cut=4000, dec=.12):
    s = supersaw(f, d, 3, .006) * adsr(d, .002, dec, 0, .02); return lp(s, cut)
def stab(notes, d, cut=3000, dec=.18, sus=.15, n=7, spread=.014):
    s = sum(supersaw(midi(m), d, n, spread) for m in notes) / len(notes); return lp(s * adsr(d, .004, dec, sus, .03), cut, 2)
def reese(f, d, cut=900):
    t = tt(d); s = saw(f, d, -.006) + saw(f, d, .006) + .6 * np.sin(2 * np.pi * f / 2 * t)
    return lp(np.tanh(s * .9).astype(np.float32) * adsr(d, .01, 9, 1, .03), cut, 4)
def obass(f, d=.2, cut=700):  # baixo de contratempo do electro
    s = saw(f, d) * .7 + .5 * np.sign(np.sin(2 * np.pi * f * tt(d))); return lp((s * adsr(d, .003, .12, .3, .03)).astype(np.float32), cut, 2)
def wobble_chord(notes, d, rate, cut0=500, cut1=4500):  # acorde com filtro em LFO (future bass)
    s = sum(supersaw(midi(m), d, 7, .02) for m in notes) / len(notes)
    t = tt(d); lfo = .5 - .5 * np.cos(2 * np.pi * rate * t)
    out = np.zeros_like(s); B = 512; zi = None
    for i in range(0, len(s), B):
        c = cut0 + (cut1 - cut0) * lfo[i]; sos = butter(2, c, 'lowpass', fs=SR, output='sos')
        if zi is None: zi = sosfilt_zi(sos) * 0
        out[i:i + B], zi = sosfilt(sos, s[i:i + B], zi=zi)
    return (out * adsr(d, .01, 9, 1, .04)).astype(np.float32)
def riser(d, lo=200, hi=9000, tonal=None):
    # ruído com filtro abrindo + tom subindo; termina no ponto exato (o motor posiciona em t_fim - d)
    t = tt(d); u = t / d; n = noise(d); out = np.zeros_like(n); B = 512; zi = None
    for i in range(0, len(n), B):
        c = lo * (hi / lo) ** (u[i] ** 1.6); sos = butter(2, [max(80, c * .5), min(SR / 2 - 200, c * 1.3)], 'bandpass', fs=SR, output='sos')
        if zi is None: zi = sosfilt_zi(sos) * 0
        out[i:i + B], zi = sosfilt(sos, n[i:i + B], zi=zi)
    out *= u ** 2 * 1.4
    if tonal: f = tonal * 2 ** (2 * u); out += .25 * supersaw(1, d, 3) * 0 + .22 * np.sin(2 * np.pi * np.cumsum(f) / SR) * u ** 1.5
    return out.astype(np.float32)
def snareroll(d, start=4):  # caixa acelerando até o drop
    out = np.zeros(int(d * SR), np.float32); t = 0.0
    while t < d - .02:
        u = t / d; step = (1 / start) * (1 - .82 * u); add(out, snare(.12) * (.25 + .75 * u), t, 1); t += step
    return out
def downlifter(d=1.0):
    t = tt(d); return (lp(noise(d), 3000) * np.exp(-t / .3) * .5 + .4 * np.sin(2 * np.pi * np.cumsum(220 * 2 ** (-3 * t / d)) / SR) * np.exp(-t / .4)).astype(np.float32)

# ---------------- narrativa ----------------
class Narr:
    def __init__(self, energia, drops=(), paradas=(), impactos=(), subida_tom=None, fim=None, riser_len=1.6):
        self.k = sorted(energia); self.drops = list(drops); self.paradas = list(paradas); self.imp = list(impactos)
        self.lift = subida_tom; self.fim = fim; self.rl = riser_len
    def E(self, t):
        ts = [a for a, _ in self.k]; vs = [b for _, b in self.k]; return float(np.interp(t, ts, vs))
    def parado(self, t):
        for a, d in self.paradas:
            if a <= t < a + d: return True
        for dt in self.drops:  # buraco curto antes de cada drop
            if dt - .14 <= t < dt: return True
        return self.fim is not None and t >= self.fim

STYLES = {
    'electro':    dict(bpm=126, prog=[[57, 60, 64, 67], [53, 57, 60, 64], [48, 55, 60, 64], [55, 59, 62, 67]], roots=[33, 29, 36, 31]),
    'dnb':        dict(bpm=172, prog=[[57, 60, 64, 71], [53, 57, 60, 67], [55, 59, 62, 66], [52, 55, 59, 64]], roots=[33, 29, 31, 28]),
    'futurebass': dict(bpm=150, prog=[[53, 57, 60, 64], [55, 59, 62, 67], [52, 55, 59, 64], [57, 60, 64, 69]], roots=[29, 31, 28, 33]),
}

def render(style, N, dur):
    S = STYLES[style]; BEAT = 60 / S['bpm']; ST = BEAT / 4; BAR = 4 * BEAT
    drums, bass, harm, lead, fx = (np.zeros(int(dur * SR), np.float32) for _ in range(5))
    kicks = []
    nst = int(dur / ST) + 1
    for i in range(nst):
        t = i * ST; e = N.E(t); s16 = i % 16; bar = int(t / BAR); ch = S['prog'][bar % 4]; root = S['roots'][bar % 4]
        tr = 2 if (N.lift and t >= N.lift) else 0; ch = [m + tr for m in ch]; root += tr
        if N.parado(t): continue
        if style == 'electro':
            if e > .35 and s16 % 4 == 0: add(drums, kick(), t, 1); kicks.append(t)
            if e > .45 and s16 in (4, 12): add(drums, clap(), t, .7)
            if e > .22 and s16 % 4 == 2: add(drums, ohat(.18), t, .22 + .2 * e)
            if e > .62: add(drums, hat(), t, .10 + (.08 if s16 % 2 else 0))
            if e > .3 and s16 % 4 == 2: add(bass, obass(midi(root + 12), ST * 1.8, 400 + 1400 * e), t, .9)
            if e > .8 and s16 in (3, 7, 11, 15): add(bass, obass(midi(root + 24), ST * .9, 1800), t, .35)
            if s16 % 8 == 0 or (e > .7 and s16 in (6, 14)): add(harm, stab(ch, BEAT * (2 if e < .5 else .9), 600 + 4200 * e ** 1.5, .25 if e > .5 else 1.2, .2), t, .5)
            if e > .78: add(lead, pluck(midi(ch[(i * 3) % 4] + 12), ST * 1.6, 2500 + 4000 * (e - .78) * 4), t, .22)
        elif style == 'dnb':
            half = e < .5
            pat_k = {0, 10} if not half else {0}
            pat_s = {4, 12} if not half else {8}
            if e > .3 and s16 in pat_k: add(drums, kick(.35, 160, 50), t, 1); kicks.append(t)
            if e > .3 and s16 in pat_s: add(drums, snare(), t, .8)
            if e > .55 and s16 in (7, 14): add(drums, snare(.08) * .5, t, .35)  # ghost
            if e > .2 and s16 % 2 == 0: add(drums, hat(.04, .012), t, .12 + .1 * e)
            if e > .7 and s16 % 2 == 1: add(drums, hat(.03, .008), t, .07)
            if s16 == 0 and e > .28: add(bass, reese(midi(root), BAR * (.98 if bar % 2 == 0 else .48), 250 + 1500 * e ** 1.3), t, .8)
            if s16 == 0: add(harm, stab(ch, BAR, 400 + 2600 * e, 9, 1, 5, .008), t, .28)
            if e > .75 and s16 % 3 == 0: add(lead, pluck(midi(ch[(i // 3) % 4] + 24), ST * 2, 3500, .08), t, .2)
        else:  # futurebass: meio-tempo, 808, acordes com wobble, hats em rolo
            if e > .32 and s16 in (0, 7, 10): add(drums, kick(.4, 140, 48), t, .9); kicks.append(t)
            if e > .4 and s16 == 8: add(drums, clap(), t, .8); add(drums, snare(), t, .4)
            if e > .2:
                if s16 % 2 == 0: add(drums, hat(.04, .012), t, .14)
                if e > .65 and s16 in (13, 14, 15):
                    for q in range(2): add(drums, hat(.03, .008), t + q * ST / 2, .09)
            if e > .3 and s16 in (0, 7, 10): add(bass, k808(midi(root), BEAT * 1.6, .5 if s16 == 0 else 0), t, .8)
            if s16 == 0:
                if e > .72: add(harm, wobble_chord([m + 12 for m in ch], BAR, (S['bpm'] / 60) * (2 if e > .9 else 1)), t, .45)
                else: add(harm, stab([m + 12 for m in ch], BAR, 500 + 3000 * e, 9, 1, 7, .016), t, .3)
            if e > .55 and s16 % 4 == 2: add(lead, pluck(midi(ch[(i // 2) % 4] + 24), ST * 2.4, 5000, .1) , t, .16)
    # sidechain: tudo menos a bateria "respira" no bumbo (mais fundo quanto mais energia)
    sc = np.ones(len(harm), np.float32); w = int(.18 * SR); cur = (1 - np.exp(-np.arange(w) / SR / .05)).astype(np.float32)
    for k in kicks:
        i = int(k * SR); n = min(w, len(sc) - i); d = .45 + .4 * N.E(k)
        if n > 0: sc[i:i + n] = np.minimum(sc[i:i + n], 1 - d + d * cur[:n])
    music = drums * .9 + (bass * .8 + harm * .7 + lead * .7) * sc
    # filtro mestre que acompanha a energia (fecha nos vales, abre nos picos)
    out = np.zeros_like(music); B = 512; zi = None
    for i in range(0, len(music), B):
        c = 350 * (16000 / 350) ** min(1, N.E(i / SR) ** .8 + .05); sos = butter(2, min(c, 16000), 'lowpass', fs=SR, output='sos')
        if zi is None: zi = sosfilt_zi(sos) * 0
        out[i:i + B], zi = sosfilt(sos, music[i:i + B], zi=zi)
    # volume também anda com a energia (até 14 dB entre vale e pico), suavizado em 60 ms
    tg = np.arange(0, dur, .01); gv = 10 ** (-14 * (1 - np.array([N.E(x) for x in tg])) / 20)
    gv = np.convolve(np.pad(gv, 3, mode='edge'), np.ones(7) / 7, 'valid'); out *= np.interp(np.arange(len(out)) / SR, tg, gv).astype(np.float32)
    # eventos de narrativa: risers que terminam no drop, impacto no drop, paradas com downlifter
    for dt in N.drops:
        L = min(N.rl, dt - .2); add(fx, riser(L, 250, 9000, 220), dt - L - .14, .5); add(fx, snareroll(L * .8), dt - L * .8 - .14, .45)
        add(fx, kick(.5, 170, 40, 1.3), dt, 1.1); add(fx, subdrop(1.3), dt, .9); add(fx, crashlike(), dt, .35)
    for t0 in N.imp: add(fx, kick(.5, 160, 38, 1.2), t0, .9); add(fx, subdrop(.9, 70, 28), t0, .7)
    for a, d in N.paradas: add(fx, downlifter(min(.8, d + .2)), a, .4)
    mix = out + fx * .8
    if N.fim is not None:  # fita parando antes do fim do vídeo
        i2 = int(N.fim * SR); i1 = i2 - int(.45 * SR); seg = mix[i1:i2].copy(); n = len(seg)
        rate = np.linspace(1, .15, n); pos = np.cumsum(rate); pos = pos / pos[-1] * (n - 1) * .55
        mix[i1:i2] = np.interp(pos, np.arange(n), seg) * np.linspace(1, 0, n); mix[i2:] = 0
    return (mix / (np.abs(mix).max() + 1e-9) * .9).astype(np.float32)
