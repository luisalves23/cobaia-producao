"""Synth + foley sem samples: tudo gerado aqui (sem banco de efeitos genérico)."""
import numpy as np, wave
from scipy.signal import butter, sosfilt, fftconvolve

SR = 48000; END = 14.0; BPM = 120; BEAT = 60 / BPM
W = dict(uma=1.00, ideia=1.22, solta=1.55, vira1=2.28, um=2.96, plano1=3.10, o=4.04, plano2=4.22,
         vira2=4.79, codigo1=5.22, eo=6.05, codigo2=6.36, ganha=8.12, vida=8.45)
BREAK, DROP = 7.0, 8.0
R = np.random.default_rng(7)

def buf(sec=END): return np.zeros(int(sec * SR), np.float32)
def tt(d): return np.arange(int(d * SR)) / SR
def add(b, s, t, g=1.0):
    i = int(round(t * SR));
    if i < 0: s = s[-i:]; i = 0
    n = min(len(s), len(b) - i)
    if n > 0: b[i:i + n] += g * s[:n]
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'bandpass', fs=SR, output='sos'), x).astype(np.float32)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'lowpass', fs=SR, output='sos'), x).astype(np.float32)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'highpass', fs=SR, output='sos'), x).astype(np.float32)
def env(d, a=0.002, dec=0.2):
    t = tt(d); return (np.minimum(1, t / max(a, 1e-4)) * np.exp(-np.maximum(0, t - a) / dec)).astype(np.float32)
def noise(d): return R.standard_normal(int(d * SR)).astype(np.float32)
def midi(n): return 440 * 2 ** ((n - 69) / 12)
def reverb(x, sec=1.6, wet=0.25, bright=6000, pre=0.012):
    n = int(sec * SR); ir = R.standard_normal(n).astype(np.float32) * np.exp(-np.arange(n) / SR * 6.9 / sec)
    ir = lp(ir, bright); ir = np.concatenate([np.zeros(int(pre * SR), np.float32), ir]); ir /= np.sqrt((ir ** 2).sum())
    y = fftconvolve(x, ir)[:len(x)].astype(np.float32); return x * (1 - wet) + y * wet * 1.2

# ---------- instrumentos ----------
def kick(d=0.45, f0=110, f1=42, punch=1.0):
    t = tt(d); f = f1 + (f0 - f1) * np.exp(-t / 0.045); ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) * np.exp(-t / 0.16); s += punch * 0.3 * hp(noise(d), 2000) * np.exp(-t / 0.004); return s.astype(np.float32)
def hat(d=0.06, dec=0.018, f=7000): return (hp(noise(d), f) * env(d, .0005, dec)).astype(np.float32)
def shaker(d=0.09): return (bp(noise(d), 4000, 11000) * env(d, 0.012, 0.03)).astype(np.float32)
def snap(d=0.25):  # clap-ish
    e = sum(env(d, .0005, .01) * (tt(d) >= k) for k in [0, .011, .022]) + 0.5 * env(d, .0005, .09)
    return (bp(noise(d), 900, 5000) * e).astype(np.float32)
def ks(freq, d=1.2, bright=0.5, decay=0.996, bend=0.0):
    """Karplus-Strong (corda/elástico). bend: semitons de queda no início (elástico)."""
    n = int(d * SR); P = SR / freq; L = int(P) + 1
    line = (R.uniform(-1, 1, L) * 1.0).astype(np.float32); line = lp(line, 300 + bright * 9000)
    out = np.zeros(n, np.float32); idx = 0
    for i in range(n):
        pcur = P * (2 ** (bend * np.exp(-i / SR / 0.06) / 12)) if bend else P
        j = int(pcur); a = line[(idx) % L]; b = line[(idx + 1) % L]
        v = decay * 0.5 * (a + b); out[i] = a; line[idx % L] = v; idx += 1
        if bend and i % 64 == 0:  # re-size delay line for pitch bend
            pass
    return out
def pluck_bend(freq, d=0.7, semis=5, dec=0.25):
    """Elástico beliscado: senoide + harmônicos com queda de afinação e batimento."""
    t = tt(d); f = freq * 2 ** (semis * np.exp(-t / 0.05) / 12); ph = 2 * np.pi * np.cumsum(f) / SR
    s = np.sin(ph) + 0.5 * np.sin(2 * ph + 0.3) * np.exp(-t / 0.08) + 0.25 * np.sin(3 * ph) * np.exp(-t / 0.05)
    s *= np.exp(-t / dec) * (1 + 0.25 * np.sin(2 * np.pi * 7 * t)); return (s * np.minimum(1, t / 0.002)).astype(np.float32)
def kalimba(freq, d=1.2):
    t = tt(d); s = np.sin(2 * np.pi * freq * t) * np.exp(-t / 0.5) + 0.35 * np.sin(2 * np.pi * freq * 5.4 * t) * np.exp(-t / 0.05)
    s += 0.15 * np.sin(2 * np.pi * freq * 2.0 * t) * np.exp(-t / 0.2); s += 0.2 * hp(noise(d), 3000) * np.exp(-t / 0.002)
    return (s * np.minimum(1, t / 0.001)).astype(np.float32)
