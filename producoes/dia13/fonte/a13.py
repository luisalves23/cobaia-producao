# DIA 13 v2 — áudio: drum and bass solar (musica13.py) + foley sintetizado + voz do ElevenLabs como chegou
import subprocess, json, numpy as np, synth
from synth import *
from musica13 import music
TEND = 55.4; PURP = 53.35; LOOP = 55.05
synth.END = TEND; synth.DROP = 999
VOZ = 'voz.mp3'   # ElevenLabs v3, versão enérgica (−17,5 LUFS, 53,47 s)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', VOZ, '-af', 'highpass=f=80,equalizer=f=3500:t=q:w=1:g=1.5,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80',
                      '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; voice = buf(TEND); voice[:min(len(x), len(voice))] = x[:len(voice)]
mus = music(TEND); sfx = buf(TEND)
CH = json.loads(open('d13chunks.js').read().split('=', 1)[1].strip().rstrip(';'))
for c in CH: add(sfx, waterdrop(260, 520, .09) * .8, c['t'] - .04, .2)
def thud(g=1.0): return (kick(.3, 90, 38, .4) + splat(.3) * .5) * g
# gancho: arquivo, digitação, envio, Claude, transformação, detector (igual à prévia aprovada)
add(sfx, thud(1.2), 0, 1); add(sfx, paperflutter(.35), 0, .3)
add(sfx, paperflutter(.25), .41, .35); add(sfx, clunk(), .62, .6); add(sfx, card(), .62, .5)
for k in range(19): add(sfx, keyclick(.6), .64 + k * .047, .35)
add(sfx, waterdrop(700, 1500), 1.75, .6); add(sfx, tink(midi(88)), 2.03, .25)
add(sfx, glass(midi(76), .6), 2.15, .18); add(sfx, card(), 2.28, .4); add(sfx, paperflutter(.2), 2.3, .25)
add(sfx, thud(1.4), 2.455, 1); add(sfx, glass(midi(83), .9), 2.47, .25); add(sfx, pencil(.4), 2.52, .3)
add(sfx, swell(.5, 400, 4000), 3.45, .18); add(sfx, waterdrop(500, 1300), 3.97, .6)
for t0, g in ((3.98, .7), (4.66, .5), (4.78, .5)): add(sfx, clunk(), t0, g)
for k in range(4): add(sfx, card(), 4.16 + k * .2, .25)
add(sfx, swell(.55, 1500, 9000), 5.08, .2); add(sfx, tink(midi(84)), 5.76, .35); add(sfx, tink(midi(91)), 5.86, .3)
# cortes de câmera
for s0 in [6.32, 9.16, 12.15, 17.03, 22.6, 24.75, 29.35, 34.09, 40.11, 43.06, 45.77, 49.22, 50.55]: add(sfx, swell(.22, 2500, 9000) * .5, s0 - .1, .22); add(sfx, card(), s0 + .02, .35)
# calendário (vinheta padrão): risquinhos nos dias feitos, círculo no 13, logo do Claude
for i in range(12): add(sfx, pencil(.06, 90), 6.44 + i * .016, .28)
add(sfx, pencil(.35, 70), 6.63, .5); add(sfx, glass(midi(88), .9, .01) * .3, 8.7, .5)
# lupa e aprovado
add(sfx, swell(1.1, 800, 3000) * .5, 9.22, .2); add(sfx, thud(1.2), 10.46, .8); add(sfx, glass(midi(86), 1.0), 10.5, .3)
# pedido
add(sfx, thud(.8), 12.2, .6)
for w0, w1 in [(13.73, 14.3), (14.38, 14.9), (14.92, 15.75), (15.81, 16.5), (16.55, 16.6)]:
    n = int((w1 - w0) / .05)
    for k in range(n): add(sfx, keyclick(.5), w0 + k * .05, .25)
