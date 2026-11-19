import synth
from synth import *
import json, subprocess
# DIA 12 — OmniRoute: electro em lá menor a 124 BPM (diferente da house lo-fi dos Dias 9 e 10 e da faixa do Dia 11) + foley sintetizado
synth.BPM = 124; BEAT = 60 / 124; BAR = 4 * BEAT
TEND = 59.9; PURP = 57.78; LOOP = 59.5
mus, sfx = buf(TEND), buf(TEND)
VOZ = 'voz.wav'   # voz do ElevenLabs com a última frase corrigida colada, pausas > 0,3 s encurtadas e atempo 1,03 (60 s)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', VOZ, '-af', 'highpass=f=80,equalizer=f=3500:t=q:w=1:g=1.5,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80',
                      '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; voice = buf(TEND); voice[:min(len(x), len(voice))] = x[:len(voice)]
CH = json.loads(open('d12chunks.js').read().split('=', 1)[1].strip().rstrip(';'))
# Trilha montanha-russa (motor/trilha.py): a energia sobe e desce com o roteiro, cena a cena.
import os, sys; sys.path.insert(0, '../../../motor'); import trilha
ESTILO = os.environ.get('ESTILO', 'electro')     # electro · dnb · futurebass
NARR = trilha.Narr(
    energia=[(0, .88), (3.3, .88), (3.35, 1), (4.05, 1), (4.1, .28), (6.75, .42), (6.8, .55), (10.4, .62), (10.45, .68), (13.6, .74), (13.72, .96),
             (17.4, .92), (17.5, .8), (22.85, .84), (22.92, .42), (24.2, .25), (24.67, .35), (26.7, .6), (26.77, 1), (28.1, 1), (28.18, .48),
             (31.95, .6), (32.05, .78), (37.55, .8), (37.64, .4), (38.58, .3), (40.1, .42), (40.18, .5), (44.2, .86), (44.26, 1), (45.45, .95),
             (45.55, .58), (52.75, .88), (52.85, .15), (54.2, .25), (54.28, 1), (57.78, 1)],
    drops=[6.8, 13.72, 26.77, 54.28],            # vinheta→GitHub, 352 provedores, "o seu trabalho não para", chamada final
    paradas=[(3.2, .15), (24.2, .47)],           # respiro antes do "GIGANTE"; a cota "acaba" e a música para até o "ela pula"
    impactos=[3.35, 20.99, 38.58, 44.26],        # GIGANTE, 1 bilhão, comprime, 9 vezes
    subida_tom=45.55, fim=PURP)
mus = trilha.render(ESTILO, NARR, TEND)
if os.environ.get('MUS_OUT'): np.save(os.environ['MUS_OUT'], mus); raise SystemExit   # só a música, para medir
add(mus, pad([57, 64, 69, 72], LOOP - PURP + .3, 900, .2, .6), PURP + .05, .35)
add(mus, glass(midi(81), 1.4, .02) * .4, PURP + .02, 1); add(mus, glass(midi(88), 1.4, .02) * .4, PURP + .28, 1)
add(mus, kick(.4, 120, 40, 1), LOOP + .2, .6)       # a bola cai na etiqueta e emenda no começo
# ---- foley ----
for c in CH: add(sfx, waterdrop(260, 520, .09) * .8, c['t'] - .04, .28)
for s0 in [4.1, 6.8, 10.45, 13.72, 17.5, 22.92, 28.18, 32.05, 37.64, 40.18, 45.55, 54.28]: add(sfx, clunk(), s0 + .02, .6); add(sfx, ratchet(.3, 9) * .6, s0 + .05, .3)
# gancho: risco, $0 verde (caixa: dinheiro), barra estourando
add(sfx, pencil(.2, 120), 1.61, .6); add(sfx, relay() * 2, 1.8, .8); add(sfx, tink(2600, .5), 1.82, .5); add(sfx, glass(midi(93), .8, .01) * .4, 1.84, .7)
add(sfx, swell(.5, 400, 5000), 2.79, .4); add(sfx, subdrop(.9, 75, 30), 3.35, .9); add(sfx, kick(.4, 140, 40, 1.2), 3.35, .8); add(sfx, crackle(.5, 50), 3.4, .5)
# calendário
for i in range(11): add(sfx, pencil(.06, 90), 4.31 + i * .016, .28)
add(sfx, pencil(.35, 70), 4.49, .5); add(sfx, tink(1800, .9), 6.3, .4)
# GitHub e estrela
add(sfx, paperflutter(.3), 7.21, .5); add(sfx, relay() * 2, 7.87, .7); add(sfx, card(.05), 8.55, .5)
for i in range(9): add(sfx, keyclick(.6), 9.61 + i * .05, .4)
add(sfx, ratchet(1.0, 30) * .5, 10.98, .35)
for i in range(12): add(sfx, tink(2000 + 90 * i, .12), 12.24 + i * .06, .12)
add(sfx, glass(midi(88), 1.0, .01) * .4, 13.04, .8); add(sfx, waterdrop(500, 1500, .1), 13.05, .6)
# 352 provedores
add(sfx, swell(.3, 1500, 8000) * .6, 14.5, .3)
for i in range(26): add(sfx, keyclick(.3), 15.19 + i * .05, .22)
# 90 grátis + 1 bilhão
for i in range(12): add(sfx, waterdrop(500 + 40 * i, 1400, .06), 17.9 + i * .08, .2)
add(sfx, relay() * 2, 18.9, .7); add(sfx, tink(3000, .4), 18.92, .4)
add(sfx, ratchet(.9, 26) * .6, 20.99, .45); add(sfx, glass(midi(93), 1.0, .01) * .35, 21.9, .6)
# cota acaba, pula
add(sfx, swell(.8, 3000, 300) * .5, 23.48, .35); add(sfx, splat(.4), 24.25, .6); add(sfx, pluck_bend(220, .45, 12, .2), 25.01, .7); add(sfx, kick(.3, 160, 60, .5), 25.46, .6); add(sfx, waterdrop(500, 1500, .1), 25.46, .6)
add(sfx, relay() * 2, 27.67, .7)
# computador e cadeado
add(sfx, marble(.8, 24), 28.4, .3)
for i in range(3): add(sfx, card(.05), 30.46 + i * .08, .5)
for i in range(12): add(sfx, keyclick(.4), 31.1 + i * .03, .3)
add(sfx, clunk(), 31.35, .9); add(sfx, relay() * 2, 31.36, .7)
# ferramentas e celular
for tt_ in (32.83, 33.2, 33.56): add(sfx, waterdrop(400, 1200, .1), tt_, .5); add(sfx, tink(2400, .25), tt_ + .01, .25)
for i in range(30): add(sfx, tink(1600 + 30 * i, .1), 34.3 + i * .03, .08)
add(sfx, glass(midi(86), .9, .01) * .35, 36.94, .6)
# prensa
add(sfx, swell(.3, 300, 2000), 37.86, .35); add(sfx, subdrop(.7, 70, 30), 38.6, .8); add(sfx, kick(.35, 120, 40, 1.1), 38.62, .8); add(sfx, crackle(.4, 60), 38.64, .4)
add(sfx, swell(.4, 800, 7000) * .6, 39.64, .35)
# 18 mil -> 2 mil
add(sfx, card(.05), 41.46, .5); add(sfx, ratchet(.5, 16) * .6, 43.01, .45); add(sfx, glass(midi(90), .8, .01) * .35, 43.2, .5); add(sfx, kick(.3, 140, 40, 1), 44.26, .7); add(sfx, relay() * 2, 44.27, .6)
# três comandos
for i, t0 in enumerate([47.5, 48.96, 50.45]):
    for j in range(10): add(sfx, keyclick(.5), t0 + j * .07, .3)