def pizz(freq, d=0.6):  # contrabaixo pizzicato
    t = tt(d); ph = 2 * np.pi * freq * t
    s = (np.sin(ph) + 0.6 * np.sin(2 * ph) * np.exp(-t / .1) + 0.3 * np.sin(3 * ph) * np.exp(-t / .05)) * np.exp(-t / 0.28)
    s += 0.15 * bp(noise(d), 200, 1200) * np.exp(-t / 0.01); return lp(s.astype(np.float32), 1800)
def glass(freq, d=2.0, att=0.06, vib=4.5):  # harmônica de vidro
    t = tt(d); v = 1 + 0.004 * np.sin(2 * np.pi * vib * t)
    s = sum(a * np.sin(2 * np.pi * freq * m * np.cumsum(v) / SR) for m, a in [(1, 1), (2.0, .35), (3.01, .12), (4.2, .05)])
    e = np.minimum(1, t / att) * np.exp(-t / (d * 0.45)); return (s * e).astype(np.float32)
def tink(freq, d=0.8):
    t = tt(d); s = sum(a * np.sin(2 * np.pi * freq * m * t) * np.exp(-t / dd) for m, a, dd in [(1, 1, .4), (2.76, .5, .15), (5.4, .3, .06), (8.9, .15, .03)])
    return (s * np.minimum(1, t / 0.0005)).astype(np.float32)
def pad(notes, d, cut=1800, att=0.4, rel=0.6, det=0.004):
    t = tt(d); s = np.zeros_like(t, dtype=np.float32)
    for n in notes:
        f = midi(n)
        for dd in (-det, 0, det): s += (2 * ((f * (1 + dd) * t) % 1) - 1).astype(np.float32)
    s = lp(s, cut, 2); e = np.minimum(1, t / att) * np.minimum(1, (d - t) / rel); return (s * e / (len(notes) * 3)).astype(np.float32)
def supersaw(notes, d, cut=5000, att=0.01, rel=0.08, det=0.012, voices=5):
    """Acorde de future bass (Dia 13): serras desafinadas abertas no estéreo do mono, brilho de cima, ataque curto."""
    t = tt(d); s = np.zeros_like(t, dtype=np.float32)
    for n in notes:
        f = midi(n)
        for k in range(voices):
            dd = det * (k / (voices - 1) - .5) * 2; ph = R.uniform(0, 1)
            s += (2 * ((f * (1 + dd) * t + ph) % 1) - 1).astype(np.float32)
    s = lp(s, cut, 2); e = np.minimum(1, t / att) * np.minimum(1, np.maximum(0, d - t) / rel)
    return (s * e / (len(notes) * voices)).astype(np.float32)
def subdrop(d=1.6, f0=70, f1=28):
    t = tt(d); f = f1 + (f0 - f1) * np.exp(-t / 0.5); return (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.7) * np.minimum(1, t / 0.005)).astype(np.float32)
def swell(d=1.0, lo=300, hi=6000):  # ruído em reverso subindo (não é whoosh: é filtro abrindo devagar)
    n = noise(d); t = tt(d); out = np.zeros_like(n); seg = int(SR * 0.02)
    for i in range(0, len(n), seg):
        k = i / len(n); f = lo * (hi / lo) ** k; out[i:i + seg] = bp(n[max(0, i - 2000):i + seg], f * 0.8, min(f * 1.25, 20000))[-len(out[i:i + seg]):]
    return (out * (t / d) ** 2.5).astype(np.float32)
def reverse(x): return x[::-1].copy()
def tapestop(x, d=0.5):
    """aplica parada de fita no final de x (último d s)."""
    n = int(d * SR); seg = x[-n:]; t = np.arange(n) / n; rate = (1 - t) ** 1.6; pos = np.cumsum(rate); pos = pos / pos[-1] * (n * 0.45)
    y = np.interp(pos, np.arange(n), seg) * (1 - t) ** 0.5; x = x.copy(); x[-n:] = y; return x
# ---------- foley sintético ----------
def waterdrop(f0=600, f1=1700, d=0.12):
    t = tt(d); f = f0 * (f1 / f0) ** np.minimum(1, t / 0.035); s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.03)
    return (s * np.minimum(1, t / 0.001)).astype(np.float32)
def pencil(d=0.6, dens=60):
    n = bp(noise(d), 2500, 7000); t = tt(d); g = np.zeros_like(t)
    rr = R.uniform(0, 1, int(d * dens));
    for k in rr: g += np.exp(-((t - k * d) / 0.012) ** 2)
    return (n * (0.3 + g) * np.minimum(1, t / .03) * np.minimum(1, (d - t) / .05)).astype(np.float32)
