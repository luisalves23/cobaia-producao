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
def sqbass(n, d=.3, cut=700):
    t = tt(d); f = midi(n); s = np.sign(np.sin(2 * np.pi * f * t)) * .6 + .4 * np.sin(2 * np.pi * f / 2 * t); return lp((s * np.exp(-t / .16) * np.minimum(1, t / .003)).astype(np.float32), cut)
def rim(): d = .06; t = tt(d); return (bp(noise(d), 1500, 4000) * np.exp(-t / .006) + .5 * np.sin(2 * np.pi * 820 * t) * np.exp(-t / .01)).astype(np.float32)
# Am F C G (mais aceso que o Dia 10)
prog = [[69, 72, 76, 79], [65, 69, 72, 76], [64, 67, 72, 76], [62, 67, 71, 74]]; roots = [33, 29, 36, 31]
def sec(t):
    if t < 4.1: return 'drop'
    if t < 6.8: return 'vin'
    if t < 22.9: return 'groove'
    if t < 26.7: return 'dark'
    if t < 37.6: return 'groove2'
    if t < 45.5: return 'mid'
    if t < 52.8: return 'build'
    if t < 54.2: return 'pause'
    return 'big'
# ---- versão suave (regra de 19/11): a mesma base do Dia 12 inteira, camadas e filtro mudando
# em rampas curtas (0,3 s) que terminam no corte de cada cena; sem degrau, sem troca de música.
nb = int(PURP / BAR) + 1
L = {k: buf(TEND) for k in ('pad', 'drum', 'k1', 'shk', 'bass', 'plk', 'kal')}
for bar in range(nb):
    t0 = bar * BAR; ch = prog[bar % 4]; root = roots[bar % 4]
    add(L['pad'], pad(ch, BAR, 6000, .02, .25), t0, .5)
    for k in range(4):
        tb = t0 + k * BEAT
        if tb >= PURP: break
        add(L['drum'], kick(f0=115, punch=.8), tb, 1); add(L['drum'], hat(.05, .02), tb + BEAT / 2, .5)
        if k in (1, 3): add(L['drum'], snap(), tb, .55)
        if k == 0: add(L['k1'], kick(f0=115, punch=.8), tb, 1)
    for k in range(16):
        tb = t0 + k * BEAT / 4
        if tb < PURP: add(L['shk'], shaker(), tb, .18 if k % 2 else .08)
    for k, off in enumerate([0, .5, 1.5, 2, 3, 3.5]):
        if t0 + off * BEAT < PURP: add(L['bass'], sqbass(root + (12 if k in (2, 5) else 0), cut=900), t0 + off * BEAT, .7)
    for k in range(8): add(L['plk'], pluck_bend(midi(ch[(k * 3) % 4] + 12), .3, 0, .12), t0 + k * BEAT / 2, .22)
    for k in range(8): add(L['kal'], kalimba(midi(ch[k % 4] + 12), .4) * .5, t0 + k * BEAT / 2, .3)
# estado de cada cena: camadas (0 a 1), ganho geral em dB e filtro (Hz). '~' = sobe aos poucos até a próxima cena (build).
ST = [  # t,   drum k1  shk bass plk kal   dB    filtro
    (0,     1,  0,  1,  1,   1,  0,    0,   4000),
    (4.1,   0,  0,  0,  0,   0, .5,   -6,   1100),   # vinheta: respira
    (6.8,   1,  0, .6,  1,   0,  0,   -3,   2000),   # GitHub
    (10.45, 1,  0,  1,  1,  .5,  0,   -2,   2600),   # estrela
    (13.72, 1,  0,  1,  1,   1,  0,    0,   4200),   # 352 provedores: cheio
    (17.5,  1,  0,  1,  1,  .6,  0,   -1,   3200),   # grátis / 1 bilhão
    (22.92, 0,  1,  0, .5,   0,  0,   -5,   1000),   # a cota acabando: só um bumbo por compasso
    (24.2,  0,  0,  0,  0,   0,  0,  -40,   1000),   # "acaba": a música some (fade curto)
    (24.67, 0,  0,  0,  0,   0, .4,  -12,    900),   # "ela pula": volta baixinho e cresce até o drop (riser)
    (26.77, 1,  0,  1,  1,   1,  0,    0,   4200),   # "o seu trabalho não para": drop
    (28.18, 1,  0, .5,  1,   0,  0,   -3,   2200),   # no seu computador
    (32.05, 1,  0,  1,  1,  .7,  0,   -1.5, 3200),   # ferramentas
    (37.64, 0,  1,  0,  1,   0,  0,   -4,   1200),   # prensa: aperta
    (40.18, 1,  0,  1,  1,   0, .5,   -3,   1800),   # teste: build até o 9 vezes
    (44.26, 1,  0,  1,  1,   1,  0,    0,   3800),   # 9 vezes
    (45.55, 1,  0,  1,  1,   0,  1,   -2,   2200),   # três comandos: build
    (52.85, 0,  0,  0,  0,   0,  0,   -7,    900),   # "quer saber mais": vale + riser
    (54.28, 1,  0,  1,  1,   1,  0,   1.5,  4800),   # chamada final: o mais cheio
]
BUILD = {40.18: 44.26, 45.55: 52.85, 24.67: 26.77}   # trechos que crescem aos poucos (filtro e volume)
RAMP = .3
def curve(col, t_arr):
    v = np.zeros_like(t_arr)
    for i, row in enumerate(ST):
        c = row[0]; val = row[col]
        if i == 0: v[:] = val; continue
        prev = ST[i - 1]
        r = np.clip((t_arr - (c - RAMP)) / RAMP, 0, 1) if c not in (24.2,) else np.clip((t_arr - (c - .12)) / .12, 0, 1)
        if prev[0] in BUILD and col in (7, 8):   # build: sobe devagar desde o começo da cena anterior
            b0 = prev[0]; tgt = val
            rb = np.clip((t_arr - b0) / (c - RAMP - b0), 0, 1) ** 1.5
            v = np.where((t_arr >= b0) & (t_arr < c - RAMP), prev[col] + (tgt - prev[col]) * .75 * rb, v)
            base = prev[col] + (tgt - prev[col]) * .75
            v = np.where(t_arr >= c - RAMP, base + (val - base) * r, v); continue
        v = v * (1 - r) + val * r if True else v
    return v
