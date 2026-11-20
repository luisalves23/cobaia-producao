import synth
from synth import *
import json, subprocess
# DIA 13 — Anti-Robô: future bass solar em fá maior a 128 BPM (Dia 10 house lo-fi em ré menor, Dia 11 faixa do Luis, Dia 12 electro em lá menor)
# Pedido do Luis: a trilha avança junto com o texto, sempre para cima e positiva; quando desce, desce pouco e volta de forma suave e orgânica.
# Uma base só (acordes em serra com "respiração" de sidechain, a palavra do vídeo é orgânico), camadas entrando e saindo em rampa.
synth.BPM = 128; BEAT = 60 / 128; BAR = 4 * BEAT
TEND = 59.05; PURP = 56.95; LOOP = 58.65
mus, sfx = buf(TEND), buf(TEND)
VOZ = 'voz.mp3'   # ElevenLabs, como chegou (−16,7 LUFS, pico −0,9 dBTP, 56,76 s)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', VOZ, '-af', 'highpass=f=80,equalizer=f=3500:t=q:w=1:g=1.5,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80',
                      '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768; voice = buf(TEND); voice[:min(len(x), len(voice))] = x[:len(voice)]
CH = json.loads(open('d13chunks.js').read().split('=', 1)[1].strip().rstrip(';'))
def subbass(n, d):
    t = tt(d); f = midi(n); s = np.sin(2 * np.pi * f * t) + .25 * np.sin(4 * np.pi * f * t); return (s * np.minimum(1, t / .004) * np.minimum(1, np.maximum(0, d - t) / .03) * .8).astype(np.float32)
# F C Dm Bb (I V vi IV): luminoso, nunca triste
prog = [[65, 69, 72, 77], [64, 67, 72, 76], [62, 65, 69, 74], [62, 65, 70, 74]]; roots = [41, 36, 38, 34]
nb = int(PURP / BAR) + 1
L = {k: buf(TEND) for k in ('pad', 'drum', 'k1', 'shk', 'bass', 'plk', 'kal')}
for bar in range(nb):
    t0 = bar * BAR; ch = prog[bar % 4]; root = roots[bar % 4]
    add(L['pad'], supersaw(ch, BAR + .05, 7000, .01, .06), t0, .9)
    for k in range(4):
        tb = t0 + k * BEAT
        if tb >= PURP: break
        add(L['drum'], kick(f0=120, punch=.9), tb, 1); add(L['drum'], hat(.05, .02), tb + BEAT / 2, .55)
        if k in (1, 3): add(L['drum'], snap(), tb, .6)
        if k in (0, 2) and k == 0: add(L['k1'], kick(f0=120, punch=.9), tb, 1)
        if k == 2: add(L['k1'], snap(), tb, .5)
    for k in range(16):
        tb = t0 + k * BEAT / 4
        if tb < PURP: add(L['shk'], shaker(), tb, .18 if k % 2 else .08)
    for k in range(4):
        if t0 + k * BEAT < PURP: add(L['bass'], subbass(root + 12 * (k == 3), BEAT * .9), t0 + k * BEAT + (BEAT * .5 if k else 0) * 0, .75)
    arp = [0, 2, 1, 3, 2, 1, 3, 2]
    for k in range(8): add(L['plk'], pluck_bend(midi(ch[arp[k]] + 12), .3, 0, .12), t0 + k * BEAT / 2, .22)
    for k in (0, 3, 6, 10, 13): add(L['kal'], kalimba(midi(ch[k % 4] + 24), .5) * .5, t0 + k * BEAT / 4, .28)
