import sys, json, subprocess
import synth
from synth import *
# DIA 11 — trilha remontada a partir da música enviada pelo Luis + foley sintetizado
CFG = json.load(open('cfg.json'))
TEND = CFG['TEND']; PURP = CFG['PURP']; LOOP = CFG['LOOP']; C = CFG['cta']   # tempos da chamada final
def dec(path, ch=1):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', str(ch), '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
M = dec(CFG['music']); V = dec(CFG['voice'])
mus, sfx, voice = buf(TEND), buf(TEND), buf(TEND)
v = hp(V, 80); v = v + 0.0 * v; voice[:min(len(v), len(voice))] = v[:len(voice)]
BAR = 4 * 60 / 124.4; F1, F2, G1, G2, Q, I0 = 11.53, 53.97, 3.816, 46.25, 44.32, -0.04
A1, A2 = 9.94, 42.22   # downbeats do vídeo (drop do contador e dos cinco cortes)
ph = lambda v0, a: (v0 - a) % BAR
# (v0, v1, src0, ganho dB, lowpass)
SEGS = [(0, 3.55, F1 + 2 * BAR + ph(0, A1), 0, None),
        (3.55, 6.08, I0 + ph(3.55, A1), 3.5, None),
        (6.08, A1, F1 - (A1 - 6.08), 1, None),
        (A1, 31.2, F1, 0, None),
        (31.2, 35.9, G2 + ph(31.2, A1), 1.5, None),
        (35.9, 39.9, G1 + ph(35.9, A1), 1.5, None),
        (39.9, 40.7, Q + ph(39.9, A1), 4, 900),
        (40.7, A2, F2 - (A2 - 40.7), 2, None),
        (A2, PURP, F2, 0, None),
        (PURP, TEND, 0.5, 2, 700)]
for v0, v1, s0, gdb, lpf in SEGS:
    xf = .03 if v0 in (39.9, 40.7, PURP) else .015
    a = int(max(0, s0 - xf) * SR); n = int((v1 - v0 + 2 * xf) * SR); seg = M[a:a + n].copy()
    if lpf: seg = lp(seg, lpf, 4)
    f = int(xf * SR); w = np.ones(len(seg), np.float32); w[:f] = np.linspace(0, 1, f); w[-f:] = np.linspace(1, 0, f)
    add(mus, seg * w * 10 ** (gdb / 20), v0 - xf)
# ---- foley ----
def snip():
    a = crackle(.06, 120) * .6; a[:len(card(.03))] += card(.03) * 1.5; return a