def marble(d=1.2, rate=28):
    t = tt(d); rumble = lp(noise(d), 500) * 0.6; clicks = np.zeros_like(t, dtype=np.float32)
    k = 0.0
    while k < d: c = bp(noise(0.01), 2000, 6000) * env(0.01, .0003, .002); add(clicks, c, k, R.uniform(.3, 1)); k += 1 / rate * R.uniform(.6, 1.4)
    return ((rumble + clicks) * np.sin(np.pi * t / d) ** 0.5).astype(np.float32)
def splat(d=0.5):
    t = tt(d); return (lp(noise(d), 1400) * np.exp(-t / 0.06) + 0.8 * np.sin(2 * np.pi * 70 * t) * np.exp(-t / .08)).astype(np.float32)
def paperflutter(d=0.5, rate=32):
    t = tt(d); am = 0.5 + 0.5 * np.sign(np.sin(2 * np.pi * rate * t + 3 * np.sin(2 * np.pi * 3 * t)))
    return (bp(noise(d), 1500, 7000) * am * np.sin(np.pi * t / d)).astype(np.float32)
def keyclick(heavy=1.0):
    d = 0.08; t = tt(d); return (hp(noise(d), 1800) * np.exp(-t / 0.004) + heavy * 0.6 * np.sin(2 * np.pi * 160 * t) * np.exp(-t / 0.018)).astype(np.float32)
def ratchet(d=0.4, n=10):
    b = np.zeros(int(d * SR), np.float32)
    for i in range(n): add(b, bp(noise(0.008), 2500, 8000) * env(.008, .0002, .0015), d * (i / n) ** 0.7, 0.7)
    return b
def relay():
    d = 0.05; b = np.zeros(int(d * SR), np.float32); c = bp(noise(0.006), 1500, 5000) * env(.006, .0001, .0012)
    add(b, c, 0, 1); add(b, c, 0.007, .6); return b
def clunk():
    d = 0.2; t = tt(d); return (np.sin(2 * np.pi * 85 * t) * np.exp(-t / 0.035) + 0.6 * bp(noise(d), 1000, 4000) * np.exp(-t / 0.004)).astype(np.float32)
def crackle(d, dens=25):
    b = np.zeros(int(d * SR), np.float32)
    for k in R.uniform(0, d, int(d * dens)): add(b, hp(noise(0.003), 2500) * env(.003, .0001, .0006), k, R.uniform(.1, .6))
    return b
def card(d=0.05): t = tt(d); return (bp(noise(d), 1200, 6000) * np.exp(-t / 0.006)).astype(np.float32)

# ---------- voz, ducking, saída ----------
def load_voice(path='voz.wav'):
    w = wave.open(path); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    b = buf(); b[:min(len(b), len(x))] = x[:len(b)]; b[int(7.9 * SR):] *= 1.9; return b
def follower(x, att=0.02, rel=0.28):
    a = np.abs(x); n = int(SR * 0.005); a = np.convolve(a, np.ones(n) / n, 'same'); y = np.zeros_like(a); v = 0
    ka, kr = np.exp(-1 / (att * SR)), np.exp(-1 / (rel * SR))
    for i in range(0, len(a), 48):
        s = a[i]; v = ka * v + (1 - ka) * s if s > v else kr * v + (1 - kr) * s; y[i:i + 48] = v
    return y
def write(path, x):
    st = x if x.ndim == 2 else np.stack([x, x], 1)
    st = st / max(1e-6, np.abs(st).max()) * 0.89
    w = wave.open(path, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
def mix(music, sfx, voice, path, duck=0.5, music_db=-6, sfx_db=-4, report=True, post=2.0, comp=0):
    if comp: sfx = np.tanh(sfx / (np.abs(sfx).max() * comp)).astype(np.float32)
    music = music.copy(); g2 = np.ones_like(music); i0 = int(DROP * SR); g2[i0:] = post; music *= g2
    e = follower(voice); e = e / (e.max() + 1e-9); g = 1 - duck * np.clip(e * 3, 0, 1)
    m = music * 10 ** (music_db / 20) * g; s = sfx * 10 ** (sfx_db / 20)
    def norm(x): r = np.sqrt((x ** 2).mean()) + 1e-9; return x / r
    v = norm(voice) * 0.12
    m = m / (np.sqrt((m ** 2).mean()) + 1e-9) * 0.12 * 10 ** (music_db / 20) if np.abs(m).max() > 0 else m
    s = s / (np.abs(s).max() + 1e-9) * 0.5 * 10 ** (sfx_db / 20) if np.abs(s).max() > 0 else s
    out = v + m + s
    if report:
        db=lambda a:20*np.log10(np.sqrt((a**2).mean())+1e-9)
        for nm,a in [('voz',v),('mus',m),('sfx',s)]: print(nm,' '.join(f'{db(a[int(i*SR):int((i+1)*SR)]):.0f}' for i in range(14)))
    # loop: fades de 4 ms nas pontas para não estalar
    f = int(.004 * SR); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
    write(path, out.astype(np.float32))