# "respiração" do acorde: o volume afunda em cada bumbo e volta (sidechain), só quando a batida está tocando
tgrid = np.arange(len(mus)) / SR
pump_shape = 1 - .6 * np.exp(-((tgrid % BEAT) / .11))
ST = [  # t,   drum k1  shk bass plk kal   dB    filtro
    (0,     1,  0,  1,  1,   1,  0,    0,   5200),   # gancho: cheio e claro
    (2.42,  1,  0,  1,  1,   1,  1,    1,   7000),   # "humanizar": abre e brilha
    (4.45,  1,  0, .6,  1,  .6,  0,   -1,   4200),   # detector
    (6.1,   0,  0, .5, .6,   1, .6,   -3,   3200),   # vinheta: sem bumbo, ainda claro
    (9.25,  0,  1, .6,  1,  .6,  0,   -2,   3000),   # "eu testei": meio-tempo crescendo até o zero
    (10.53, 1,  0,  1,  1,   1,  1,    1,   7000),   # "zero por cento": drop
    (12.3,  1,  0,  1,  1,  .5,  0,   -1,   4200),   # primeiro
    (17.55, 1,  0, .6,  1,   0,  1,  -1.5,  3400),   # depois: kalimba
    (19.67, 1,  0, .4,  1,   0,  1,  -2.5,  2400),   # "profunda": mergulho leve
    (21.39, 1,  0,  1,  1,   1,  0,    0,   4800),   # padrões: volta a subir
    (23.7,  0,  1, .5,  1,  .6,  0,  -2.5,  2800),   # nunca repetir: meio-tempo
    (25.9,  1,  0,  1,  1,  .6,  0,   -1,   4000),   # sinais óbvios
    (29.9,  1,  0,  1,  1,  .6, .5,  -1.5,  3200),   # cresce até o truque
    (31.53, 1,  0,  1,  1,   1,  1,   1.5,  7500),   # "o truque": drop
    (36.0,  1,  0, .6,  1,  .5,  0,  -1.5,  3800),   # pede
    (39.05, 1,  0,  1,  1,   1,  0,    0,   5200),   # Anti-Robô
    (40.9,  1,  0,  1,  1,  .6, .5,  -.5,   4600),
    (42.6,  1,  0,  1,  1,   1,  1,    1,   6800),   # o Claude cria a sua skill
    (46.2,  0,  1, .5,  1,  .5,  1,   -3,   2600),   # antes de escrever: cresce até o zero
    (50.34, 1,  0,  1,  1,   1,  1,   1.5,  7500),   # "zero por cento" de novo: drop
    (52.8,  0,  0, .6, .6,   1, .6,   -3,   3000),   # quer o guia: respiro curto e sobe
    (54.15, 1,  0,  1,  1,   1,  1,    2,   8000),   # chamada final: o mais cheio
]
BUILD = {9.25: 10.53, 29.9: 31.53, 46.2: 50.34, 52.8: 54.15}
RAMP = .3
def curve(col, t_arr):
    v = np.zeros_like(t_arr)
    for i, row in enumerate(ST):
        c = row[0]; val = row[col]
        if i == 0: v[:] = val; continue
        prev = ST[i - 1]
        r = np.clip((t_arr - (c - RAMP)) / RAMP, 0, 1)
        if prev[0] in BUILD and col in (7, 8):
            b0 = prev[0]; rb = np.clip((t_arr - b0) / (c - RAMP - b0), 0, 1) ** 1.5
            v = np.where((t_arr >= b0) & (t_arr < c - RAMP), prev[col] + (val - prev[col]) * .75 * rb, v)
            base = prev[col] + (val - prev[col]) * .75
            v = np.where(t_arr >= c - RAMP, base + (val - base) * r, v); continue
        v = v * (1 - r) + val * r
    return v
tg = np.arange(0, TEND, .005)
G = {k: np.interp(tgrid, tg, curve(i + 1, tg)).astype(np.float32) for i, k in enumerate(['drum', 'k1', 'shk', 'bass', 'plk', 'kal'])}
gdb = np.interp(tgrid, tg, curve(7, tg)); cut = np.interp(tgrid, tg, curve(8, tg))
pump = 1 - (1 - pump_shape) * np.clip(G['drum'] + .6 * G['k1'], 0, 1)
inner = L['drum'] * G['drum'] + L['k1'] * G['k1'] + L['shk'] * G['shk'] + L['bass'] * G['bass'] * pump + L['plk'] * G['plk'] + L['kal'] * G['kal']
padf = np.zeros_like(L['pad']); zi = None; Bk = 480
from scipy.signal import butter, sosfilt, sosfilt_zi
for i in range(0, len(padf), Bk):
    sos = butter(2, float(cut[i]), 'lowpass', fs=SR, output='sos'); zi = sosfilt_zi(sos) * 0 if zi is None else zi
    padf[i:i + Bk], zi = sosfilt(sos, L['pad'][i:i + Bk], zi=zi)