E = []
def ev(fn, t, g): E.append((fn, t, g))
# gancho
ev(card(.05), .21, .6); ev(kick(.5, 120, 40, 1.1), .69, .9); ev(subdrop(.8, 70, 30), .7, .7); ev(glass(midi(86), 1.0, .02) * .3, .72, .6)
ev(paperflutter(.35), .1, .35)
ev(relay() * 2, 1.33, .8); [ev(keyclick(.35), 1.36 + i * .03, .3) for i in range(11)]; ev(tink(2600, .4), 2.3, .45)
ev(swell(.8, 300, 5000), 2.4, .45); ev(pluck_bend(220, .5, 12, .2), 2.45, .5)
# vinheta
[ev(pencil(.07, 90), 3.66 + i * .02, .3) for i in range(10)]; ev(pencil(.35, 70), 3.9, .5)
# placar + contador + multidão
[ev(card(.05), 6.93 + i * .16, .55) for i in range(4)]; ev(ratchet(1.0, 30) * .6, 7.0, .35)
ev(ratchet(.9, 28) * .7, A1, .5); ev(subdrop(1.0, 75, 32), A1, .9); ev(relay() * 2, 10.9, .8); ev(tink(2400, .5), 10.92, .45)
[ev(tink(1800 + 90 * (i % 7), .12), 11.15 + i * .025, .12) for i in range(30)]
# escada
[ev(clunk(), 13.72 + i * .09, .5) for i in range(4)]
for i, tb in enumerate([14.6, 14.88, 15.04, 15.38]): ev(kick(.25, 160, 70, .6), tb, .5); ev(pluck_bend(midi(62 + 4 * i), .3, 2, .1), tb, .45)
ev(crackle(.4, 50), 15.4, .4)
# 1 página
ev(waterdrop(300, 1300, .1), 15.96, .5); ev(card(.05), 16.5, .5); ev(card(.05), 16.86, .5); [ev(keyclick(.3), 17.0 + i * .05, .25) for i in range(5)]; ev(card(.05), 18.24, .5)
# 2 streamers
ev(waterdrop(300, 1300, .1), 19.61, .5); [ev(card(.05), 19.7 + i * .1, .5) for i in range(3)]; ev(marble(1.3, 18), 20.3, .3)
ev(tink(2200, .4), 21.07, .4); ev(tink(2500, .4), 21.19, .4); ev(clunk(), 21.31, .6); ev(swell(.5, 600, 6000) * .6, 22.2, .4)
# 3 skill
ev(waterdrop(300, 1300, .1), 23.99, .5); ev(ratchet(.7, 16) * .6, 24.16, .35); ev(tink(2600, .5), 24.86, .45)
ev(pluck_bend(330, .5, 7, .15), 25.9, .4); ev(relay() * 2, 26.45, .8); ev(kick(.3, 150, 60, .6), 26.45, .5)
[ev(keyclick(.5), 26.47 + i * .04, .3) for i in range(13)]; ev(glass(midi(88), 1.0, .02) * .3, 26.6, .5)
# 4 pasta e pedido
ev(waterdrop(300, 1300, .1), 27.23, .5); ev(clunk(), 27.3, .6); ev(card(.05), 27.55, .5); ev(swell(.3, 3000, 500) * .5, 28.24, .3); ev(kick(.35, 120, 50, .7), 28.56, .7); ev(paperflutter(.3), 28.58, .4)
ev(card(.05), 29.05, .5); [ev(keyclick(.6), 29.75 + i * .042, .35) for i in range(24)]; ev(relay() * 2, 30.95, .8); ev(swell(.3, 1500, 7000) * .6, 30.95, .35)
# escuta, nota, sustos, risadas
ev(marble(1.2, 22), 31.55, .3); [ev(tink(900 + 40 * i, .15), 32.75 + i * .05, .15) for i in range(18)]
for tb in (34.75, 34.85): ev(snap(), tb, .7); ev(subdrop(.5, 90, 40), tb, .5)
for i, tb in enumerate((35.3, 35.38, 35.46)): ev(pluck_bend(midi(70 + 3 * i), .25, 5, .08), tb, .45)
# corta, em pé, legenda
[ev(card(.04), 35.95 + i * .05, .35) for i in range(6)]; ev(clunk(), 36.39, .5); ev(snip(), 36.69, .8); ev(snip(), 37.43, .8)
ev(ratchet(.5, 10) * .7, 37.9, .4); ev(kick(.3, 140, 60, .5), 38.47, .5); [ev(keyclick(.6), 39.35 + i * .15, .4) for i in range(3)]
# queda: relógio
[ev(tick if False else (lambda: (bp(noise(.03), 2500, 6000) * env(.03, .0005, .006)))(), tb, .45) for tb in np.arange(40.7, 42.1, .25)]
ev(tink(2400, .4), 41.25, .35); ev(swell(1.3, 300, 8000), 40.9, .4)
ev(subdrop(1.2, 75, 32), A2, 1.0); ev(kick(.5, 140, 40, 1.2), A2, .9); [ev(waterdrop(300 + 70 * i, 1100, .08), A2 + i * .06, .4) for i in range(5)]
[ev(tink(2600 + 120 * i, .3), 42.87 + i * .05, .25) for i in range(5)]; ev(swell(.4, 800, 5000) * .5, 43.2, .3)
# amigo
ev(waterdrop(300, 1000, .1), 44.39, .5); [ev(pluck_bend(midi(64 + 2 * i), .25, 3, .1), 45.6 + i * .42, .35) for i in range(3)]
ev(card(.05), 47.65, .5); ev(relay() * 2, 48.47, .7); ev(swell(.35, 1500, 7000) * .5, 48.47, .35)
# guia
ev(card(.05), 49.3, .5); [ev(tink(1800 + 300 * i, .3), C['chk'] + i * .12, .35) for i in range(4)]; ev(clunk(), C['comp'], .7); ev(kick(.3, 150, 60, .6), C['comp'], .5)
# chamada final
ev(relay() * 2, C['fol'], .8); ev(keyclick(1), C['fol'], .5); ev(tink(2400, .4), C['fol'] + .05, .4)
ev(waterdrop(300, 1000, .12), C['curte'] + .04, .7); ev(relay() * 2, C['like'], .8); ev(tink(3000, .4), C['like'] + .02, .4)
[ev(keyclick(.7), C['type'] + i * .09, .45) for i in range(3)]
ev(relay() * 2, C['send'], .7); ev(swell(.25, 1500, 7000) * .6, C['send'], .4); ev(waterdrop(500, 1300, .1), C['send'] + .05, .5); ev(card(.05), C['card'], .6)
ev(lp(noise(.08), 1500) * env(.08, .0005, .02), PURP, .9); ev(glass(midi(81), 1.6, .02) * .4, PURP + .02, 1); ev(glass(midi(88), 1.6, .02) * .4, PURP + .28, 1)
ev(kick(.5, 120, 40, 1), LOOP + .22, .6)
for fn, t, g in E: add(sfx, fn, t, g)
# elemento de destaque: comprime (squish), voa (pluck) e abre (pop) — 30% mais baixo que no Dia 10 v3
HS = CFG['HS']
for i in range(len(HS) - 1):
    t1, t0n = HS[i][1], HS[i + 1][0]
    if t0n - t1 < .05: continue
    add(sfx, waterdrop(420, 180, .09), t1 - .1, .45 * .7)
    add(sfx, pluck_bend(330 + 20 * (i % 5), min(.5, t0n - t1), 7, .12), t1, .3 * .7)
    add(sfx, waterdrop(300, 1500, .08), t0n, .5 * .7); add(sfx, tink(2400 + 150 * (i % 4), .2), t0n + .01, .18 * .7)
# "Claude" vira a logo girando
for tl in CFG['claude']: add(sfx, swell(.3, 1500, 8000) * .6, tl - .05, .3); add(sfx, glass(midi(90), .9, .01) * .3, tl + .2, .7)
sfx = reverb(sfx, .5, .1)
# ---- mix: voz em cima, música com ducking, efeitos ----
rms = lambda x: np.sqrt((x ** 2).mean()) + 1e-9
vv = voice / rms(voice[voice != 0]) * .1
e = follower(vv); e = e / (e.max() + 1e-9); duck = 1 - .5 * np.clip(e * 3, 0, 1)
m = mus / rms(mus) * .1 * 10 ** (-12 / 20) * duck
s = sfx / (np.abs(sfx).max() + 1e-9) * .5 * 10 ** (-9 / 20)
out = vv + m + s
f = int(.004 * SR); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
db = lambda a: 20 * np.log10(rms(a))
print('voz', round(db(vv[vv != 0]), 1), 'mus', round(db(m), 1), 'sfx', round(db(s), 1))
write(CFG['out'], out.astype(np.float32))
