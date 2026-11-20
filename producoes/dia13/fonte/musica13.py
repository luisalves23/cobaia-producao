# DIA 13 v2: drum and bass solar em ré maior a 172 BPM (trilha nova: nada de house, electro, future bass ou afro-pop)
# Clima sempre para cima: desce de leve e volta subindo, com drops em "ZERO", "truque" e no segundo "ZERO".
import numpy as np, synth
from synth import *
BPM = 172; BT = 60 / BPM; BAR = 4 * BT
CH = [[62, 66, 69, 74], [61, 64, 69, 73], [59, 62, 66, 71], [55, 59, 62, 67]]   # D  A/C#  Bm  G
RT = [38, 33, 35, 31]
def saw(f, d, det=0.0):
    t = tt(d); return (2 * ((f * (1 + det) * t) % 1) - 1).astype(np.float32)
def reese(n, d):
    f = midi(n); t = tt(d); s = .5 * saw(f, d, -.006) + .5 * saw(f, d, .006); s = lp(s, 380, 2) + .9 * np.sin(2 * np.pi * f * t)
    return (s * np.minimum(1, t / .01) * np.minimum(1, np.maximum(0, d - t) / .04) * .6).astype(np.float32)
def snare(d=.22):
    t = tt(d); s = .9 * bp(noise(d), 1200, 7000) * np.exp(-t / .055) + .7 * np.sin(2 * np.pi * 190 * t) * np.exp(-t / .03); return s.astype(np.float32)
def ride(d=.25): t = tt(d); return (hp(noise(d), 6000) * np.exp(-t / .07) * .5).astype(np.float32)
def crash(d=1.6): t = tt(d); return (hp(noise(d), 4000) * np.exp(-t / .5) * .6).astype(np.float32)
def pluck(f, d=.3):
    t = tt(d); s = saw(f, d) * .6 + saw(f, d, .005) * .4; cut = 700 + 5000 * np.exp(-t / .06)
    out = np.zeros_like(s); seg = 480
    for i in range(0, len(s), seg): out[i:i + seg] = lp(s[max(0, i - 2000):i + seg], float(cut[i]), 2)[-len(s[i:i + seg]):]
    return (out * np.exp(-t / .16) * np.minimum(1, t / .002)).astype(np.float32)
# --- mapa da trilha (segundos do vídeo). nível 0..3 ---
SEC = [(0, 3), (2.46, 3), (6.3, 1), (9.16, 2), (10.46, 3), (17.0, 2), (22.6, 2.5), (24.75, 3), (29.3, 1.2), (29.96, 3), (40.1, 2), (44.1, 2.5), (46.95, 3), (50.55, 3)]
def lvl(t):
    v = 0
    for a, l in SEC:
        if t >= a: v = l
    return v
