# Motor

O que renderizou o Dia 10 v3 aprovado. Tudo é determinístico: o quadro `f` é sempre `draw(f / 30)`.

## Arquivos
| Arquivo | O que faz |
|---|---|
| `lib.js` | Base de animação em canvas 1080×1920: `spring(t, f, z)` e `springV` (mola com overshoot), `easeOutCubic`, `easeInOutCubic`, `easeInCubic`, `easeOutExpo`, `clamp`, `lerp`, `inv`, `rng(seed)`, `noise1` (ruído suave), `mk(w,h)` (canvas extra), `rr` (retângulo arredondado), `springText`, `textW`, `resample`, `grain`. |
| `icons.js` | Desenhos vetoriais oficiais (`CLAUDE_PATH` e outros). Logo nova entra aqui. |
| `fonts.css` + `fonts/` | Inter 400/800/900, Anton, Instrument Serif (normal e itálico), JetBrains Mono 400/700, Permanent Marker, Dela Gothic One (OFL). |
| `perfil.jpg` | Foto de perfil do canal (chamada final, capas, site). |
| `synth.py` | Áudio sem samples: instrumentos (`kick`, `hat`, `shaker`, `snap`, `ks`, `pluck_bend`, `kalimba`, `pizz`, `glass`, `tink`, `pad`, `subdrop`, `swell`, `tapestop`), foley (`waterdrop`, `pencil`, `marble`, `splat`, `paperflutter`, `keyclick`, `ratchet`, `relay`, `clunk`, `crackle`, `card`), `reverb`, `follower` (ducking) e `mix(...)`. |
| `render.cjs` | Render completo num processo: `node render.cjs dNN.html frames`. |
| `render-paralelo.cjs` | Render em fatias: `node render-paralelo.cjs dNN.html frames I N` (rode I = 0..N−1 ao mesmo tempo). |
| `storyboard.cjs` | Quadros estáticos em tempos escolhidos: `node storyboard.cjs dNN.html sb 0.5 2.1 4.0 ...`. |
| `folha.py` | Folha de contato: `python3 folha.py sb storyboard.jpg [colunas] [largura]`. |
| `enc.sh` | MP4 final: `bash enc.sh frames mix.wav saida.mp4` (x264 crf 17, AAC 256k, loudnorm −14 LUFS / −1,2 dBTP). |
| `enc-leve.sh` | Versão < 25 MB a partir do HQ (dois passes). |
| `novo-dia.sh` | Cria `producoes/diaNN/` com tudo isto e a base do Dia 10 v3. |
| `voz/` | `transcribe.py` (faster-whisper), `align.py` (alinhamento pelo texto quando o whisper não baixa), `cut3.py` / `cut.py` (corte de silêncio), `medir-musica.py` (BPM e volume). |

## Contrato da página do vídeo (`dNN.html`)
- Carrega `fonts.css`, `lib.js`, `dNNchunks.js`, `icons.js`.
- Define `window.NFRAMES` (duração × 30), `window.ready` (Promise que espera fontes e foto) e a função global `draw(t)`.
- Sem `Date`, sem `Math.random` sem semente, sem CSS transition, sem rede.

## Formato das palavras grandes (`dNNchunks.js`)
```js
const CHUNKS=[{"f":"anton","t":0.44,"w":[["roubando",0.44,1]]}, ...]
```
- `f`: fonte do bloco (`inter`, `anton`, `serif`, `mono`); `t`: início do bloco em segundos.
- `w`: palavras `[texto, tempo, destaque, fonte opcional]`. Destaque: 0 normal, 1 vermelho, 2 "Claude" (laranja, vira a logo), 3 verde (positivo).
- Uma palavra ou frase curta por bloco; a fonte alterna entre blocos e pode mudar dentro da frase ("de 30" em Inter, "experimentos" em serif).

## Verificar uma instalação nova
```bash
cd referencia/dia10-v3/fonte
node ../../../motor/storyboard.cjs d10.html /tmp/sb 7.5
ffmpeg -v error -ss 7.5 -i ../postar/cobaia-dia10-final-leve.mp4 -frames:v 1 /tmp/ref.jpg
```
Os dois quadros precisam ser iguais (diferença média de pixel perto de 1, só compressão). `python3 a10.py` precisa gerar `d10.wav` com 54,8 s.
