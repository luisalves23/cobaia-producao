# Motor

O que renderizou o Dia 10 v3 aprovado. Tudo é determinístico: o quadro `f` é sempre `draw(f / 30)`.

## Arquivos
| Arquivo | O que faz |
|---|---|
| `lib.js` | Base de animação em canvas 1080×1920: `spring(t, f, z)` e `springV` (mola com overshoot), `easeOutCubic`, `easeInOutCubic`, `easeInCubic`, `easeOutExpo`, `clamp`, `lerp`, `inv`, `rng(seed)`, `noise1` (ruído suave), `mk(w,h)` (canvas extra), `rr` (retângulo arredondado), `springText`, `textW`, `resample`, `grain`. |
| `icons.js` | Desenhos vetoriais oficiais (`CLAUDE_PATH` e outros). Logo nova entra aqui. |
| `fonts.css` + `fonts/` | Inter 400/800/900, Anton, Instrument Serif (normal e itálico), JetBrains Mono 400/700, Permanent Marker, Dela Gothic One (OFL). |
| `perfil.jpg` | Foto de perfil do canal (chamada final, capas, site). |
| `synth.py` | Áudio sem samples: instrumentos (`supersaw` acorde de future bass do Dia 13, `kick`, `hat`, `shaker`, `snap`, `ks`, `pluck_bend`, `kalimba`, `pizz`, `glass`, `tink`, `pad`, `subdrop`, `swell`, `tapestop`), foley (`waterdrop`, `pencil`, `marble`, `splat`, `paperflutter`, `keyclick`, `ratchet`, `relay`, `clunk`, `crackle`, `card`), `reverb`, `follower` (ducking) e `mix(...)`. |
| `trilha.py` | **Experimental, reprovado pelo Luis em 19/11 (degraus de volume e trocas secas).** Trilha montanha-russa: `Narr(energia, drops, paradas, impactos, subida_tom, fim)` + `render(estilo, narr, dur)` com estilos `electro`, `dnb` e `futurebass`. Camadas, filtro e volume seguem a curva de energia; riser e caixa acelerando terminam no drop. Exemplo no `producoes/dia12/fonte/a12.py` (`ESTILO=dnb python3 a12.py`). |
| `render.cjs` | Render completo num processo: `node render.cjs dNN.html frames`. |
| `render-paralelo.cjs` | Render em fatias: `node render-paralelo.cjs dNN.html frames I N` (rode I = 0..N−1 ao mesmo tempo). |
| `storyboard.cjs` | Quadros estáticos em tempos escolhidos: `node storyboard.cjs dNN.html sb 0.5 2.1 4.0 ...`. |
| `folha.py` | Folha de contato: `python3 folha.py sb storyboard.jpg [colunas] [largura]`. |
| `enc.sh` | MP4 final: `bash enc.sh frames mix.wav saida.mp4` (x264 crf 17, AAC 256k, loudnorm −14 LUFS / −1,2 dBTP). |
| `enc-leve.sh` | Versão < 25 MB a partir do HQ (dois passes). |
| `novo-dia.sh` | Cria `producoes/diaNN/` com tudo isto e a base limpa de `base/`. |
| `base/` | Modelo de novo dia do Dossiê Cobaia 2.0: `dNN.html` (acabamento do Dia 10 v3 sem cena de calendário, sem gancho palavra por palavra e sem frase de envio; com frase-tema fixa `TEMA`, selo, legenda e card do próximo episódio `PROXIMO`), `dNNlegenda.js` (legenda embaixo) e `aNN.py` (áudio sem a vinheta). Medidas da frase-tema e da legenda são proposta até o Luis aprovar no primeiro storyboard. `referencia/dia10-v3/` continua intacto para a verificação de instalação. |
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
- Palavras grandes são destaque, depois do gancho: no gancho a frase entra inteira e fixa no quadro 0, e a legenda embaixo acompanha a fala o tempo todo (Dossiê Cobaia 2.0).
- Uma palavra ou frase curta por bloco; a fonte alterna entre blocos e pode mudar dentro da frase ("de 30" em Inter, "experimentos" em serif).

### Como montar (não há script: os blocos são escritos à mão a partir das palavras com tempo)
Feito assim no Dia 10 (66 blocos, conferir em `referencia/dia10-v3/fonte/d10chunks.js`):
1. Pegue as palavras com tempo da voz (`align.json` ou `palavras.json`, seção 5 do `motor/voz/LEIAME.md`), com a grafia do roteiro aprovado.
2. **Agrupe em blocos de 1 a 4 palavras** (no Dia 10: 16 de uma, 25 de duas, 18 de três, 7 de quatro), cortando nas unidades naturais da fala: "Isso tá" / "roubando" / "metade" / "do seu Wi-Fi". A palavra de impacto fica sozinha no bloco.
3. **`t` do bloco = início da primeira palavra**; o tempo de cada palavra é o início dela (`s`).
4. **Fonte por bloco**, alternando para nunca ficar igual por muito tempo (no Dia 10: 26 serif, 20 inter, 17 anton, 3 mono):
   - `anton`: impacto, números e marcos ("Dia 10", "Um:", "Dois:", "operadora", "brigam", "pro ralo");
   - `serif` (Instrument Serif itálico): emoção, ligação e pergunta ("mas eu", "nesse vídeo", "quase sempre", "a cereja do bolo");
   - `inter` (900): frase neutra de ação ("do seu Wi-Fi", "mede a velocidade");
   - `mono`: termo técnico ou de tela, digitado ("um prompt", "escondido", "testa de novo").
5. **Duas fontes na mesma frase:** 4º campo na palavra (`["de",5.7,0,"inter"],["30",5.92,0,"inter"],["experimentos",6.28,1,"serif"]`).
6. **Destaques:** `1` vermelho em no máximo uma ideia-chave por bloco (cerca de 1 bloco a cada 3); `2` só em "Claude" (e "Code" em "Claude Code"), que vira a logo; `3` verde só no que é positivo ("aprovar", "subir").
7. **A chamada final não entra nos blocos:** entre `CTA0` e `RALO` as palavras ficam escondidas (`hideWords` no `dNN.html`) e a chamada tem a animação própria. O último bloco é a frase de fechamento antes do roxo.
8. Confira no storyboard que cada bloco acende no tempo da fala.

## Verificar uma instalação nova
```bash
cd referencia/dia10-v3/fonte
node ../../../motor/storyboard.cjs d10.html /tmp/sb 7.5
ffmpeg -v error -ss 7.5 -i ../postar/cobaia-dia10-final-leve.mp4 -frames:v 1 /tmp/ref.jpg
```
Os dois quadros precisam ser iguais (diferença média de pixel perto de 1, só compressão). `python3 a10.py` precisa gerar `d10.wav` com 54,8 s.