DROPS = [0.0, 2.46, 10.46, 29.96, 46.95]
ANCH_X = [53.35]
BUILDS = [(9.16, 10.46), (28.9, 29.96), (45.2, 46.95)]
def music(TEND):
    L = {k: buf(TEND) for k in ['kick', 'snare', 'hat', 'bass', 'stab', 'arp', 'pad', 'fx']}
    ANCH = DROPS + [53.35, TEND]
    for si in range(len(ANCH) - 1):
        a0, a1 = ANCH[si], ANCH[si + 1]; k = 0
        while a0 + k * BT < a1 - .01:
            t = a0 + k * BT; bb = k // 4; c = bb % 4; p = k % 4; lv = lvl(t + .01); k += 1
            inb = any(x <= t + .01 < z for x, z in BUILDS)
            room = a1 - t
            if lv >= 2 and not inb:
                if p == 0: add(L['kick'], kick(.3, 120, 44, .8), t, .9)
                if p == 2 and room > BT * .5: add(L['kick'], kick(.3, 120, 44, .8), t + BT * .5, .9)
                if p in (1, 3): add(L['snare'], snare(), t, .8); add(L['snare'], snare(.1), t + BT * (.75 if p == 1 else .5), .22)
                for i in range(2): add(L['hat'], hat(.05, .015), t + i * BT / 2, .35 if i else .22)
                if lv >= 3: add(L['hat'], ride(), t, .3)
            elif lv >= 1 and not inb:
                if p == 0: add(L['kick'], kick(.3, 120, 44, .8), t, .6)
                if p in (1, 3): add(L['snare'], snare(.12), t, .5)
                add(L['hat'], ride(), t, .28); add(L['hat'], hat(.05, .015), t + BT / 2, .25)
            if lv >= 2:
                if p == 0: add(L['bass'], reese(RT[c], min(1.4 * BT, room)), t, .8 if lv >= 3 else .6)
                if p == 1: add(L['bass'], reese(RT[c], .5 * BT), t + .5 * BT, .8 if lv >= 3 else .6)
                if p == 2 and room > BT * .5: add(L['bass'], reese(RT[c], min(1.4 * BT, room - .5 * BT)), t + .5 * BT, .8 if lv >= 3 else .6)
            elif lv >= 1 and p == 0: add(L['bass'], reese(RT[c] + 12, min(3.8 * BT, room)) * .5, t, .6)
            if lv >= 3:
                off = {0: .5, 1: .5, 2: .75, 3: .5}[p]
                if room > off * BT: add(L['stab'], supersaw([n + 12 for n in CH[c]], .16, cut=5200, att=.004, rel=.06), t + off * BT, .55)
            if lv in (1, 1.2, 2, 2.5) or (lv >= 3 and bb % 2):
                seq = [0, 1, 2, 3, 2, 1, 3, 2]
                for i in range(4):
                    if i * BT / 4 < room: add(L['arp'], pluck(midi(CH[c][seq[(p * 4 + i) % 8]] + 12), .22), t + i * BT / 4, .3 if lv < 3 else .16)
            if p == 0: add(L['pad'], pad(CH[c], min(BAR + .1, room + .05), cut=1600 + 900 * min(lv, 3), att=.08, rel=.2), t, .6 if lv < 2 else .45)
    # builds: rufo de caixa acelerando + filtro subindo (sobe sem descer o clima)
    for a, z in BUILDS:
        n = int((z - a) / (BT / 4)); 
        for i in range(n):
            tp = a + i * BT / 4; k = i / max(1, n - 1); add(L['snare'], snare(.08), tp, .15 + .55 * k)
        add(L['fx'], swell(z - a, 300, 9000), a, .45)
    # impactos nos drops
    for d in DROPS:
        add(L['kick'], kick(.5, 150, 38, 1.2), d, 1.0); add(L['fx'], crash(), d, .55); add(L['fx'], subdrop(1.2, 70, 30), d, .6)
    mix_ = {'kick': 1.0, 'snare': .75, 'hat': .5, 'bass': .8, 'stab': .5, 'arp': .55, 'pad': .4, 'fx': .55}
    # sidechain leve do kick no pad, baixo e stabs (respira junto da batida)
    env_k = follower(L['kick'], .002, .12); env_k /= env_k.max() + 1e-9
    duck = 1 - .35 * np.clip(env_k * 2, 0, 1)
    out = (L['kick'] * mix_['kick'] + L['snare'] * mix_['snare'] + L['hat'] * mix_['hat'] + L['fx'] * mix_['fx']
           + (L['bass'] * mix_['bass'] + reverb(L['stab'], .9, .18) * mix_['stab'] + reverb(L['arp'], .9, .18) * mix_['arp'] + L['pad'] * mix_['pad']) * duck)
    out = hp(out, 28); out = np.tanh(out * 1.2) / 1.2
    return (out / (np.abs(out).max() + 1e-9) * .9).astype(np.float32)
if __name__ == '__main__':
    import sys; T = float(sys.argv[1]) if len(sys.argv) > 1 else 24
    m = music(T); write(sys.argv[2] if len(sys.argv) > 2 else 'musica13.wav', m); print('ok', T)
