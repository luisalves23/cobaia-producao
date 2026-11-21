# aNN.py — base de áudio tirada do Dia 10 v3, sem a vinheta do calendário. Refazer os tempos com o mapa da música e a corrente.
import synth
from synth import *
import json, subprocess
# DIA 10 — detetive de Wi-Fi: house lo-fi agitada que acompanha a história + foley sintetizado
TEND = 54.8; PURP = 52.4; LOOP = 54.4; RALO = 48.95
mus, sfx = buf(TEND), buf(TEND)
VOZ = 'voz.mp3'
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', VOZ, '-af', 'highpass=f=80,equalizer=f=3500:t=q:w=1:g=1.5,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80',
                      '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; voice = buf(TEND); voice[:min(len(x), len(voice))] = x[:len(voice)]
CH = json.loads(open('dNNchunks.js').read().split('=',1)[1].strip().rstrip(';'))
def sawbass(n, d=.4, cut=500):
    t = tt(d); f = midi(n); s = 2 * ((f * t) % 1) - 1; return lp((s * np.exp(-t / .22) * np.minimum(1, t / .003)).astype(np.float32), cut)
def rim(): d = .06; t = tt(d); return (bp(noise(d), 1500, 4000) * np.exp(-t / .006) + .5 * np.sin(2 * np.pi * 820 * t) * np.exp(-t / .01)).astype(np.float32)
# progressão mais clara (Dm9 Bbmaj7 F C/E) — alto astral
prog = [[62, 65, 69, 72], [58, 62, 65, 69], [60, 65, 69, 72], [59, 64, 67, 72]]; roots = [38, 46, 41, 40]
for bar in range(int(PURP / 2) + 1):
    t0 = bar * 2.0; ch = prog[bar % 4]; root = roots[bar % 4]
    vin = False   # Dossiê 2.0: sem vinheta do calendário
    brk = 28.4 <= t0 + .5 < 32.4        # esperando: tira a batida
    build = 36.0 <= t0 < 38.76
    big = t0 >= 38.76 and t0 < RALO
    cut = 900 if vin else 1400 if t0 < 16 else 2200 if t0 < 28 else 1000 if brk else 1800 if build else 4000 if big else 2000
    add(mus, pad(ch, 2.0, cut, .02, .25), t0, .55)
    for k in range(4):
        tb = t0 + k * BEAT
        if tb >= PURP: break
        add(mus, hat(.05, .02), tb + BEAT / 2, .45)
        if vin: continue
        if not brk or k == 0: add(mus, kick(f0=105, punch=.7), tb, 1)
        if k in (1, 3) and not brk: add(mus, snap(), tb, .5)
    if vin: continue
    for k in range(16):
        tb = t0 + k * BEAT / 4
        if tb < PURP: add(mus, shaker(), tb, (.2 if k % 2 else .1) * (1.3 if brk else 1))
    if brk: continue
    for off in [0.75, 1.5, 2.75, 3.5]:
        if t0 + off * BEAT < PURP: add(mus, pad(ch, .22, cut + 800, .005, .1), t0 + off * BEAT, .5)
    for k in (3, 7, 11, 14): add(mus, rim(), t0 + k * BEAT / 4, .35)
    for k, off in enumerate([0, .75, 1.5, 2.5, 3.25]):
        if t0 + off * BEAT < PURP: add(mus, sawbass(root + (12 if k == 3 else 0), cut=450 if t0 < 30 else 900), t0 + off * BEAT, .8)
    if big:
        for k in range(8): add(mus, kalimba(midi(ch[k % 4] + 12), .5) * .5, t0 + k * BEAT / 2, .35)
