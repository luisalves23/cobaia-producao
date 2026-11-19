from synth import *
# 07 SÍNTESE — trilha no estilo do 03 (house lo-fi, acordes abafados que abrem no drop), mais agitada; sons do 05; final do 04.
mus, sfx = buf(), buf(); voice = load_voice()
def sawbass(n, d=.4, cut=500):
    t = tt(d); f = midi(n); s = 2 * ((f * t) % 1) - 1; return lp((s * np.exp(-t / .22) * np.minimum(1, t / .003)).astype(np.float32), cut)
def rim(): d = .06; t = tt(d); return (bp(noise(d), 1500, 4000) * np.exp(-t / .006) + .5 * np.sin(2 * np.pi * 820 * t) * np.exp(-t / .01)).astype(np.float32)
prog = [[57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 65], [52, 55, 59, 62]]; roots = [45, 41, 43, 40]
for bar in range(6):
    t0 = bar * 2.0; ch = prog[bar % 4]; root = roots[bar % 4]; brk = bar == 3
    cut = 1000 if bar < 4 else 3600
    add(mus, pad(ch, 1.0 if brk else 2.0, cut, .02, .25), t0, .55)
    # stabs sincopados de acorde (agitação)
    for off in [0.75, 1.5, 2.75, 3.5]:
        if brk and off >= 2: continue
        add(mus, pad(ch, .22, cut + 800, .005, .1), t0 + off * BEAT, .5)
    for k in range(4):
        if brk and k >= 2: continue
        if not (bar == 0 and k == 0 and False): add(mus, kick(f0=105, punch=.7), t0 + k * BEAT, 1)
        add(mus, hat(.05, .02), t0 + k * BEAT + BEAT / 2, .45)
    for k in range(16):
        if brk and k >= 8: continue
        add(mus, shaker(), t0 + k * BEAT / 4, .2 if k % 2 else .1)
    for k in (1, 3):
        if not (brk and k == 3): add(mus, snap(), t0 + k * BEAT, .5)
    for k in (3, 7, 11, 14):
        if not (brk and k >= 8): add(mus, rim(), t0 + k * BEAT / 4, .35)
    for k, off in enumerate([0, .75, 1.5, 2.5, 3.25]):
        if brk and off >= 2: continue
        add(mus, sawbass(root + (12 if k == 3 else 0), cut=450 if bar < 4 else 1000), t0 + off * BEAT, .8)
mus = reverb(mus, 1.1, .14)
cut12 = int(12.0 * SR); mus[cut12:] = 0                       # corte seco do 04
# sons do 05 (mecânicos) + slime a cada palavra
for k, tw in W.items(): add(sfx, waterdrop(260, 520, .09) * .8, tw - .04, .35)
n = len('uma ideia solta')
for i in range(n): add(sfx, keyclick(.7), W['uma'] + .1 + i * (W['solta'] + .3 - W['uma']) / n, .45)
for tt_ in (W['uma'], W['vira1'], W['vira2'], 9.0): add(sfx, clunk(), tt_, .8); add(sfx, ratchet(.3, 9) * .6, tt_ + .02, .4)   # a linha constrói
for tt_ in (W['um'], W['plano1'] + .15, W['o'] + .1): add(sfx, relay() * 2, tt_, .9); add(sfx, tink(2400, .2), tt_ + .01, .2)
for i in range(9): add(sfx, keyclick(.3), W['vira2'] + .1 + i * .12, .45)
t = W['eo']
while t < BREAK: add(sfx, relay(), t, .5); t += .09 + .2 * ((t - W['eo']) / (BREAK - W['eo'])) ** 2
tone = np.sin(2 * np.pi * np.cumsum(880 * 2 ** (tt(1.0) / 12)) / SR).astype(np.float32) * np.minimum(1, tt(1.0) / .3) * .25
add(sfx, tone, BREAK, .5)
add(sfx, subdrop(1.4, 75, 35), DROP, 1.0); add(sfx, kick(.5, 140, 40, 1.2), DROP, .9)
for tb in (8.5, 9.0): add(sfx, pluck_bend(98, .5, 3, .12), tb, 1.0); add(sfx, kick(.3, 90, 45, .3), tb, .6)   # quiques (01)
ui = [lambda: clunk(), lambda: ratchet(.3, 9), lambda: ratchet(.25, 6), lambda: tink(1500, .4)]
for b, f in enumerate(ui): add(sfx, f(), 9.25 + .5 * b, .8)
for i in range(14): add(sfx, card(.03), 11.0 + i * .05, .4)
# final do 04: clique do corte + nota de vidro; outra nota no "professor"
add(sfx, lp(noise(.08), 1500) * env(.08, .0005, .02), 12.0, .9)
add(mus, glass(midi(81), 1.6, .02) * .4, 12.02, 1); add(mus, glass(midi(88), 1.6, .02) * .35, 12.3, 1); add(mus, glass(midi(93), 1.4, .02) * .3, 12.5, 1)
sfx = reverb(sfx, .5, .1)
mix(mus, sfx, voice, 'u7.wav', duck=.5, music_db=-5, sfx_db=-6, post=1.7, comp=.25)