for td in (48.96, 50.45, 52.3): add(sfx, tink(2600, .3), td, .3); add(sfx, waterdrop(500, 1300, .08), td, .4)
# chamada final
add(sfx, relay() * 2, 54.9, .8); add(sfx, keyclick(1), 54.9, .5); add(sfx, tink(2400, .4), 54.95, .4)
add(sfx, waterdrop(300, 1000, .12), 55.47, .7); add(sfx, relay() * 2, 55.6, .8); add(sfx, tink(3000, .4), 55.62, .4)
for i in range(6): add(sfx, keyclick(.7), 56.25 + i * .08, .45)
add(sfx, relay() * 2, 56.75, .7); add(sfx, swell(.25, 1500, 7000) * .6, 56.75, .4); add(sfx, waterdrop(500, 1300, .1), 56.8, .5); add(sfx, card(.05), 57.06, .6)
add(sfx, lp(noise(.08), 1500) * env(.08, .0005, .02), PURP, .9)
add(sfx, pluck_bend(98, .4, 3, .12), LOOP + .2, .6)
# o elemento vermelho: squish, voo, pop (×0,7 em relação ao Dia 10 v3)
HS = [(0, 2.2), (2.42, 3.95), (4.3, 6.48), (7.0, 7.85), (8.75, 10.25), (10.6, 13.55), (13.9, 17.3), (17.6, 19.45), (19.75, 22.8), (23.05, 26.6), (26.8, 28.05), (28.35, 30.25), (30.5, 31.9), (32.7, 36.2), (36.55, 37.55), (37.85, 39.6), (42.4, 44.15), (47.4, 52.3), (52.95, 54.25), (54.42, 55.2), (55.48, 57.7)]
for i in range(len(HS) - 1):
    t1, t0n = HS[i][1], HS[i + 1][0]
    if t0n - t1 < .05: continue
    add(sfx, waterdrop(420, 180, .09), t1 - .1, .45 * .7)
    add(sfx, pluck_bend(330 + 20 * (i % 5), min(.5, t0n - t1), 7, .12), t1, .3 * .7)
    add(sfx, waterdrop(300, 1500, .08), t0n, .5 * .7); add(sfx, tink(2400 + 150 * (i % 4), .2), t0n + .01, .18 * .7)
# "Claude" vira a logo girando
for tl in (0.94, 6.24, 14.48, 50.96, 53.73, 56.29): add(sfx, swell(.3, 1500, 8000) * .6, tl + .05, .3); add(sfx, glass(midi(90), .9, .01) * .3, tl + .3, .6)
sfx = reverb(sfx, .5, .1)
synth.DROP = 54.28
mix(mus, sfx, voice, os.environ.get('SAIDA', 'd12.wav'), duck=.5, music_db=-6, sfx_db=-7, post=1.15, comp=.25, report=False)
print('ok', TEND)