add(mus, swell(1.6, 300, 7000), 37.16, .6)
mus = reverb(mus, 1.1, .14)
# fita parando no "pro ralo"
i1 = int(51.56 * SR); i2 = int(52.36 * SR); seg = tapestop(mus[i1:i2].copy(), .8); mus[i1:i2] = seg; mus[i2:] = 0
add(mus, pad([62, 69, 74, 77], LOOP - PURP, 900, .3, .8), PURP + .05, .35)
add(mus, glass(midi(81), 1.6, .02) * .4, PURP + .02, 1); add(mus, glass(midi(88), 1.6, .02) * .4, PURP + .28, 1)
add(mus, kick(.5, 120, 40, 1), 54.6, .6)   # quique que emenda no começo
# ---- foley ----
for c in CH: add(sfx, waterdrop(260, 520, .09) * .8, c['t'] - .04, .3)
for s0 in [7.8, 11.1, 16.0, 19.6, 23.3, 28.4, 32.4, 36.0, 40.1, 44.86, 47.5, 48.95]: add(sfx, clunk(), s0 + .02, .7); add(sfx, ratchet(.3, 9) * .6, s0 + .05, .35)
# gancho
add(sfx, snap(), .84, .8); add(sfx, crackle(.3, 50), .86, .5); add(sfx, pluck_bend(220, .9, -12, .5), .95, .6)
for i in range(16): add(sfx, keyclick(.4), .84 + i * .035, .35)
add(sfx, relay() * 2, 2.82, .9); add(sfx, tink(2400, .5), 2.84, .4); add(sfx, kick(.3, 140, 50, .8), 2.82, .6)
for i in range(14): add(sfx, keyclick(.4), 2.85 + i * .035, .35)
add(sfx, card(.05), 3.9, .6); add(sfx, waterdrop(400, 1300, .1), 4.1, .6)
# operadora
add(sfx, marble(.6, 26), 8.0, .4); add(sfx, swell(.4, 500, 4000), 9.3, .4); add(sfx, relay() * 2, 10.3, .8); add(sfx, tink(2200, .3), 10.31, .3); add(sfx, waterdrop(300, 900, .1), 10.4, .6)
# Claude Code
add(sfx, paperflutter(.35), 11.35, .5); add(sfx, card(.05), 11.62, .6)
for i in range(10): add(sfx, keyclick(.6), 11.66 + i * .045, .4)
add(sfx, tink(2600, .6), 12.1, .4); add(sfx, marble(.8, 24), 12.96, .35)
for i in range(3): add(sfx, relay() * 2, 13.88 + i * .14, .6)
for i in range(3): add(sfx, waterdrop(500, 1100, .08), 14.72 + i * .1, .4)
# velocímetro
add(sfx, ratchet(.6, 18) * .7, 16.62, .5); add(sfx, card(.05), 17.7, .5); add(sfx, splat(.4), 18.9, .5); add(sfx, subdrop(.7, 70, 34), 19.1, .6)
# caça
for i in range(4): add(sfx, waterdrop(350 + 60 * i, 900, .07), 19.8 + i * .08, .35)
add(sfx, marble(1.2, 20), 20.46, .35); add(sfx, subdrop(.9, 60, 30), 21.98, .8); add(sfx, crackle(.5, 40), 22.0, .4)
for i in range(17): add(sfx, keyclick(.5), 22.22 + i * .04, .35)
# cereja + vizinhança + canais
add(sfx, swell(.45, 2000, 6000) * .5, 23.96, .3); add(sfx, kick(.3, 160, 60, .5), 24.46, .6); add(sfx, waterdrop(500, 1500, .1), 24.46, .7); add(sfx, pluck_bend(330, .3, 5, .1), 24.75, .4)
for i in range(5): add(sfx, tink(1500 + 200 * i, .25), 25.3 + i * .07, .25)
for i in range(5): add(sfx, waterdrop(300 + 80 * i, 800, .08), 26.7 + i * .09, .35)
add(sfx, relay() * 2, 27.24, .8)
# briga pelo mesmo espaço
for tb in np.arange(28.5, 29.3, .27): add(sfx, pluck_bend(110, .35, 3, .1), tb, .6)
add(sfx, kick(.4, 150, 40, 1.2), 29.32, .9); add(sfx, crackle(.4, 60), 29.33, .6)
for tb in np.arange(29.5, 30.6, .45): add(sfx, clunk(), tb, .35)
add(sfx, swell(.5, 400, 3000), 30.7, .35)
for tb in np.arange(30.9, 31.8, .25): add(sfx, rim(), tb, .4)
add(sfx, pluck_bend(147, .5, 7, .2), 31.82, .7)
# solução
add(sfx, card(.05), 32.74, .5); add(sfx, clunk(), 33.18, .6); add(sfx, card(.05), 33.84, .5)
add(sfx, relay() * 2, 35.24, .9); add(sfx, glass(midi(93), 1.2, .02) * .35, 35.26, .8)
# testa de novo
add(sfx, tink(2000, .4), 36.0, .4); add(sfx, ratchet(.3, 10), 37.0, .4)
for i in range(6): add(sfx, keyclick(.5), 37.0 + i * .06, .35)
add(sfx, relay() * 2, 37.5, .7); add(sfx, subdrop(1.2, 75, 35), 38.76, 1.0); add(sfx, kick(.5, 140, 40, 1.2), 38.76, .9); add(sfx, crackle(.6, 50), 38.9, .4)
# pessoa
for tb in np.arange(40.4, 42.0, .3): add(sfx, rim(), tb, .25)
add(sfx, splat(.5), 42.0, .6); add(sfx, crackle(.8, 40), 42.05, .4); add(sfx, paperflutter(.45), 43.2, .5); add(sfx, waterdrop(400, 1400, .1), 43.65, .7); add(sfx, tink(2600, .4), 43.68, .35)
# chamada final no estilo do vídeo
add(sfx, relay() * 2, 45.45, .8); add(sfx, keyclick(1), 45.45, .5); add(sfx, tink(2400, .4), 45.5, .4)
add(sfx, waterdrop(300, 1000, .12), 45.95, .7); add(sfx, relay() * 2, 46.08, .8); add(sfx, tink(3000, .4), 46.1, .4)
for i in range(4): add(sfx, keyclick(.7), 46.5 + i * .08, .45)
add(sfx, relay() * 2, 47.0, .7); add(sfx, swell(.25, 1500, 7000) * .6, 47.0, .4); add(sfx, waterdrop(500, 1300, .1), 47.05, .5); add(sfx, card(.05), 47.56, .6)
# ralo
add(sfx, swell(1.5, 200, 2500), 49.92, .35)
for i in range(20): add(sfx, keyclick(.3), 49.92 + i * .06, .25)
add(sfx, subdrop(1.0, 80, 25), 51.56, .9); add(sfx, waterdrop(200, 120, .3), 51.7, .6)
add(sfx, lp(noise(.08), 1500) * env(.08, .0005, .02), PURP, .9)
add(sfx, pluck_bend(98, .4, 3, .12), 54.6, .6)
# o elemento vermelho: comprime em bola (squish), voa com uma voltinha e vira a próxima coisa (pop)
HS = [(0, 3.42), (3.86, 4.72), (7.98, 10.18), (10.32, 10.95), (11.64, 12.16), (12.28, 12.46), (12.46, 12.98), (13.22, 15.62), (16.02, 19.32), (19.78, 22.98), (23.94, 25.12), (25.35, 28.12), (28.5, 32.3), (33.3, 35.02), (36.02, 39.92), (40.35, 43.5), (43.62, 44.62), (45.0, 45.78), (45.96, 48.6), (49.02, 52.32)]
for i in range(len(HS) - 1):
    t1, t0n = HS[i][1], HS[i + 1][0]
    if t0n - t1 < .05: continue
    add(sfx, waterdrop(420, 180, .09), t1 - .1, .45)                 # comprime
    add(sfx, pluck_bend(330 + 20 * (i % 5), min(.5, t0n - t1), 7, .12), t1, .3)   # voa
    add(sfx, waterdrop(300, 1500, .08), t0n, .5); add(sfx, tink(2400 + 150 * (i % 4), .2), t0n + .01, .18)  # vira a próxima
# "Claude" vira a logo girando
for tl in (12.2,): add(sfx, swell(.3, 1500, 8000) * .6, tl - .05, .3); add(sfx, glass(midi(90), .9, .01) * .3, tl + .2, .7)
sfx = reverb(sfx, .5, .1)
synth.DROP = 38.76
mix(mus, sfx, voice, 'dNN.wav', duck=.5, music_db=-6, sfx_db=-7, post=1.15, comp=.25, report=False)
