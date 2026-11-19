import synth
from synth import *
import json, subprocess
# DIA 09 — trilha house lo-fi agitada (a do 07) + foley sintetizado; final roxo do 04
TEND = 55.4; CTA = 50.96
mus, sfx = buf(TEND), buf(TEND)
# voz: mp3 original, limpa e comprimida
VOZ = 'voz.mp3'
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', VOZ, '-af', 'highpass=f=80,afftdn=nf=-25,equalizer=f=3500:t=q:w=1:g=2,equalizer=f=250:t=q:w=1:g=-2,acompressor=threshold=-20dB:ratio=3:attack=5:release=80',
                      '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; voice = buf(TEND); voice[:min(len(x), len(voice))] = x[:len(voice)]
CH = json.loads(open('d9chunks.js').read().split('=',1)[1].strip().rstrip(';'))
SC = [0, 5.14, 7.6, 12.78, 17.38, 21.44, 30.2, 33.4, 37.12, 44.0, 48.4]
FL = [4.10, 5.14, 11.38, 12.30, 15.02, 16.02, 23.68, 24.66, 28.92, 29.90, 38.22, 39.74, 47.5, 48.4, 49.38, 50.16]

def sawbass(n, d=.4, cut=500):
    t = tt(d); f = midi(n); s = 2 * ((f * t) % 1) - 1; return lp((s * np.exp(-t / .22) * np.minimum(1, t / .003)).astype(np.float32), cut)
def rim(): d = .06; t = tt(d); return (bp(noise(d), 1500, 4000) * np.exp(-t / .006) + .5 * np.sin(2 * np.pi * 820 * t) * np.exp(-t / .01)).astype(np.float32)
prog = [[57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 65], [52, 55, 59, 62]]; roots = [45, 41, 43, 40]
nb = int(CTA / 2) + 1
for bar in range(nb):
    t0 = bar * 2.0; ch = prog[bar % 4]; root = roots[bar % 4]
    vin = 5.14 <= t0 + 1 < 7.6               # vinheta "dia 9 de 30": só pad + hat, filtrado
    brk = 44.0 <= t0 < 47.5                  # breakdown antes do drop
    drop = t0 >= 47.5
    cut = 900 if vin else 1300 if t0 < 30 else 2600 if t0 < 44 else 1100 if brk else 4200
    add(mus, pad(ch, 2.0, cut, .02, .25), t0, .55 if not drop else .65)
    for k in range(4):
        tb = t0 + k * BEAT
        if tb >= CTA: break
        add(mus, hat(.05, .02), tb + BEAT / 2, .45)
        if vin: continue
        if not brk or k == 0: add(mus, kick(f0=105, punch=.7), tb, 1)
        if k in (1, 3) and not brk: add(mus, snap(), tb, .5)
    if vin: continue
    for k in range(16):
        if t0 + k * BEAT / 4 < CTA: add(mus, shaker(), t0 + k * BEAT / 4, (.2 if k % 2 else .1) * (1.4 if brk else 1))
    if brk: continue
    for off in [0.75, 1.5, 2.75, 3.5]: add(mus, pad(ch, .22, cut + 800, .005, .1), t0 + off * BEAT, .5)
    for k in (3, 7, 11, 14): add(mus, rim(), t0 + k * BEAT / 4, .35)
    for k, off in enumerate([0, .75, 1.5, 2.5, 3.25]):
        if t0 + off * BEAT < CTA: add(mus, sawbass(root + (12 if k == 3 else 0), cut=450 if t0 < 30 else 900), t0 + off * BEAT, .8)
