import sys, subprocess, wave, numpy as np
sys.path.insert(0,'.')
import synth as S
from synth import *
T=6.0; S.END=T; S.DROP=99
raw = subprocess.run(['ffmpeg','-v','error','-i','voz.mp3','-af','highpass=f=80,equalizer=f=3500:t=q:w=1:g=1.5,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80','-ac','1','-ar',str(SR),'-f','s16le','-'],capture_output=True).stdout
x=np.frombuffer(raw,np.int16).astype(np.float32)/32768; voice=buf(T); voice[:]=x[:len(voice)]
w=wave.open('amostra-musica.wav'); m=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32).reshape(-1,2)[:,0]/32768
mus=buf(T); mus[:]=m[:len(mus)]
sfx=buf(T)
def thud(g=1.0): return (kick(.3,90,38,.4)+splat(.3)*.5)*g
add(sfx,thud(1.2),0,1); add(sfx,paperflutter(.35),.0,.3)
add(sfx,paperflutter(.25),.41,.35); add(sfx,clunk(),.62,.6); add(sfx,card(),.62,.5)
for k in range(19): add(sfx,keyclick(.6),.64+k*.047,.35)
add(sfx,waterdrop(700,1500),1.75,.6); add(sfx,tink(midi(88)),2.03,.25)
add(sfx,glass(midi(76),.6),2.15,.18); add(sfx,card(),2.28,.4); add(sfx,paperflutter(.2),2.3,.25)
add(sfx,thud(1.4),2.455,1); add(sfx,glass(midi(83),.9),2.47,.25); add(sfx,pencil(.4),2.52,.3)
add(sfx,swell(.5,400,4000),3.45,.18); add(sfx,waterdrop(500,1300),3.97,.6)
for t0,g in ((3.98,.7),(4.66,.5),(4.78,.5)): add(sfx,clunk(),t0,g)
for k in range(4): add(sfx,card(),4.16+k*.2,.25)
add(sfx,swell(.55,1500,9000),5.08,.2); add(sfx,tink(midi(84)),5.76,.35); add(sfx,tink(midi(91)),5.86,.3)
mix(mus,sfx,voice,'previa6.wav',duck=.45,music_db=-7,sfx_db=-6,post=1.0,comp=.3,report=False)