tg = np.arange(0, TEND, .005)
G = {k: np.interp(np.arange(len(mus)) / SR, tg, curve(i + 1, tg)).astype(np.float32) for i, k in enumerate(['drum', 'k1', 'shk', 'bass', 'plk', 'kal'])}
gdb = np.interp(np.arange(len(mus)) / SR, tg, curve(7, tg)); cut = np.interp(np.arange(len(mus)) / SR, tg, curve(8, tg))
inner = L['drum'] * G['drum'] + L['k1'] * G['k1'] + L['shk'] * G['shk'] + L['bass'] * G['bass'] + L['plk'] * G['plk'] + L['kal'] * G['kal']
padf = np.zeros_like(L['pad']); zi = None; Bk = 480
from scipy.signal import butter, sosfilt, sosfilt_zi
for i in range(0, len(padf), Bk):
    sos = butter(2, float(cut[i]), 'lowpass', fs=SR, output='sos'); zi = sosfilt_zi(sos) * 0 if zi is None else zi
    padf[i:i + Bk], zi = sosfilt(sos, L['pad'][i:i + Bk], zi=zi)
mus += ((padf * .9 + inner) * 10 ** (gdb / 20)).astype(np.float32)
add(mus, swell(2.0, 300, 7000), 26.77 - 2.0, .45)   # "ela pula" → drop
add(mus, swell(1.4, 300, 7000), 54.28 - 1.4, .5)    # riser até a chamada
add(mus, swell(1.2, 300, 6000), 13.72 - 1.2, .3)    # sobe para os 352
mus = reverb(mus, 1.0, .14)
i1 = int(PURP * SR) - int(.5 * SR); i2 = int(PURP * SR); mus[i1:i2] = tapestop(mus[i1:i2].copy(), .5); mus[i2:] = 0
add(mus, pad([57, 64, 69, 72], LOOP - PURP + .3, 900, .2, .6), PURP + .05, .35)
add(mus, glass(midi(81), 1.4, .02) * .4, PURP + .02, 1); add(mus, glass(midi(88), 1.4, .02) * .4, PURP + .28, 1)
add(mus, kick(.4, 120, 40, 1), LOOP + .2, .6)       # a bola cai na etiqueta e emenda no começo
# ---- foley ----
for c in CH: add(sfx, waterdrop(260, 520, .09) * .8, c['t'] - .04, .28)
for s0 in [4.1, 6.8, 10.45, 13.72, 17.5, 22.92, 28.18, 32.05, 37.64, 40.18, 45.55, 54.28]: add(sfx, clunk(), s0 + .02, .6); add(sfx, ratchet(.3, 9) * .6, s0 + .05, .3)
# gancho v2: correntes chacoalhando, corte que estoura as correntes, cadeado abre e cai, $0 verde carimbado
add(sfx, kick(.35, 150, 45, 1.1), 0.0, .7)                      # soco de zoom no frame 0
for tc in (0.05, 0.67, 1.29): add(sfx, ratchet(.25, 8) * .6, tc, .3)  # correntes tremendo
add(sfx, swell(.14, 800, 9000), 1.47, .45)                       # o corte vermelho
add(sfx, crackle(.45, 90), 1.61, .7); add(sfx, ratchet(.5, 22) * .8, 1.62, .55); add(sfx, clunk(), 1.62, .9)   # elos estourando, cadeado abrindo
add(sfx, relay() * 2, 1.68, .8); add(sfx, subdrop(.7, 70, 30), 1.68, .6); add(sfx, tink(2600, .5), 1.7, .45); add(sfx, glass(midi(93), .8, .01) * .4, 1.72, .6)  # $0 carimbado
add(sfx, clunk(), 1.98, .35)                                     # cadeado caindo
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
HS = [(0, 1.42), (1.5, 1.95), (2.42, 3.95), (4.3, 6.48), (7.0, 7.85), (8.75, 10.25), (10.6, 13.55), (13.9, 17.3), (17.6, 19.45), (19.75, 22.8), (23.05, 26.6), (26.8, 28.05), (28.35, 30.25), (30.5, 31.9), (32.7, 36.2), (36.55, 37.55), (37.85, 39.6), (42.4, 44.15), (47.4, 52.3), (52.95, 54.25), (54.42, 55.2), (55.48, 57.7)]
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
mix(mus, sfx, voice, 'd12.wav', duck=.5, music_db=-6, sfx_db=-7, post=1.0, comp=.25, report=False)
print('ok', TEND)