mus += ((padf * pump * 1.1 + inner) * 10 ** (gdb / 20)).astype(np.float32)
for tb, d, g in ((2.42, .5, .3), (10.53, 1.1, .45), (31.53, 1.4, .45), (50.34, 1.8, .45), (54.15, 1.3, .5)): add(mus, swell(d, 300, 7500), tb - d, g)
for tb in (2.42, 10.53, 31.53, 50.34, 54.15): add(mus, subdrop(.9, 72, 30), tb, .5)
mus = reverb(mus, 1.1, .16)
i1 = int(PURP * SR) - int(.45 * SR); i2 = int(PURP * SR); mus[i1:i2] = tapestop(mus[i1:i2].copy(), .45); mus[i2:] = 0
add(mus, pad([65, 69, 72, 77], LOOP - PURP + .35, 1400, .15, .5), PURP + .04, .35)
add(mus, glass(midi(84), 1.4, .02) * .4, PURP + .02, 1); add(mus, glass(midi(89), 1.4, .02) * .4, PURP + .28, 1)
add(mus, kick(.4, 120, 40, 1), LOOP + .22, .6)
# ---- foley ----
for c in CH: add(sfx, waterdrop(260, 520, .09) * .8, c['t'] - .04, .26)
for s0 in [4.45, 6.1, 9.25, 12.3, 17.55, 23.7, 25.9, 31.0, 36.0, 42.6, 46.2, 49.15, 52.8, 54.15]: add(sfx, clunk(), s0 + .02, .55); add(sfx, ratchet(.3, 9) * .6, s0 + .05, .28)
# gancho: robô ligando (relé + bipes mecânicos), impressora de texto, pedido enviado, derretimento orgânico
add(sfx, kick(.35, 150, 45, 1.1), 0.0, .7); add(sfx, relay() * 2, 0.02, .6)
for i in range(14): add(sfx, keyclick(.35), 0.1 + i * .065, .22)              # a fita de texto de robô saindo
add(sfx, ratchet(.2, 6) * .7, .41, .4); add(sfx, tink(1200, .2), .42, .3)
for i in range(4): add(sfx, keyclick(.6), 1.05 + i * .17, .35)                 # você digita o pedido
add(sfx, relay() * 2, 1.9, .6); add(sfx, swell(.3, 1500, 7000) * .6, 1.95, .35)  # enviar, o pedido sobe
add(sfx, splat(.4), 2.42, .55); add(sfx, glass(midi(89), 1.2, .01) * .45, 2.45, .7); add(sfx, waterdrop(300, 1200, .14), 2.44, .7)  # robô vira humano
add(sfx, paperflutter(.3), 3.19, .45); add(sfx, pencil(.5, 70), 3.25, .35)
# detector
add(sfx, swell(.8, 2000, 9000) * .4, 4.7, .3); add(sfx, tink(2600, .2), 5.3, .3); add(sfx, tink(2000, .2), 5.45, .3)
# calendário
for i in range(12): add(sfx, pencil(.06, 90), 6.29 + i * .016, .28)
add(sfx, pencil(.35, 70), 6.48, .5); add(sfx, glass(midi(88), .9, .01) * .3, 8.65, .5)
# medidor: sobe a 100, despenca a 0 verde
add(sfx, ratchet(.55, 14) * .6, 9.4, .4); add(sfx, ratchet(.7, 22) * .6, 10.53, .45); add(sfx, relay() * 2, 11.22, .7); add(sfx, tink(3000, .4), 11.24, .45); add(sfx, glass(midi(93), 1.0, .01) * .35, 11.62, .6)
# primeiro: o pedido
for b in [14.08, 14.76, 14.96, 15.32, 15.68, 15.88, 16.25, 16.45, 16.66]:
    for j in range(3): add(sfx, keyclick(.5), b + j * .06, .28)
add(sfx, card(.05), 17.02, .5); add(sfx, swell(.25, 1500, 7000) * .5, 17.3, .3)
# pesquisa profunda e padrões
add(sfx, swell(1.0, 4000, 400) * .5, 19.67, .35); add(sfx, subdrop(.7, 60, 30), 20.3, .4)
for i in range(5): add(sfx, card(.05), 21.3 + i * .12, .5); add(sfx, tink(1800 + 200 * i, .15), 21.31 + i * .12, .18)
# nunca repetir: um X por padrão
for i, tx in enumerate([24.32, 24.52, 24.72, 24.92, 25.12]): add(sfx, tick := kick(.12, 300, 120, .6), tx, .35); add(sfx, card(.04), tx, .5)
# sinais óbvios
add(sfx, waterdrop(500, 1500, .1), 27.98, .5); add(sfx, clunk(), 28.25, .6)
add(sfx, swell(.9, 300, 3000) * .4, 28.5, .35); add(sfx, splat(.4), 29.5, .7); add(sfx, clunk(), 29.6, .5)
add(sfx, relay() * 2, 29.95, .5); add(sfx, waterdrop(300, 1200, .12), 30.5, .6); add(sfx, tink(2600, .3), 30.85, .35)
# o truque: barra e skill creator
add(sfx, keyclick(1), 33.65, .6); add(sfx, card(.05), 34.08, .5)
for i in range(6): add(sfx, keyclick(.4), 34.94 + i * .05, .25)
add(sfx, relay() * 2, 35.3, .7)
# pede: humanizador, Anti-Robô, com tudo isso, nunca mais explicar
for b in [36.77, 36.97, 37.16, 37.96, 38.16, 38.51, 38.85]:
    for j in range(3): add(sfx, keyclick(.5), b + j * .06, .26)
