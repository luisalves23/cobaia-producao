# Análise das 5 referências de fluid motion (16/11/2026)

Método: frames a 3 fps (folhas de contato) e 12 fps nas transições (`folhas/s0*.jpg`), detecção de cortes e análise de áudio (onsets, BPM, volume a cada 0,5 s, brilho espectral). Folhas em `folhas/`.

## Ficha técnica
| Ref | Peça | Formato | Duração | Trilha |
|---|---|---|---|---|
| 01 | "I make things move" / showreel | 9:16, 60 fps | 15 s | ~120 BPM, eventos na grade de 1/16; respiro 7,5–10 s; volta cheia na recapitulação |
| 02 | Maxterz (logo) | 9:16, 30 fps | 9 s | sem trilha de fundo (34% silêncio); cada quique da bola = um som = troca de cor (0,32 / 0,74 / 1,16 / 1,63 s) |
| 03 | Finqube (app de finanças) | 9:16, 60 fps | 45 s | ~134 BPM; baixa até 13 s, drop na revelação do logo (13,5 s); some no fim |
| 04 | Spidra (conceito Spotify/Espresso) | 4:5, 24 fps | 17 s | a própria música (~104 BPM) entra no clique do player (2,5 s); corte seco em 12,7 s, logo em silêncio |
| 05 | Teddy Graphics "UX in motion" | 16:9, 24 fps | 15 s | ~128 BPM; montagem de 8,0 a 11,3 s com um corte por batida (0,46 s) |

## Linha do tempo resumida
- **01:** texto digitado → o ponto final laranja vira o protagonista (íris escura) → círculo/quadrado/losango/pílula com contorno-fantasma indicando a forma-alvo e o preenchimento atrasado → multiplica em grade de pontos → campo vetorial (fluxo) → dobra em esfera → colapsa num círculo branco que vira o fundo → a fórmula spring(t) desenhando a própria curva → "900 frames / 60 fps / 0 keyframes / 1 function" → recapitulação em 1/16 → o ponto pousa como ponto final de "CLAUDE.".
- **02:** bola azul quica; cada quique inverte o fundo e revela uma palavra → encolhe → cresce e enche a tela → vira caneta e desenha "maxterz" → desenha o "m" → o círculo encolhe e vira o selo do logo.
- **03:** marca-texto que desliza entre palavras (Freelancer/Solopreneur/Creator) + rabiscos amarelos → caos de ícones XLS e notificações em 3D com profundidade de campo → caem num morro verde → "Where is my money?" → ícone do app → logo e dashboard (drop) → cartões flutuando, câmera atravessando → "FREE" com emojis → preço → CTA parado 6,5 s (ponto fraco).
- **04:** logo Spotify vira pílula de busca "Espresso" → clique → ondas concêntricas enchem a tela → player → cartão de letra azul com karaokê no tempo da música e cartão "gelatinoso" (cantos deformam no movimento) → iMessage sobre foto desfocada digitando a letra → "That's that me" tipográfico → "Espresso" neon com xícara → corte seco, logo em silêncio.
- **05:** ponto pulsando (radar) → vira toggle → bolinha do toggle cresce e enche → "UX IN MOTION" com o O como anel → fluxo de pagamento, uma palavra por batida (Amount. Tap. PIN. Approved. Printed.) → montagem de microinterações na batida → parede isométrica com todas as telas → volta ao ponto → mascote desenhado. Etiquetas pequenas de HUD nos cantos.

## Em comum
1. Um elemento condutor (ponto, bola, pílula, cartão) atravessa o vídeo; a transição é o próprio objeto (cresce e vira fundo, vira letra, vira logo). Quase sem corte seco.
2. Física de mola: overshoot e assentamento, squash & stretch na direção do movimento, follow-through (parte atrasada), desfoque só no trecho rápido.
3. Som preso à grade: cada evento visual cai numa batida ou subdivisão; a música respira antes da revelação e cai ou para no logo.
4. Arco: semente → transformação → revelação → volta ao início (loop).
5. Contenção: 1 cor de destaque + neutro, muito espaço vazio, uma ideia por vez.
6. Ritmo variável: rajadas rápidas alternando com pausas curtas.

## Único de cada
- 01: o movimento explica a si mesmo (mostra a curva spring); contorno-fantasma antecipando a forma; pontos → campo vetorial → esfera (partículas com comportamento de fluido).
- 02: um elemento só faz tudo; cor inverte no quique; só efeitos, sem música: cada som é um evento físico.
- 03: história problema → solução (caos → ordem); profundidade 3D com DOF; camada "feita à mão" (marca-texto, rabisco).
- 04: a música é o roteiro (letra dirige a cena); cartões com deformação de corpo mole; interface (chat) contando história; corte seco do som para o logo.
- 05: fluxo de usuário como narrativa, uma palavra por batida; montagem na batida; parede isométrica de recapitulação; HUD de ficha técnica.

## Ligação com o @cobaia.dev
A skill hoje liga cenas por passagem de câmera lateral (0,36 s). As referências ligam cenas por transformação do objeto. Caminho: escolher um objeto condutor por vídeo (ex.: o ponto vermelho), trocar back-out por mola real (função determinística no GSAP), e um efeito sonoro por evento físico, na grade da música.
Limite: a análise de áudio foi por espectro e onsets; não dá para afirmar a origem de cada efeito.
