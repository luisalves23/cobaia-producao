import sys; sys.path.insert(0,'/home/claude/cobaia-producao/motor')
import numpy as np, synth as S
from synth import *
BPM=104; BEAT=60/BPM; BAR=4*BEAT; N=9; END=N*BAR+1.5
SW=0.58  # swing das semicolcheias
def s16(i): b=i//2; return b*BEAT/2 + (SW-0.5)*BEAT*(i%2)  # posição de colcheias com swing
def marimba(f,d=0.7):
    t=tt(d); s=np.sin(2*np.pi*f*t)*np.exp(-t/0.28)+0.5*np.sin(2*np.pi*f*4*t)*np.exp(-t/0.03)+0.25*np.sin(2*np.pi*f*10*t)*np.exp(-t/0.008)
    return (s*np.minimum(1,t/0.0015)).astype(np.float32)
def logdrum(f,d=0.55):
    t=tt(d); ff=f*(1+0.35*np.exp(-t/0.02)); ph=2*np.pi*np.cumsum(ff)/SR
    s=np.tanh(1.6*(np.sin(ph)+0.3*np.sin(2*ph)*np.exp(-t/.06)))*np.exp(-t/0.22); return lp(s.astype(np.float32),900)
def rim(d=0.08): t=tt(d); return (bp(noise(d),1500,4500)*np.exp(-t/0.006)+0.6*np.sin(2*np.pi*1700*t)*np.exp(-t/0.012)).astype(np.float32)
def conga(f=220,d=0.3): t=tt(d); ff=f*(1+0.15*np.exp(-t/0.01)); return (np.sin(2*np.pi*np.cumsum(ff)/SR)*np.exp(-t/0.12)+0.2*bp(noise(d),800,3000)*np.exp(-t/0.004)).astype(np.float32)
def brass(notes,d):  # stab de metais sintetizado, brilhante e curto
    t=tt(d); s=np.zeros_like(t,dtype=np.float32)
    for n in notes:
        f=midi(n); ph=2*np.pi*f*t+0.8*np.sin(2*np.pi*f*t)*np.exp(-t/0.08)
        s+=np.sin(ph+1.2*np.sin(ph)*np.exp(-t/0.15)).astype(np.float32)
    e=np.minimum(1,t/0.012)*np.exp(-t/0.25); return (lp(s,4000)*e/len(notes)).astype(np.float32)
# acordes: G  D/F#  Em  C   (sol maior, I V vi IV)
CH=[[55,59,62,67],[54,57,62,66],[52,55,59,64],[48,52,55,60]]
ROOT=[43,38,40,36]
L={k:buf(END) for k in 'drum perc bass mar pad brass'.split()}
RIFF=[0,2,3,5,7,8,10,12,13,15]  # semicolcheias do riff de marimba (pergunta/resposta)
ARP=[3,2,1,2,3,1,2,0,3,2]
for b in range(N):
    t0=b*BAR; c=b%4; dens= 1 if b in (0,1,5,6,7,8) else .55 if b in (2,3) else .8
    # bateria: kick em 1 e no "e" do 3 (afro), palmas no 2 e 4
    for p in ([0,2.5] if b not in (4,) else [0,1,2,3]):
        add(L['drum'],kick(0.4,95,45,.6),t0+p*BEAT,.9 if dens>.6 or p==0 else .5)
    if b not in (2,3): [add(L['drum'],snap(),t0+p*BEAT,.55) for p in (1,3)]
    for i in range(16):
        tp=t0+(i//2)*BEAT/2*0+ (i*BEAT/4) + (SW-.5)*BEAT/2*(i%2)
        add(L['perc'],shaker(),tp,(.35 if i%2 else .55)*(.7+.3*dens))
    for p in [0,.75,1.5,2.5,3.0]: add(L['perc'],rim(),t0+p*BEAT,.35*dens)
    if dens>.6:
        for p,f in [(1.75,260),(2.0,200),(3.5,260),(3.75,200)]: add(L['perc'],conga(f),t0+p*BEAT,.35)
    # log drum como baixo: padrão sincopado
    for p,o in [(0,0),(1.5,0),(2.25,12),(2.75,7),(3.5,5)]:
        if dens<.6 and p>2: continue
        add(L['bass'],logdrum(midi(ROOT[c]+o)),t0+p*BEAT,.8)
    # marimba: riff nas notas do acorde
    for k,i in enumerate(RIFF):
        n=CH[c][ARP[k]]+12; tp=t0+i*BEAT/4+(SW-.5)*BEAT/2*(i%2)
        add(L['mar'],marimba(midi(n)),tp,.45*(1 if dens>.6 else .8))
    # pad suave por baixo
    add(L['pad'],pad(CH[c],BAR+.2,cut=1400 if dens<.9 else 2600,att=.05,rel=.3),t0,.6)
    # metais no drop
    if b>=5:
        for p in [0,1.5,3]: add(L['brass'],brass([n+12 for n in CH[c][1:]],.4),t0+p*BEAT,.5 if p else .7)
# virada/subida no compasso 4 (índice 4): conga em semicolcheias crescendo + filtro abrindo
t0=4*BAR
for i in range(16): add(L['perc'],conga(200+8*i),t0+i*BEAT/4,.15+.03*i)
add(L['perc'],swell(BAR,300,7000),t0,.25)
add(L['drum'],subdrop(1.4),5*BAR,.5)
# gancho: impacto no 0
add(L['drum'],kick(.5,130,40,1.2),0,.6)
mus=sum(reverb(L[k],1.1,.18) if k in('mar','brass','perc') else L[k] for k in L)
mus=hp(mus,30); mus=np.tanh(mus*1.1)/1.1; mus/=np.abs(mus).max()/0.9
write('amostra-musica.wav',mus)
print(END)