add(sfx, subdrop(.6, 70, 30), 39.05, .55); add(sfx, glass(midi(86), .9, .01) * .35, 39.1, .6)
add(sfx, swell(.5, 4000, 500) * .5, 39.94, .35); add(sfx, waterdrop(500, 200, .1), 40.45, .5)
add(sfx, marble(.4, 30), 40.92, .3); add(sfx, splat(.3), 41.31, .5); add(sfx, tink(3000, .4), 41.86, .4)
# a skill nasce e instala
add(sfx, paperflutter(.3), 43.36, .45); add(sfx, card(.05), 44.14, .6); add(sfx, waterdrop(400, 1200, .1), 45.42, .5); add(sfx, relay() * 2, 45.55, .6); add(sfx, tink(2600, .4), 45.75, .4)
# /anti-robô
add(sfx, keyclick(1), 47.84, .6)
for i in range(9): add(sfx, keyclick(.6), 48.21 + i * .055, .33)
# o texto volta, carimbo 0%, toda vez
add(sfx, paperflutter(.35), 49.3, .45); add(sfx, pencil(.7, 80), 49.5, .35)
add(sfx, kick(.3, 140, 40, 1), 50.36, .6); add(sfx, relay() * 2, 50.37, .6); add(sfx, glass(midi(93), 1.0, .01) * .3, 50.4, .5)
for tl in (51.95, 52.2): add(sfx, kick(.2, 160, 60, .6), tl, .45); add(sfx, card(.05), tl, .5)
# escada do passo a passo
for i, tl in enumerate((53.26, 53.51, 53.66)): add(sfx, waterdrop(400 + 150 * i, 1200 + 200 * i, .08), tl, .5)
# chamada final: segue, comenta HUMANO
add(sfx, relay() * 2, 54.7, .8); add(sfx, keyclick(1), 54.7, .5); add(sfx, tink(2400, .4), 54.75, .4)
for i in range(6): add(sfx, keyclick(.7), 55.45 + i * .07, .45)
add(sfx, relay() * 2, 56.1, .7); add(sfx, swell(.25, 1500, 7000) * .6, 56.1, .4); add(sfx, card(.05), 56.36, .6)
add(sfx, lp(noise(.08), 1500) * env(.08, .0005, .02), PURP, .9)
add(sfx, pluck_bend(98, .4, 3, .12), LOOP + .22, .6)
# o elemento vermelho: squish, voo, pop (×0,7 em relação ao Dia 10 v3)
HS = [(0, .92), (1.15, 2.22), (2.42, 4.25), (4.62, 5.95), (6.3, 8.4), (9.35, 12.05), (12.35, 12.85), (13.0, 17.3), (17.62, 18.35), (18.55, 23.4), (24.0, 25.55), (26.0, 27.75), (27.98, 28.42), (28.55, 29.45), (29.97, 30.75), (31.15, 33.4), (33.65, 34.85), (34.95, 35.85), (36.8, 38.95), (39.05, 42.45), (43.0, 44.9), (45.05, 46.05), (46.3, 47.15), (47.35, 48.95), (49.45, 50.15), (50.3, 52.5), (52.95, 54.0), (54.25, 55.0), (55.15, 56.2), (56.42, 56.88)]
for i in range(len(HS) - 1):
    t1, t0n = HS[i][1], HS[i + 1][0]
    if t0n - t1 < .05: continue
    add(sfx, waterdrop(420, 180, .09), t1 - .1, .45 * .7)
    add(sfx, pluck_bend(349 + 22 * (i % 5), min(.5, t0n - t1), 7, .12), t1, .3 * .7)
    add(sfx, waterdrop(300, 1500, .08), t0n, .5 * .7); add(sfx, tink(2400 + 150 * (i % 4), .2), t0n + .01, .18 * .7)
# "Claude" vira a logo girando
for tl in (2.11, 8.55, 13.39, 42.90): add(sfx, swell(.3, 1500, 8000) * .6, tl + .05, .3); add(sfx, glass(midi(89), .9, .01) * .3, tl + .3, .6)
sfx = reverb(sfx, .5, .1)
synth.DROP = 54.15
mix(mus, sfx, voice, 'd13.wav', duck=.5, music_db=-6, sfx_db=-7, post=1.0, comp=.25, report=False)
print('ok', TEND)