add(sfx, waterdrop(700, 1500), 16.62, .6); add(sfx, tink(midi(93)), 16.8, .3)
# pesquisa profunda
add(sfx, thud(.8), 17.08, .6); add(sfx, swell(2.0, 4000, 300) * .6, 17.8, .3); add(sfx, subdrop(1.0, 60, 26), 19.35, .6)
add(sfx, ratchet(.3, 10), 19.92, .45); add(sfx, ratchet(.45, 14), 20.2, .45)
for k in range(5): add(sfx, card(), 20.55 + k * .05, .4); add(sfx, tink(1800 + 220 * k, .15), 21.0 + k * .08, .2)
# fragmentadora
add(sfx, relay() * 2, 22.82, .6); add(sfx, lp(noise(1.6), 900) * .5, 22.85, .4)
for t0 in [22.86, 23.22, 23.5, 23.76, 23.92]: add(sfx, crackle(.35, 120), t0 + .25, .6)
# placas
for i in range(3): add(sfx, clunk(), 25.05 + i * .12, .55)
for ts in (26.6, 27.6, 28.6): add(sfx, thud(.7), ts, .6); add(sfx, card(), ts, .5)
# truque
for k in range(6): add(sfx, card(), 29.38 + k * .09, .4)
add(sfx, paperflutter(.2), 29.94, .5); add(sfx, glass(midi(88), .8), 30.0, .3)
add(sfx, keyclick(1.4), 31.95, .8); add(sfx, card(), 32.4, .4); add(sfx, relay() * 2, 33.42, .6)
# Anti-Robô nasce
add(sfx, pencil(1.2, 70), 34.66, .35); add(sfx, pencil(.5, 90), 36.02, .3); add(sfx, thud(.9), 36.89, .7)
for k in range(5): add(sfx, waterdrop(500 + 90 * k, 1300, .06), 37.55 + k * .1 + .3, .3)
add(sfx, ratchet(.62, 24), 38.94, .5)
# caixa, laço, instalação
add(sfx, paperflutter(.4), 40.3, .4); add(sfx, glass(midi(81), .6), 40.62, .2); add(sfx, tink(2600, .3), 41.42, .35)
add(sfx, swell(.25, 4000, 600), 42.44, .3); add(sfx, thud(1.0), 42.69, .7); add(sfx, ratchet(.4, 16), 42.6, .3); add(sfx, glass(midi(93), .8), 42.98, .3)
# /anti-robô
add(sfx, keyclick(1), 44.6, .6)
for k in range(9): add(sfx, keyclick(.6), 44.94 + k * .06, .33)
# o texto volta, aprovado, toda vez
add(sfx, swell(.5, 600, 5000), 45.8, .3); add(sfx, pencil(.5, 80), 46.13, .3); add(sfx, swell(.7, 800, 3000) * .5, 46.2, .2)
add(sfx, thud(1.2), 46.95, .8); add(sfx, glass(midi(86), 1.0), 47.0, .3)
for i, tv in enumerate([48.4, 48.62, 48.84]): add(sfx, tink(midi(84 + 3 * i)), tv, .35)
# guia
add(sfx, paperflutter(.3), 49.3, .4)
for f in (49.69, 49.96, 50.12): add(sfx, paperflutter(.15), f, .4)
# chamada final
add(sfx, relay() * 2, 51.09, .8); add(sfx, tink(2400, .4), 51.12, .4); add(sfx, waterdrop(400, 900), 51.68, .6)
for i in range(6): add(sfx, keyclick(.7), 52.28 + i * .06, .45)
add(sfx, relay() * 2, 52.8, .7); add(sfx, card(), 52.95, .6)
add(sfx, lp(noise(.08), 1500) * env(.08, .0005, .02), PURP, .9); add(sfx, pluck_bend(98, .4, 3, .12), LOOP + .1, .5)
# o elemento vermelho: squish, voo e pop (×0,7)
HS = [(5.96, 6.36), (6.45, 8.95), (9.22, 10.42), (10.6, 12.0), (12.2, 12.8), (13.0, 16.78), (17.08, 17.7), (17.9, 19.85), (19.92, 22.45), (22.66, 24.6), (26.6, 27.28), (27.6, 28.28), (28.6, 29.2), (30.08, 30.42), (30.7, 32.3), (32.42, 34.0), (34.66, 36.0), (36.1, 38.35), (38.7, 39.95), (40.2, 41.3), (41.42, 43.0), (43.25, 44.05), (44.62, 45.72), (46.2, 46.92), (47.05, 48.25), (48.32, 49.15), (49.35, 50.45), (50.62, 51.42), (51.66, 51.98), (52.12, 53.0), (53.1, 53.32)]
for i in range(len(HS) - 1):
    t1, t0n = HS[i][1], HS[i + 1][0]
    if t0n - t1 < .05: continue
    add(sfx, waterdrop(420, 180, .09), t1 - .1, .45 * .7); add(sfx, pluck_bend(294 + 22 * (i % 5), min(.5, t0n - t1), 7, .12), t1, .3 * .7)
    add(sfx, waterdrop(300, 1500, .08), t0n, .5 * .7)
for tl in (2.15, 8.56, 13.31, 40.38): add(sfx, swell(.3, 1500, 8000) * .6, tl + .05, .3); add(sfx, glass(midi(86), .9, .01) * .3, tl + .3, .5)
sfx = reverb(sfx, .5, .1)
f = int(.03 * SR); mus[-f:] *= np.linspace(1, 0, f)
mix(mus, sfx, voice, 'd13.wav', duck=.45, music_db=-7, sfx_db=-6, post=1.0, comp=.3, report=False)
print('ok', TEND)