# sobe no breakdown
L_ = 47.5 - 45.0; tone = np.sin(2 * np.pi * np.cumsum(660 * 2 ** (tt(L_) * 1.0 / 12 * 4)) / SR).astype(np.float32) * np.minimum(1, tt(L_) / 1.2) * .2
add(mus, tone, 45.0, .6); add(mus, swell(1.2, 300, 7000), 46.3, .5)
mus = reverb(mus, 1.1, .14)
i0 = int(CTA * SR); mus[i0:] = 0
# cama suave no roxo + notas de vidro em cada palavra do final
add(mus, pad([57, 64, 69, 72], TEND - CTA, 900, .3, 1.2), CTA + .05, .35)
add(mus, glass(midi(81), 1.6, .02) * .4, CTA + .02, 1)
add(mus, glass(midi(84), 1.2, .02) * .3, 51.6, 1)          # ✓ seguir
add(mus, glass(midi(88), 1.4, .02) * .35, 52.26, 1)        # comenta
add(mus, glass(midi(93), 1.6, .02) * .35, 52.64, 1)        # professor
add(mus, glass(midi(86), 1.4, .02) * .25, 53.9, 1)         # guia completo
# ---- foley ----
for c in CH: add(sfx, waterdrop(260, 520, .09) * .8, c['t'] - .04, .35)                 # slime entre palavras
for s0 in SC: add(sfx, clunk(), s0 + .02, .8); add(sfx, ratchet(.3, 9) * .6, s0 + .04, .4)  # a linha constrói
for f in FL: add(sfx, subdrop(.7, 70, 34), f, .55); add(sfx, kick(.3, 130, 45, .8), f, .4)  # viradas de cor
for i, tx in enumerate([.75, 1.1, 1.4, 1.7, 2.0]): add(sfx, relay() * 2, tx, .7)            # X no gabarito
for i in range(4): add(sfx, tink(1800 + 300 * i, .25), 3.7 + i * .12, .3)                    # nota máxima
for i in range(6): add(sfx, card(.03), 5.3 + i * .09, .45)                                   # calendário
for i in range(14): add(sfx, keyclick(.6), 7.8 + i * .08, .45)                               # digita o repo
t = 10.38
while t < 11.38: add(sfx, tink(2600, .12), t, .15); t += .06 + .1 * ((t - 10.38))           # estrelas contando
add(sfx, tink(3100, .7), 11.38, .5); add(sfx, crackle(.6, 40), 11.4, .4)
add(sfx, marble(.8, 22), 13.0, .4)                                                           # chapéu cai
for tx in (18.0, 19.2, 20.4): add(sfx, relay() * 2, tx, .7); add(sfx, tink(2400, .2), tx + .01, .2)  # testes
for tx in (22.2, 23.0, 23.8): add(sfx, pluck_bend(220, .4, 3, .1), tx, .6)                   # nós do mapa
for tb in (24.9, 25.3, 25.7, 29.5, 29.9): add(sfx, pluck_bend(98, .5, 3, .12), tb, .9); add(sfx, kick(.3, 90, 45, .3), tb, .5)  # quiques
add(sfx, relay() * 2, 27.4, .8); add(sfx, relay() * 2, 28.9, .8)                              # previsão A/B
add(sfx, paperflutter(.5), 30.2, .7); add(sfx, pencil(.6), 32.7, .5)                         # prova em pdf
for i in range(3): add(sfx, card(.04), 33.5 + i * .25, .6)                                    # exercícios
for i in range(8): add(sfx, waterdrop(500 + 90 * i, 1400, .08), 37.3 + i * .14, .3)           # grafo
add(sfx, ratchet(.5, 14) * .6, 40.0, .4)
for i in range(4): add(sfx, relay() * 2, 44.4 + i * .2, .6)                                   # gabarito 2
add(sfx, splat(.4), 46.6, .5)                                                                 # manda pra ela
add(sfx, subdrop(1.4, 75, 35), 47.5, 1.0); add(sfx, kick(.5, 140, 40, 1.2), 47.5, .9)         # drop
for i in range(14): add(sfx, card(.03), 48.4 + i * .05, .4)                                   # parede
add(sfx, lp(noise(.08), 1500) * env(.08, .0005, .02), CTA, .9)                                # clique do corte
add(sfx, relay() * 2, 51.6, .6); add(sfx, waterdrop(400, 1200, .1), 52.0, .6); add(sfx, card(.05), 53.9, .5)
sfx = reverb(sfx, .5, .1)
synth.DROP = 47.5
mix(mus, sfx, voice, 'd9.wav', duck=.5, music_db=-6, sfx_db=-7, post=1.3, comp=.25, report=False)
