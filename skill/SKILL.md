---
name: "cobaia-dev-videos"
description: "Roteiros, cenas e vídeos curtos do @cobaia.dev (série 30 dias, 30 experimentos com Claude) seguindo o Dossiê Cobaia 2.0 e a identidade, animações, áudio e processo aprovados pelo Luis."
---

# @cobaia.dev: vídeos curtos

Esta skill guarda tudo que o Luis aprovou nos vídeos do @cobaia.dev: identidade, animações, áudio, roteiro, chamada final e o processo técnico. Leia inteira antes de produzir qualquer roteiro, cena ou vídeo do canal.

Prioridade: o que o Luis pedir na conversa vence tudo. Depois vem o **Dossiê Cobaia 2.0** (`DOSSIE.md` na raiz do repositório), que vale por cima desta skill e de qualquer modelo ou doc antigo. Depois esta skill. Logo depois de um pedido do Luis, registre a mudança nesta skill (seção 13).

Meta permanente: **cada vídeo precisa superar o anterior** nas metas do dossiê (pulo nos 3 s abaixo de 35%, tempo médio de 25 s ou mais, seguidores/espectadores de 2% ou mais, envios de 2% ou mais, salvamentos de 4% ou mais), sem quebrar nenhuma regra.

**Em todo trabalho entregue ao Luis, mostre o checklist da seção 11 do dossiê preenchido** (seção 11 desta skill). Item "não" se corrige antes de entregar, ou se explica por que não dá. Quando o Luis mandar os números de um vídeo postado, faça a revisão da seção 12 do dossiê e proponha o ajuste no `DOSSIE.md`, com a data e o vídeo que provou.

## 0. Repositório primeiro (regra que vale para todas as seções)

Tudo o que se repete entre os vídeos mora no repositório privado `luisalves23/cobaia-producao`, que é a fonte única para todas as contas do Claude que produzem o canal. Comece pelo `CLAUDE.md` e pelo `DOSSIE.md` da raiz.

1. **Antes de cada produção: `git pull`.** Outra conta pode ter melhorado a skill, o motor ou as regras. Leia as entradas novas do `CHANGELOG.md` antes de começar.
2. **Todo vídeo novo nasce com `bash motor/novo-dia.sh NN`**, que cria `producoes/diaNN/` com o motor e a base do Dia 10 v3. A base serve para o acabamento (paleta, leque, elemento vermelho, chamada final, roxo e loop); as cenas são sempre novas. A cena de calendário e a vinheta da base saem sempre (dossiê, seção 13).
3. **O storyboard indica, cena por cena, de onde veio a peça** (referência, peça do motor ou "nova").
4. **Peça nova e reaproveitável volta para `motor/`** no fim do vídeo, com uma linha no `motor/LEIAME.md`.
5. **Mudou a identidade ou o processo?** Mude aqui (skill, motor ou CLAUDE.md), registre no `CHANGELOG.md` e dê push no mesmo dia.

## 1. O canal

- Perfil **@cobaia.dev**, lema "testo antes de você". Redes: Instagram Reels, TikTok e YouTube Shorts.
- **Objetivo (dossiê, seção 1): crescer em seguidores e alcance**, com autoridade, e preparar a venda sem vender no vídeo. Meta de médio prazo: 50 mil seguidores no Instagram.
- **O tema vem primeiro (tema > gancho > formato).** Só entra tema que passa nas 4 perguntas da seção 3 do dossiê: promete ganho concreto (economia, tempo, velocidade, aparelho salvo, dinheiro)? Serve a qual público (aparelhos e vida prática, ou dev e IA)? Tem prova (do Luis ou de quem já fez)? A pessoa mandaria pra alguém sem a gente pedir (teste interno, nunca frase no roteiro)?
- **Dois tipos de vídeo:** transformação + continuação, para crescer em seguidores (ressuscitar aparelho, resolver problema da casa, economia); utilidade / ferramenta, para salvamento, comentário e lead (Claude Code, ferramentas de IA, Wi-Fi).
- **Não usar:** tema que fala só com um recorte ("quem foi mal no Enem"), tendência que não liga com o que o perfil entrega (GTA), conceito puro sem ganho concreto ("o que é skill"). Analogia da vida real (como o pão de queijo) ainda ajuda a explicar, mas nunca atrasa a dor nem o ganho.
- Série atual: **"30 dias, 30 experimentos com Claude"**. A série aparece só no selo (seção 4), nunca na fala nem numa cena.
- Formato: o Claude faz o motion, a legenda, a música e os efeitos, e monta junto o que é real: gravação de tela, aparelho na mão e o rosto do Luis (seção 5). Ícone explica, imagem real prova.
- **Voz: o Luis sempre manda o áudio pronto** (ElevenLabs com a voz dele clonada, ou gravação de celular), anexado na conversa, junto com o texto aprovado do roteiro. **As gravações de tela, do aparelho e do rosto também vêm dele, junto com o áudio.** O Claude nunca gera nem clona voz. Todo roteiro sai pronto para os dois jeitos (texto para gravar e texto para a IA de voz). Com o arquivo em mãos, não pergunte "gravada ou IA"; só pergunte se o áudio ou a gravação da prova não vier.
- Mascote: rato de laboratório branco **de brinquedo**, com cara de impresso em 3D (4 cores de filamento), estilo miniatura de desenho animado antigo. O avatar do perfil é esse rato.
- Nunca revelar que algum cenário foi gerado por IA.
- Inspiração de ritmo: canal Sanji Chien (cortes ~3,7 s, ~190 palavras/min, zero silêncio vazio). Inspiração, nunca cópia.

## 2. Regras invioláveis

1. **Nada sobrepõe nada.** Palavras do Luis: "Não coloque elementos para sobrescrever elementos." Nenhum elemento fica em cima de outro, da frase fixa do topo ou da legenda, nem confete ou partículas sobre texto. Exceções: uma transição breve, e o recorte em que a cabeça do Luis sai do card e a prova acontece atrás (dossiê 8.6).
2. **Nunca inventar exemplos.** Mostre o que existe de verdade: o arquivo real, o print real, a música realmente usada. Se precisar de um exemplo, baixe o real.
3. **Só música e efeitos próprios ou gratuitos com licença.** Padrão do Dia 10 v3: trilha e efeitos sintetizados no próprio vídeo com `motor/synth.py` (sem banco de efeitos genérico). Quando o Luis manda uma faixa, ela é remontada por trechos (exemplo no Dia 11). Faixa baixada: Mixkit direto por `https://assets.mixkit.co/music/<ID>/<ID>.mp3`, medida com `motor/voz/medir-musica.py`, crédito em `producoes/diaNN/CREDITOS.txt`. Pixabay bloqueia download automático. Nunca uma trilha "padrão de IA".
4. Sem marcas registradas em prompts de imagem (ex.: LEGO vira "blocos de montar"), sem Star Wars e sem plágio.
5. **Ícone do Claude:**
   - Aparece só quando "Claude" é falado (ou "ele", referindo-se ao Claude). No resto do tempo fica oculto ou num canto, sem cobrir nada.
   - Use o ícone oficial (o desenho `CLAUDE_PATH` de `motor/icons.js`), nunca um genérico. **Toda vez que "Claude" é falado, a logo aparece** (inclusive na chamada final): as pessoas batem o olho e reconhecem. A palavra "Claude" vai em Instrument Serif itálico laranja, e a transição de slime que chega nela também é laranja (nunca vermelha).
   - **A palavra vira a logo (Dia 10 v3):** "Claude" escrito se transforma, girando e de forma orgânica, na logo laranja (~0,1 s depois da fala, ~0,28 s de transformação). Palavra e logo nunca competem, e a logo nunca fica escondida. Só a palavra "Claude" faz isso ("Code" não).
   - **Outras ferramentas com a cara oficial delas:** falou GitHub, aparece a logo do GitHub, a tipografia e um formato que lembre o GitHub (estrelas no amarelo-ouro característico dele). Vale para qualquer marca citada: logo oficial (desenho vetorial em `motor/icons.js`; acrescente lá a que faltar), nunca caixa genérica com o nome escrito.
   - Em "foi o Claude", ele entra forte. No carimbo "ESCRITO PELO CLAUDE", ele **tomba**.
6. **Só os elementos que estão sendo falados naquele momento.** Muita informação no frame faz a pessoa rolar a tela. Exceção: as três camadas fixas (frase-tema no topo, selo e legenda embaixo) ficam o tempo todo (seção 4).
7. **Nenhuma tela parada.** Cenas ligadas por transições de câmera com rastro, da esquerda para a direita. Nunca mais de ~1 s sem movimento relevante, e nenhuma tela quase igual por mais de ~2,5 s (no Dia 5 o chat ficou 4 a 5 s parado).
8. **Respeitar a área útil** das plataformas (seção 4).
9. **Aprovação antes de renderizar:** roteiro aprovado e storyboard estático (imagens) aprovado. Nunca amostra animada nem teste de animação. **Sem aprovação, não renderiza.** A única exceção é quando o Luis avisa antes que vai estar ausente e quer receber pronto.
10. **Estratégia é segredo da casa.** Palavras do Luis: "A gente usa, mas a gente não revela." Nunca explique na fala, na tela ou nas legendas do post as táticas do canal: a barra dinâmica, a curva de retenção, a fórmula dos ganchos e loops, a chuva de dopamina.
11. **O que se borra na tela (Luis, 21/11/2026):** código real pode aparecer legível (terminal rodando é prova). Sempre borrados: prompts internos, chaves, dados pessoais e o conteúdo das skills, além do changelog e dos arquivos internos do canal. Números reais aparecem.
12. **Rosto sim, dados não (Luis, 21/11/2026).** O rosto do Luis entra na abertura e na reação (dossiê, seções 5, 8 e 9). O primeiro nome pode aparecer. Profissão, diploma, formação, e-mail e outros dados pessoais ficam fora da fala e da tela; saudações de tela sem nome completo e avatares de quem comenta genéricos. A foto de perfil do canal (`motor/perfil.jpg`) aparece **em todos os vídeos** (no mínimo no "segue o cobaia" da chamada final, com "@cobaia.dev" logo abaixo), nas capas e no site. Moldura branca redonda com o "+" **por cima da moldura**, nunca coberto pelo leque.
13. **Vídeo em loop.** O último frame emenda no primeiro.
14. **Verde só para o que é positivo:** acertou, certinhos do gabarito, grátis, R$ 0, dinheiro. "Nota máxima" e destaques de ênfase continuam vermelhos.
15. **Laranja é do Claude.** O laranja (`--or`) só aparece no ícone do Claude, na palavra "Claude" e no brilho dele. Nenhuma cena pode ser dominada por laranja, amarelo, azul ou verde: o vídeo é preto, off-white e vermelho (com fundo vermelho permitido nas inversões de ritmo), e cores de terceiros ficam dentro das telas. Exceção: o roxo escuro da chamada final padrão (seção 7).
16. **Cada vídeo nasce do zero (pedido do Luis em 20/11/2026).** Palavras dele: "Todo vídeo que você fizer, eu quero que você esquece totalmente como é que você fez o vídeo anterior e cria algo totalmente novo, dinâmico e orgânico." O Dia 13 v1 foi recusado por repetir elementos dos vídeos anteriores. Antes de desenhar as cenas, esqueça como os outros vídeos foram montados e invente tudo a partir do roteiro do dia:
   - gancho, metáforas visuais, cenas, transições e movimentos de câmera novos, tirados do que a fala diz (ex.: "0% de IA" vira uma lupa varrendo o texto sem achar vestígio e o carimbo de aprovado, não um velocímetro);
   - música em estilo novo a cada vídeo (nunca repetir gênero, timbre ou progressão do vídeo anterior; o Luis chamou a repetida de "batida") e efeitos novos;
   - o que continua igual é só a identidade (paleta, fontes, regras desta seção, logo do Claude, selo da série, chamada final e roxo do loop). O Dia 10 v3 é referência de nível de acabamento, não molde de cenas.
   - **A vinheta do calendário foi revogada (Dossiê Cobaia 2.0, 21/11/2026):** nada de "Dia N de trinta" na fala nem cena de calendário depois do gancho. Em 5 de 5 vídeos medidos ela perdeu de 8 a 17 pontos de retenção em 2 a 3 s. A série aparece só no selo fixo (seção 4).

## 3. Identidade visual

O Dia 10 v3 (`referencia/dia10-v3/`) é a referência viva: tudo é desenhado em canvas pelo motor (`motor/lib.js`) com as cores abaixo. Para mudar a identidade, mude o motor e a skill, nunca só dentro de um vídeo. Troca de paleta pontual (como o Dia 11 em tons de GTA VI) só quando o Luis pedir para aquele vídeo; o exemplo está em `exemplos/dia11-paleta-gta/`.

| Token | Cor | Uso |
|---|---|---|
| `--bk` | `#0C0C0C` | fundo |
| `--ow` | `#F2EEE6` | off-white, texto |
| `--rd` | `#FF2D2D` | vermelho da marca, destaque |
| `--or` | `#D97757` | laranja do Claude, só no ícone e no brilho dele |
| `--gr` | `#22C55E` | só em "grátis" e dinheiro |

- **Fundo de todo frame:** no Dia 10 v3 é chapado e alterna no ritmo entre preto (B), vermelho (R) e off-white (O) (tabela `FL` e `MODES` no `d10.html`), com vinheta radial e grão leve (`grain` do `lib.js`). Versão antiga, para cartões e telas: gradiente radial escuro, grade de pontos rolando devagar, 2 blobs desfocados (vermelho .20, off-white .07), vinheta e grão muito leve (.03; chiado forte parece vídeo sem definição).
- **Tipografia** (`motor/fonts.css` e `motor/fonts/`, OFL), variando entre cenas porque o Luis não quer tipografia engessada: Anton (impacto, selo, carimbos), Inter 500 a 900 (textos, legendas, cartões), JetBrains Mono (UI, arquivos, handle, contadores), Instrument Serif itálico (emoção e pergunta: "foi o", "amanhã..."), Permanent Marker (anotação à mão), Press Start 2P (jogo). Palavra-chave em vermelho, o resto em off-white.
- **Liquid Glass** (aprovado em 09/11/2026): vale para o site e para cartões de vidro quando o vídeo pedir (miolo desfocado, borda fina funcionando como lupa, reflexo em diagonal, nunca cinza fosco, nunca `backdrop-filter` no pai). O Dia 10 v3 usa cartões flat (`#1D1D21`) com o contorno em leque.
- **Peças do motor:** mola (`spring`), texto com mola (`springText`), grão, ruído suave, retângulo arredondado (`rr`); no `d10.html`: palavras grandes com transformação em slime, leque de 3 vermelhos (`FAN`), elemento vermelho que vira bola e viaja, logo do Claude girando, chamada final, tela roxa e loop. Lista em `motor/LEIAME.md`.
- **Glitch** sempre em neon (cópias deslocadas e barras ciano `#00F0FF` e magenta `#FF2BD6`, com brilho), nunca nas cores das letras, senão parece texto riscado.
- **Desenho:** nada que lembre forma fálica (nada de dedo solitário com unha). Mão é mão aberta, cinco dedos, sem unhas.

## 4. Layout: 1080×1920, 30 fps

**Três camadas em todo quadro (dossiê 8.2):** no topo a frase-tema fixa (para quem entra no meio entender do que é o vídeo), no meio a imagem (flat, 3D, gravação de tela ou o Luis) e embaixo a legenda acompanhando a fala (para quem assiste sem som). A palavra grande animada pode continuar como destaque, mas nunca no lugar da frase fixa nem da legenda. As medidas exatas da frase fixa e da legenda vão no storyboard do primeiro vídeo nesse layout, para o Luis aprovar, e depois entram nesta tabela.

| Zona | Coordenadas |
|---|---|
| Topo da plataforma | y < 200: nada importante |
| Cabeçalho próprio | barra, selo e handle (abaixo) |
| **Frase-tema fixa** | logo abaixo do cabeçalho, inteira desde o quadro 0 |
| **Imagem** | x 90–940, entre a frase fixa e a legenda |
| **Legenda** | embaixo, largura 850, terminando acima de y 1536 |
| Área segura | nada importante nos 20% de baixo (y > 1536) nem na lateral direita (x > 940) |

- **Barra de progresso:** x 90–940, top 212, 12 px, cantos 6, trilho `rgba(242,238,230,.13)`, vermelho com glow. **Barra dinâmica:** `largura = 850 · (1 − e^(−K·u)) / (1 − e^(−K))`, `u = t/T`, `K = ln 25`, presa entre 0 e 850. Enche rápido no começo e quase para no fim, porque aí a pessoa já está presa.
- **Selo da série** "DIA NN/30 · experimentos com Claude": pequeno e fixo do primeiro ao último quadro, sem cena própria e sem pop ligado à fala (dossiê 5.2 e 8.9). Pílula vermelha (left 90, top 246). **Handle** "@cobaia.dev": Mono 700 30 px `#bdbdbd` (right 140, top 253).

**Legenda (obrigatória em todo quadro com fala, dossiê 8.2):**
- Inter 800 46 px, centradas, palavra ativa com sublinhado vermelho; as outras com opacidade .8 e sombra escura. Blocos curtos sincronizados palavra a palavra.
- **Nunca some**, nem quando a palavra grande ou um título falado está na tela.
- **Sem piscadas:** nenhum bloco fica menos de ~0,3 s na tela fora da fala real.

## 5. Movimento e transições

### 5.0 Estética de motion aprovada (16/11/2026, vale para todo vídeo)
Referência aprovada: teste "07 · Síntese" (`estudos/sintese-07/`, na versão com a identidade nova). Palavras do Luis: "Essa é a estética que eu quero nos próximos vídeos daqui pra frente." Não precisa repetir a mesma ordem de cores, cenas ou fontes; pode trazer algo a mais mantendo essa identidade.
- **O vídeo conta o que está sendo falado, literalmente:** cada fala vira a coisa de verdade na tela ("plano" abre um plano com checklist, "código" abre um terminal com código, "ganha vida" vira um app rodando), não só o lettering.
- **Cada roteiro pede a sua dinâmica.** Nada de ordem fixa de animações: o vídeo é fluido e está sempre em movimento. As regras abaixo são o padrão de qualidade, não um roteiro de cenas.
- **Gancho (0 a 3 s), regras do dossiê (seção 4):** no primeiro quadro, a frase do gancho aparece **inteira**, grande e fixa (nunca uma palavra por vez), junto com o objeto em conflito ou o resultado com número (aparelho indo pro lixo, tablet num caixão, teste marcando 250 de 500 Mega, detector marcando 0% de IA). Nenhum quadro vazio, nenhuma abertura só com paisagem ou logo. Promessa falada sem a imagem do problema não conta como gancho. Cena 3D com história funciona na abertura; do meio pra frente, tela real.
- **Gancho é o trecho mais denso do vídeo:** mais dinâmico, mais efeitos, mais entrega e dopamina. Uma coisa nova por segundo; no segundo 2 a cena já mudou. Exemplo do Luis (Dia 09, "foi mal no Enem"): s1 prova do Enem minimalista sendo marcada e a nota caindo com números rolando rápido; s2 a prova vira uma caneta vermelha que escreve uma página num caderno branco pautado com espiral, rabisca, desenha, risca e reescreve; s3–4 a caneta vira uma nota 1000 gigante que encolhe e pousa na prova como nota escrita à mão, sublinhada como correção, com o gabarito cheio de certinhos verdes.
- **Um único elemento vermelho do começo ao fim (Dia 10 v3):** o destaque vermelho de cada cena é sempre o mesmo personagem. Palavras do Luis: "o elemento de destaque da cena anterior é deformado e comprimido até virar uma bola, e dessa bola ele se transforma no próximo elemento, sempre de forma orgânica." Nunca animação padrão ou engessada.
  - Passagem: comprime em bola (~0,16 s) e **deixa o lugar vazio**; a bola viaja em arco com uma voltinha (oscila, estica na velocidade, rastro e respingos); chegando, abre no destaque novo com mola. **A cena se monta ao redor dela**: é a bola que dá o start da construção.
  - Antes do storyboard, escreva a corrente "veio de → vira" batida por batida. Dia 10: ponto do Wi-Fi → play → caneta no calendário → seta → sinal de atenção → cursor do prompt → escrita do Claude Code → logo → lupa → ponteiro → lupa → cereja → casa → bola da briga → seta 6→11 → ponteiro → carregando → Wi-Fi → + de seguir → coração → base do Wi-Fi → ralo → roxo sem bola → loop.
  - Em fundo vermelho, o destaque troca de cor (off-white ou preto).
- **O elemento da cena anterior constrói a próxima** (fluidez): o contorno traça a nova forma (pontos com mola e atraso ao longo da linha) e o preenchimento chega logo depois.
- **Contorno em leque de 3 vermelhos:** pelo menos 3 contornos (vermelho vivo, médio e opaco), cada um num tempo e velocidade diferentes, formando um espectro/leque até assentarem na forma e sumirem. A abertura (a quebra) do contorno fica no **canto inferior esquerdo**, nunca em cima.
- **Contorno rente ao elemento**: segue exatamente a forma de baixo. Card arredondado → mesmo raio (nunca quadrado); estrela → colado na estrela. Gerar os pontos da forma real.
- **O contorno não fica parado na tela**: monta a forma e some (~1 s depois). Volta só para construir a próxima coisa.
- **Alternar janela e cena, nunca caixa-caixa-caixa:** o card/quadrado é só para janela de app ou quando é mesmo necessário. Intercale com cenas livres, ilustradas, sem caixa (um caminho, um mapa, um personagem). Card → cena → outra cena → card, por exemplo.
- **Ícone explica, imagem real prova (dossiê 8.3):** o flat desenha a ideia. Na hora da prova entra a coisa real: tela real, terminal rodando, aparelho na mão, ou a tela de quem já fez quando o resultado é de referência. Se o vídeo for de referência e o Luis não tiver gravação, vale uma **reprodução fiel da tela real, com os números reais do resultado** (Luis, 21/11/2026). Proibido: ícone abstrato no lugar da prova.
- **Número na hora da prova**, em contador animado e com destaque (0,08 s, 8h30, 474 Mega).
- **Explicar em flat minimalista (fora da prova):** prova do Enem = folha de prova de verdade, simplificada; mapa = papel que se desdobra e vira mapa tradicional com rotas, depois a bolinha entra nele e quica até uma bifurcação (um lado sem saída, outro no objetivo, com certo e errado); exercícios = lista estilo prova, um embaixo do outro, rolando, com opções A/B/C em barras arredondadas; professor = bonequinho minimalista com quadro, terno e gravata vermelha (chapéu de formatura não é professor).
- **Ligar duas coisas é uma animação, não uma caixa:** ex.: "ligo ele no Claude" = logo do GitHub com o repositório embaixo, a bolinha faz zigue-zague e encaixa na logo do Claude, e a ligação entre os dois aparece.
- **Números que caem:** nota ou valor diminuindo com dígitos rolando bem rápido (estilo caça-níquel).
- **Grafo de conhecimento** com partículas, e a linha vermelha ganha neon quando conecta.
- **Neon só se for neon de verdade** (bem vivo, brilho forte). Se não ficar convincente, sem neon.
- **Perspectiva leve** nas telas e cartões (rotação de 5 a 7°, nunca exagerada), mantendo a identidade.
- **Física de mola** (overshoot e assentamento), bolinha que quica com sombra no chão e squash no contato.
- **Fundo e tipografia invertendo no ritmo** (preto, vermelho, off-white) nos momentos de ênfase; o vídeo nunca fica estático.
- **Textura jateada/granulada** (como tinta borrifada): alternar contornos nítidos (em repouso, no contato) com contornos esfumaçados (em movimento). Nunca deixar um elemento só borrado, que parece baixa qualidade.
- **Palavras grandes como destaque, depois do gancho:** uma palavra ou frase curta por vez, bem grande, com a palavra falada acesa (karaokê) e a palavra-chave em vermelho. Nunca no gancho (lá a frase entra inteira) e nunca no lugar da frase fixa do topo nem da legenda. **Várias fontes** alternando (Anton, Instrument Serif itálico, Inter 900, JetBrains Mono); nunca o vídeo todo numa fonte só, e nada de título final em fonte tipo Helvética.
- **Duas fontes na mesma frase** quando ajuda: "de 30" numa fonte e "experimentos" em outra, vermelho; "com" na fonte da frase e "Claude" em serif laranja.
- **Cada fonte tem a sua animação de entrada** (não é sempre a mesma): a mono (código) é digitada, com o elemento vermelho virando o cursor; a serif acende; a Anton bate com peso; etc.
- **Uma palavra se transforma na outra como slime:** transição orgânica, sutil e rápida (~0,15 a 0,2 s, desfoque + limiar), nunca palavra que só surge.
- **HUD de ficha técnica** discreto (rótulos nos cantos, contador de tempo, marcador de batida) e uma interação por batida nos trechos de demonstração.
- **Cor oficial: vermelho** (`--rd`); verde só no que é positivo (regra 14).
- **Área segura e desfoque de lente:** o principal fica dentro da área de conteúdo (seção 4). Elementos podem passar para a borda, mas tudo o que sai da área segura ganha desfoque progressivo: leve perto dela e bem borrado na borda do vídeo, como lente. Pode ter uma distorção de luz sutil (tipo glassmorphism), sem chamar atenção.
- **Ritmo agitado**, com batida que mantém o vídeo vivo.

- **Sincronia:** cada palavra-chave dispara um evento visual no tempo dela (`k.T(i)`), com 0,05 a 0,15 s de antecipação.
- **Desfoque sempre rápido e sutil:** até ~5 px e até 0,15 s. Texto nunca fica borrado parado.
- **Número exagerado:** contador gigante rolando do zero que trava com tremida e "+" vermelho quando a fala diz "mais de" .
- **Dinheiro ou grátis:** selo verde, estouro de "$" e som `caixa`.
- **Surgimento de texto:** nada de palavra solta com pop. Varie por cena: saindo do desfoque , serif acendendo de cinza , número rolando atrás de máscara. Título pousado fica parado.
- **Entradas:** back-out com overshoot para pops, cúbica para deslizes, escala 0.5→1 com leve `rotateY(-40→0)`.
- **Pulso no beat** só nos compassos com bumbo; desligado em silêncios dramáticos.
- **Tremor** em impactos (8 a 40 px, decaindo). **Flash** branco curto (≤ 0,5, 0,12 a 0,25 s) só em impactos grandes.
- **Partículas** com sementes fixas, sempre atrás do conteúdo (canvas `#fx` antes da câmera). Perto de texto, escala pequena e origem no próprio objeto.
- **X de "errado":** selo redondo vermelho ao lado do elemento , nunca riscado por cima.
- **Telas (gravação real ou reprodução fiel):** a prova usa a gravação que o Luis manda. Sem gravação, só em vídeo de referência, a reprodução fiel da tela real com os números reais. Para as telas:
  - Só o conteúdo da tela, cantos levemente arredondados e sombra, **sem moldura** de monitor ou celular falso. Parece gravação de tela editada.
  - Entram giradas (rotateY 25 a 40°, escala .8) e assentam inclinadas (±6 a 8°).
  - **Zoom inclinado no ponto falado:** a cada clique ou detalhe, a tela inteira corre e inclina até o ponto (`foco()`, ~0,4 s). **Raramente a tela inteira**, só quando o assunto é geral. Anime a escala do contêiner, nunca amplie bitmap pequeno.
  - **Zoom na ênfase (pedido do Luis em 11/11):** onde a fala dá ênfase ou mostra algo, a câmera dá zoom nesse ponto, e os frames de aprovação já mostram esse zoom. Em demonstração de sistema ou app (vários apps abrindo, teste de velocidade, player), o zoom é **leve** (1,15 a 1,35x) e **acompanha o mouse**.
  - **Antes e depois lado a lado:** em comparação de velocidade, tela dividida com o jeito antigo travando (carregando, erro, fechando) e o novo abrindo na hora, cada lado com seu cronômetro.
  - **Cursor branco** guiando tudo o que é falado: vai até o item e clica com leve encolhida.
  - Pedido digitado no ritmo da fala, palavras-chave em vermelho; a legenda continua embaixo.
  - Em reprodução, fiel à tela real e aos números reais; fora da prova, telas de apoio podem ser genéricas.
  - **Cliques em sequência** (ex.: "Cancelar inscrição"): botão vermelho com texto branco; o cursor clica num, desce, clica no próximo; cada linha clicada vira "✓ Cancelada" e some; o zoom acompanha cada clique.
- **Gancho desde o frame 0**, sem fade do preto: o quadro 0 já tem a frase inteira e a imagem concreta, e o loop volta para esse quadro completo.
- **Nunca "parte 2":** cada episódio se sustenta sozinho, com uma promessa nova (o Dia 07, continuação do notebook, teve 0,5% de envio e 44,9% de pulo).
- Pode acelerar a voz se ajudar no ritmo (seção 9).
- **Rosto do Luis em dois momentos (dossiê 5.6 e 8.6):** na abertura e na reação, com o recorte em que a cabeça dele sai do card e a prova acontece atrás. A reação entra curta (até ~3 s), em vertical 1080×1920, podendo acelerar até 1,15x. Antes de usar, confira quadro a quadro e borre o que for sensível (nome de Wi-Fi, IPs, nomes, e-mails). Direção de gravação: `formatos/face-cam/regras.md`.

## 6. Cenas aprovadas (referência de nível)

**Referência de formato (o que os dados provaram):** Dia 06 (notebook velho: cena 3D + tela real + reação real, 31,7% de pulo, 27 s, 3,2% de seguidores) e Dia 08 (tablet morto: cena 3D + tela real, 29,5% de pulo, 28 s). Os dois vídeos valem só como formato; a identidade antiga deles não volta.

Referência de acabamento do motion: Dia 10 v3 (`referencia/dia10-v3/postar/cobaia-dia10-final-leve.mp4`, fonte em `referencia/dia10-v3/fonte/`). A estrutura dele está superada: a vinheta, o gancho palavra por palavra e o pedido de envio ("Sabe aquela pessoa... Ela precisa saber disso") não são modelo. Também na nova estética: Dia 9 (`referencia/dia09/`) e o teste "07 · Síntese" (`estudos/sintese-07/`). Ela mostra o nível de qualidade, não um molde: as cenas de cada vídeo são inventadas do zero a partir do roteiro (seção 2, regra 16), e nunca se repete exemplo, app, cena ou música de um vídeo anterior. Temas já usados nos Dias 1 a 11 estão no `CLAUDE.md`.

## 7. Chamada final e material de quem comenta

**Chamada final padrão (atualizada em 17/11/2026):** a chamada ainda é o vídeo: mesmo estilo (preto, vermelho e branco), e o elemento vermelho continua construindo as cenas.
0. **CTA curto (dossiê 5.7):** "Segue o Cobaia, curte e comenta PALAVRA". **Nunca pedir pra mandar o vídeo** ("sabe aquela pessoa que...", "manda pra..."): os dois vídeos mais enviados não pediram.
1. **"Segue o cobaia":** foto de perfil do canal (`motor/perfil.jpg`) com **"@cobaia.dev" logo embaixo** (nunca escondido no rodapé). Botão "+" como no TikTok: o cursor vai e clica (ou aparece o clique), o ícone vibra e vira ✓.
2. **"Curte":** a foto com o ✓ desliza para a esquerda; à direita, o coração cresce com pop de bolha e fica curtido.
3. **"Comenta PALAVRA":** abre uma caixa de comentário, a palavra é digitada e enviada; depois aparece embaixo o card do material ("guia completo").
4. **Card final sem fala (~2 s):** corte seco para a tela roxa escura (`#0B0820`), clique e nota de vidro, "comenta" em Inter e a PALAVRA em Instrument Serif itálico acesa (neon só se for vivo de verdade), **e a prévia do próximo episódio** ("amanhã: dia 16, o tablet no Android 11"). É o motivo pra seguir (dossiê 5.8 e 8.7). **Mantenha sempre uns 3 temas aprovados à frente**, para o card nunca travar (Luis, 21/11/2026).
5. **Loop:** a bolinha volta para a posição do primeiro frame, emendando no começo.
- Se "Claude" é falado na chamada, a logo do Claude aparece.
- Fala: "Segue o Cobaia, curte e comenta PALAVRA." Sem pergunta antes e sem frase de envio.
- Animação: avatar 330 px centralizado com "+" que vira ✓ e fogos; coração branco que fica vermelho; só o campo de comentário em vidro digitando a palavra; cartão da mensagem com o material; no fim, "COMENTA / PALAVRA" gigante. Só o elemento que está sendo falado. Nunca print ou réplica da tela do TikTok.
- Cada dia tem uma palavra-chave diferente (lista em `roteiro/temas.md`). Sem palavra-chave, pergunta aberta, nunca sim/não.
- **Entrega do material:** cada palavra-chave tem uma página no site (`cobaia-dev.vercel.app/<palavra>`). **Instagram:** o ManyChat responde os comentários novos com a DM, com a regra de seguir para receber, e o Sentinela cuida dos comentários atrasados. **TikTok:** o comentário fixado pede DM com a palavra-chave (a automação lá ainda está sendo confirmada pelo Luis). Entregue sempre a mensagem de DM com o **link sozinho numa linha** (a prévia vira o botão).
- **Página no ar antes de postar (dossiê, seção 10):** nenhum vídeo com potencial de estouro sai sem a página do que a pessoa recebe, e do que pode comprar, já no ar. Produtos que existem hoje: guia do tablet (R$ 27,90) e mentoria de casos reais; o guia do notebook (R$ 49,90) está planejado. Nos outros temas, por enquanto, só o material grátis. Não invente produto nem preço.
- **PDF só quando o Luis pedir.** Palavras dele: "esse pdf deve ser solicitado, enquanto não for solicitado não produza, pois posso pedir alterações nos vídeos". O roteiro pode prometer o material; a página do site leva o guia.
- Pedido extra de engajamento só quando o Luis pedir (custa segundos).

## 8. Roteiro e textos do post

- **Tema antes de tudo:** passa nas 4 perguntas (seção 1) antes de escrever uma linha.
- **Gancho (dossiê, seção 4):** começa pelo ganho ou pela dor de quem assiste, nunca pelo contexto do criador ("vocês lotaram meus comentários") nem por "hoje eu vou mostrar". Fala com todo mundo que tem o problema. **Afirma, não pergunta** (nada de "O que acontece quando..."). A frase falada é a mesma que aparece inteira no quadro 0, junto com a imagem do problema. O banco de ganchos virais (`roteiro/banco-ganchos-virais.md`) e a pesquisa de canais de fora são fonte de ideia; quem decide são o dossiê e os dados do canal. Formato, ângulo e edição continuam sem pergunta ao Luis: decidem o dossiê, depois a pesquisa.
- **Estrutura do experimento (dossiê, seção 5), nesta ordem:**
  1. Gancho com conflito (0 a 3 s).
  2. Série só no selo visual, sem fala e sem cena.
  3. A dor real, com número, antes dos 7 s. O ganho vem antes de qualquer contexto ("um dev publicou no GitHub..." perde gente).
  4. A virada: "aí eu chamei o Claude".
  5. De três a quatro provas, cada uma com número e imagem real, numa escada em que cada prova impressiona mais que a anterior.
  6. O momento humano: a reação real do Luis, de rosto.
  7. CTA curto: "Segue o Cobaia, curte e comenta X". Sem pedir pra mandar o vídeo.
  8. Card final com o próximo episódio.
- **Episódio de série:** cada um se sustenta sozinho, com uma promessa nova. Nunca "parte 2".
- **Quadro de novidades** (IA, Claude, ferramentas novas): de rosto, de 20 a 35 s, caminhando. A novidade nunca é o assunto: o assunto é o que muda na vida da pessoa. Ordem: gancho com o que muda pra pessoa; o que é, numa frase de leigo; um exemplo do dia a dia com antes e depois; como usar hoje e se é de graça; a dica que faz funcionar; CTA padrão. Postar no dia do lançamento e confirmar tudo na fonte oficial antes de gravar.
- **Copo meio cheio (dossiê, seção 7):** mostrar o que deu certo; o que não funcionou não entra. **Nunca prometer o que a ferramenta não faz.** Limitação que a pessoa vai encontrar logo de cara entra como "a dica que faz funcionar", em tom positivo ("funciona até no grátis, só liga essa opção aqui"). Confira na documentação o que o recurso faz antes de prometer.
- **Vida real, não conceito:** "eu não falo sobre o tema, eu falo sobre a vida das pessoas com o tema". No máximo uma metáfora, e ela nunca vem antes da dor e do ganho.
- **No máximo 59 segundos** (dossiê: 58 a 59 s), bem prático, narração animada e em alto astral, termos técnicos pontuais com cara de especialista e linguagem que um leigo entende. Se não couber, corte frase de enchimento em vez de acelerar mais; a faixa de palavras se ajusta pelo tempo real da voz.
- **Não repetir exemplos nem apps de vídeos anteriores** (Gmail e Agenda já foram no Dia 4; Canva no Dia 5).
- **Sem fórmula:** nada de "o truque" ou "o segredo" em todo vídeo. Loop aberto, mito e quebra só quando cabem.
- **Sem palavra repetida** na mesma frase nem na seguinte (fora o tema e "Claude"). Rode uma checagem de repetição antes de entregar. Vetado: "Todo mundo tá falando de skill no Claude. E tá todo mundo complicando." Evite abrir de novo com negação (Dia 1 "Ninguém...", Dia 2 "Eu não...").
- **Senioridade:** nunca "eu não escrevi", "eu não fiz" ou "eu não sei", que fazem o Luis parecer leigo. Use "você não precisa fazer isso: o próprio Claude faz (ou ajuda)". Quando ele entrega um arquivo ou prompt grande, ele diz que fez, e que a pessoa não precisa de um desse tamanho porque o Claude ajuda a montar o dela.
- **Valor do perfil:** o Luis deixa simples o que outros vendem em curso pago ou explicam em vídeo longo. Isso aparece pela clareza, sem virar bordão. Se citar curso pago, confira antes que ele existe.
- **Próximo episódio no card final (obrigatório):** uma linha afirmativa com o ganho do próximo dia ("amanhã: dia 16, o tablet no Android 11"). Ele trava a ordem dos temas: mantenha uns 3 temas aprovados à frente e, se o Luis quiser trocar o próximo, ajuste antes de fechar o vídeo.
- **Motion junto com o roteiro:** cada frase tem um evento visual forte, com transição e som.
- **Humanizer sempre:** todo roteiro e todo plano de roteiro passam pela skill `humanizer` antes de ir para o Luis.
- **Um roteiro por vez**, do próximo dia. Quando o dia depende de um teste, o texto final só sai com o resultado na mão.
- **Entrega do roteiro:** texto para o Luis gravar e texto para a IA de voz (sem tags, ou com tags animadas como [excited], [curious], [laughs]; nada de tom baixo astral; fala enérgica e para cima, com frases curtas, exclamações e as palavras de ênfase em MAIÚSCULAS, porque o Luis achou a voz calma demais no Dia 13; a sigla "IA" se escreve "í-á" ou "inteligência artificial", porque o ElevenLabs v3 lê "IA" como "A-I-E"), mais "Como gravar", "Onde estão os gatilhos" e "O que vai aparecer na tela" (Fala | Na tela | De onde vem a peça | Transição e som).
- **Textos de postagem do dia num único pedido:** legendas das 3 redes e comentário fixado.
  - **Instagram:** postar à mão pelo celular, às 17h, sem agendar. 1ª linha é um segundo gancho com emoji; 3 a 5 linhas que ensinam; "comenta PALAVRA"; 5 hashtags (1 grande, 2 médias, 2 de nicho). Comentário fixado com uma pergunta sobre o aparelho ou a situação da pessoa ("Qual o modelo do seu notebook?").
  - **TikTok:** o mesmo vídeo, sem re-renderizar. Legenda com as palavras que a pessoa digitaria na busca, 1 ou 2 linhas e 3 a 5 hashtags. O CTA vai no comentário fixado: "Quer o passo a passo? Me manda [PALAVRA] no direct 🚀". Quando o link da bio for liberado: "o link tá na bio".
  - **YouTube Shorts:** subir todo vídeo, pelo celular. Título com resultado, objeto e conflito, em até ~60 caracteres (modelo: "A Samsung matou esse tablet em 2017 (mas eu ressuscitei com IA)"), 2 linhas, "Inscreva-se: amanhã sai o Dia N+1" com o motivo, 2 ou 3 hashtags. Comentário fixado: pedido de inscrição com motivo.
  - Modelo completo: `roteiro/modelo-textos-postagem.md`.
  - Hashtags: grandes #inteligenciaartificial #ia #tecnologia; médias #claudeai #produtividade #automacao #dicasdetecnologia; nicho #claude #anthropic #skills #claudecode #semprogramar.
  - Nunca explicam as táticas do vídeo.
- Roteiros e decisões ficam em `producoes/diaNN/` e no `roteiro/temas.md` (temas aprovados à frente).

## 9. Áudio

**Entrada:** o arquivo do Luis (mp3 ou wav) e o texto aprovado. Trabalhe sempre numa cópia (`producoes/diaNN/fonte/voz.*`). Receita completa, medida nos Dias 9 a 11, em `motor/voz/LEIAME.md`.

**Áudio do ElevenLabs (padrão dos Dias 9, 10 e 11):** entra no `aNN.py` como chegou: sem corte de silêncio, sem atempo e sem normalização antes. O `aNN.py` aplica highpass 80, EQ 3,5 kHz +1,5 dB e compressor −20 dB 2,5:1, o `mix()` iguala a voz pelo RMS e o `enc.sh` fecha em −14 LUFS. A voz começa no tempo 0 do vídeo. Palavras com tempo pelo `align.py` (texto aprovado + áudio).

**Gravação de celular:**
1. WAV 48 kHz. Transcrição com faster-whisper (`motor/voz/transcribe.py`: modelo small, cpu int8, `language="pt"`, tempos por palavra, `initial_prompt` com os termos do canal). Se o download do modelo for bloqueado na rede, use o alinhamento pelo texto (abaixo).
2. Corte de silêncios (`motor/voz/cut3.py`): limiar relativo ao ruído (−32 dB quando o fundo está em ~−40 dB), janelas de 10 ms, junta falas com intervalo < 0,12 s, margens de 0,05 s antes e 0,09 s depois, fades de 8 ms. **O fim de cada frase vem do envelope de energia**, não do fim da palavra do whisper: sílabas finais fracas ("grá-tis", "impor-tam") somem com limiar alto. Não comprima pausas de vírgula em listas.
3. Tratamento: `highpass=f=80, afftdn=nf=-30, equalizer 250 Hz −2 dB, equalizer 4 kHz +2 dB, acompressor thr −20 dB ratio 3, atempo (até ~1,18 em gravação limpa), loudnorm I=-16`.
4. **"Corrigindo":** quando o Luis erra, ele fala "corrigindo" e repete. Corte do início da tentativa errada até o fim de "corrigindo". Se gravar a mesma frase duas vezes, fique com a que bate com o roteiro.
5. Corrija a transcrição pelo roteiro antes das legendas (ex.: "chefe" → "chef", "Tropic" → "Anthropic", "a risca" → "à risca"). Pausas dramáticas ficam definidas à mão onde o roteiro pedir, e os tempos das palavras são recalculados depois do corte e da aceleração.
6. Confira por nova transcrição com prompt neutro (um prompt com a frase faz o whisper pular a frase). Se a transcrição longa cortar uma sílaba, confira numa janela curta antes de mexer no mix.
7. Regravação parcial: mantenha a voz aprovada até o ponto de troca e anexe a parte nova, cada parte em −16 LUFS. Se houver risco de diferença de timbre, peça para regravar inteiro.

**Sem whisper:** `motor/voz/align.py` alinha pelo texto do roteiro (frases pela pontuação, programação dinâmica por duração esperada de sílaba, palavras distribuídas por sílaba; ajuste a contagem de siglas como MCP). Foi o caminho do Dia 11. Em voz do ElevenLabs os tempos já são os do vídeo; o `motor/voz/cut.py` (corte + atempo) só entra em gravação. Gravação com "corrigindo" sem whisper: plano B no `motor/voz/LEIAME.md`.

Resultado dos dois caminhos: a voz tratada e as palavras com tempo, que viram os blocos de palavras grandes em `fonte/dNNchunks.js` (formato no `motor/LEIAME.md`).

**Música:**
- Animada, instrumental, sem voz, eletrônica com pegada (electro, drum & bass, future bass, tech house). **Música do primeiro ao último quadro** (no Dia 5 v1 metade ficou sem música).
- **Não repita a faixa de nenhum dos três dias anteriores.** Dias 3, 4 e 5 usaram "Cat Walk": os Dias 9 e 10 usaram trilha sintetizada no `synth.py` (house lo-fi); o Dia 11 usou a faixa enviada pelo Luis. Faixa nova entra no `CREDITOS.txt` do dia.
- **Trilha que acompanha a narrativa**, remontada compasso a compasso (lista `SEGS` no `aNN.py`, crossfade de 12 a 30 ms; ou sintetizada por trecho, como no `a10.py`): drop no gancho; breakdown no problema do dia a dia e build depois; compasso de pausa + tape stop antes da virada e drop na palavra-chave; build na digitação e cheio no resultado; breakdown + riser até o drop na prova; cheio na chamada final. Ganho por trecho (breakdown +4,5 dB, build +2,5 dB), sempre em rampa, nunca em degrau (regra abaixo).
- Volume base −11 dB, ducking pela voz (até −55%, ataque 20 ms, release 280 ms), −20 dB em silêncio dramático, −10 dB em tensão. A voz fica ~17 dB acima. Nada abaixo de ~−40 dBFS (confira no relatório do `mix` do `synth.py`).

**Trilha dinâmica, mas suave (pedidos do Luis em 19/11/2026):** a música não pode ficar estática, numa linha reta do começo ao fim. Ela acompanha a narrativa e o motion: sobe nas revelações, baixa no problema, cresce até a chamada final. **Mas toda mudança é gradual.** O Luis reprovou a primeira tentativa (`motor/trilha.py`, Dia 12) porque ficou "cheia de degrau": trocava de música de uma vez e o volume pulava de baixo para alto num corte seco.
- Troca de trecho ou de instrumento: fade-out de um e fade-in do outro, nunca corte seco. **O fade combina com o vídeo:** dura o mesmo que a transição da cena (em geral 0,2 a 0,5 s, o tempo do voo da bola) e termina junto com ela. Fade longo (1 s ou mais) o Luis reprovou.
- Volume e filtro mudam em rampa curta, colada na transição da cena (0,2 a 0,5 s), nunca em degrau seco. Crescendo longo só em build (riser até um drop).
- Uma base musical só, que evolui (camadas entrando e saindo aos poucos, filtro abrindo e fechando). Não pular de uma música para outra.
- Silêncio ou parada só com fade curto na entrada e na saída, e só em momento forte do roteiro.
- **Clima sempre para cima (pedido do Luis em 20/11/2026):** a trilha avança junto com o texto e com o que o vídeo quer entregar, mas o clímax nunca cai para algo triste ou depressivo. Tom maior e progressão luminosa (Dia 13: F C Dm Bb); quando desce, desce pouco (no máximo uns −3 dB, filtro acima de ~2,4 kHz, acordes ainda tocando) e volta subindo de forma suave e orgânica. A respiração do acorde no bumbo (sidechain) ajuda a sensação orgânica. Exemplo: `producoes/dia13/fonte/a13.py`.
- **Modelo aprovado:** `producoes/dia12/fonte/a12.py` (tabela `ST`: estado das camadas, volume e filtro por cena, rampas de 0,3 s no corte, builds só antes de drop).
- `motor/trilha.py` não está aprovado como está: antes de reusar, suavize as transições (rampas e crossfades) e mande uma amostra de áudio para o Luis ouvir antes de montar no vídeo.

**Som do elemento vermelho:** squish na compressão, pluck no voo, pop com tink na abertura, **30% mais baixo que no Dia 10 v3** (×0,7, cerca de −3 dB).

**Efeitos que fogem do óbvio:** nada do whoosh, pop, ding e confete que todo vídeo com IA usa. Prefira sub_drop, reverse_swell, glass_chime, bloom, tape_whirl, tick_wood, power_down; e no visual, vinheta que respira na tensão, luz vazada na revelação, separação RGB na falha, linha de varredura, anel de onda e soco de zoom no drop.

**Efeitos ("chuva de dopamina"):** todos sincronizados com palavras ou eventos, gerados pelos instrumentos de foley do `motor/synth.py` (waterdrop, tink, glass, relay, keyclick, subdrop, swell, tapestop, pluck_bend etc.; lista no `motor/LEIAME.md`). As passagens alternam sons diferentes. Instrumento novo entra no `synth.py`, nunca solto dentro de um vídeo.

**Master:** `loudnorm I=-14 LUFS, TP=-1.2` (aplicado no `motor/enc.sh`).

## 10. Pipeline de produção

O passo a passo com comandos está no `CLAUDE.md`. Resumo:
1. `git pull` e leitura do `CHANGELOG.md`.
2. Tema aprovado pelas 4 perguntas e roteiro aprovado (seção 8); o Luis manda o áudio pronto (ElevenLabs ou celular) com o texto aprovado, mais as gravações de tela, do aparelho e do rosto.
3. `bash motor/novo-dia.sh NN` → `producoes/diaNN/` (fonte, postar e CREDITOS).
4. **Voz** (seção 9) → palavras com tempo → `fonte/dNNchunks.js` (palavras grandes: fonte por bloco, palavra-chave 1 = vermelho, 2 = "Claude" laranja, 3 = verde).
5. **Mapa da música:** medir a faixa (ou planejar a sintetizada) e escrever o mapa de trechos contra a fala (`mapa-musica.md`, modelo no Dia 11).
6. **Corrente do elemento vermelho:** tabela "veio de → vira" batida por batida (`corrente.md`, modelo no Dia 11).
7. **Cenas** no `fonte/dNN.html` em canvas, tudo função de `t` (sem `Date`, sem `Math.random` sem semente, sem CSS transition). `window.NFRAMES` e `window.ready` obrigatórios; `draw(t)` desenha o quadro.
8. **Storyboard estático** (com as três camadas visíveis em todos os quadros e a página do site em PR junto, para aprovação): `node ../../motor/storyboard.cjs dNN.html sb <tempos...>` e folha com `python3 ../../motor/folha.py sb storyboard.jpg`. Mande para aprovação. Não renderize sem aprovação (seção 2, regra 9).
9. **Render:** `node ../../motor/render-paralelo.cjs dNN.html frames I N` em N processos (ou `render.cjs` num só). Confira correções com o storyboard nos tempos alterados; o arquivo final sai de um render completo.
10. **Áudio:** `python3 aNN.py` gera o mix (trilha + foley + voz) com `motor/synth.py`. Som do elemento vermelho a ×0,7.
11. **Encode:** `bash ../../motor/enc.sh frames mix.wav ../postar/cobaia-diaNN-final.mp4` (x264 crf 17, yuv420p, AAC 256k, loudnorm −14 LUFS, TP −1,2). Leve (< 25 MB): `bash ../../motor/enc-leve.sh` (alvo `192000 ÷ duração − 160` kbps).
12. **Entrega em `producoes/diaNN/postar/`:** `cobaia-diaNN-final.mp4` (HQ), `cobaia-diaNN-final-leve.mp4`, `capa-diaNN.jpg` e `textos-postagem-diaNN.txt` (legendas das 3 redes, comentário fixado e DM). Os MP4 não vão para o git (ficam na pasta do projeto / Biblioteca); o resto vai.
    - **Cópia no PC (até o fim dos 30 dias):** a versão HQ vai para `C:\Users\Fernando\cobaia\diaNN\`. Sem ferramenta de transferência, avise o Luis para baixar.
13. **Capa 1080×1920 (identidade nova, 17/11):** gerador em `capas/capas.html` (`node shot_capas.cjs <saída>`; dia novo = entrada em `DAYS` + ilustração em `ILL`, e o número do dia na lista do `shot_capas.cjs`). Fundo preto com brilho vermelho e grão, HUD de cantos e barra de progresso da série; "DIA NN" Anton vermelho 132 px com "/30" apagado; gancho encurtado em duas linhas (serif itálico + Anton, palavra-chave vermelha, "Claude" laranja); cartão 900×700 com leque de 3 vermelhos e ilustração flat da coisa real, ponto vermelho guiando o olho; rodapé com foto + "+", "@cobaia.dev" e "comenta PALAVRA" em pílula vermelha. Tudo entre y 240 e 1680. Destaque do Instagram: ícone grande no círculo central com leque circular (`destaque(kind)`).
14. **Site (obrigatório, no ar antes de postar):** sempre que um vídeo for criado ou editado, atualize a página da palavra-chave e o calendário em cobaia-dev.vercel.app (repo `luisalves23/cobaia-site`; a Vercel publica a cada push na `main`): capa reduzida em `assets/img/capa-diaNN.jpg`, entrada em `DIAS` no `src/build.py`, miolo em `src/dias/<palavra>.html` com o guia prometido, `python3 src/build.py` e `node src/og.js`. Todo card e modal do site usa o Liquid Glass. Identidade nova: `.fan` (leque), `.okl` (certinho verde), `.pf` (foto com +), `em` serif em h1/h2, `.claude` laranja, fechamento roxo. `HOLD` tranca, `EARLY[n]` libera num horário (UTC), `?lab` mostra a prévia. Publicar na `main` só com o ok escrito do Luis (PR com a prévia antes).
15. **PDF da palavra-chave, só quando o Luis pedir:** páginas 1080×1920, 6 a 8 páginas (Playwright `page.pdf` com `printBackground`), fundo da marca, títulos em Anton, texto em Inter, pedidos ao Claude em bolhas vermelhas, passo a passo real conferido na ajuda do Claude (plano, nome da opção, botão), imagens só de frames do vídeo (nunca código), última página com a colinha e o convite pra marcar o @cobaia.dev, brilhos com `radial-gradient` (sem `filter: blur`).
16. Ajustes de cada vídeo juntos numa lista única antes de refazer. Uma tarefa por thread.
17. **Fim:** commit de `producoes/diaNN/` (sem MP4), peças novas em `motor/`, entrada no `CHANGELOG.md` e push.
18. **Revisão em 48 h (dossiê, seção 12):** quando o Luis mandar os números (pulo nos 3 s, tempo médio, envios, salvamentos, comentários, seguidores e visitas ao perfil por espectador, curva de retenção, origem das views, seguidores x não seguidores), cruze com as metas da seção 1 do dossiê, diga em que segundo a curva cai mais e o que estava na tela, e proponha o ajuste no `DOSSIE.md` (seção 14) com a data e o vídeo que provou. Registre em `producoes/diaNN/revisao-48h.md`.

## 11. QA antes de entregar

**Primeiro, o checklist da seção 11 do dossiê, mostrado preenchido ao Luis em toda entrega.** Todo item precisa ser "sim"; o que ficar "não" se corrige antes de mandar, ou se explica por que não dá:
- O tema passa nas 4 perguntas da seção 3?
- O primeiro quadro mostra a frase inteira e uma imagem concreta?
- O gancho afirma e começa pelo ganho ou pela dor de quem assiste?
- A série aparece só no selo, sem fala e sem cena?
- A dor com número aparece antes dos 7 s?
- O ganho vem antes do contexto?
- Cada prova tem número e imagem real (ou de referência)?
- As provas estão em escada crescente?
- As três camadas aparecem em todos os quadros?
- O vídeo tem no máximo 59 s?
- O CTA é curto e não pede pra mandar o vídeo?
- O card final mostra o próximo episódio?
- Nada promete o que a ferramenta não faz?
- A página do que a pessoa recebe já está no ar?

Depois, o QA técnico:
- **Repositório:** fez `git pull` antes? A chamada final é a padrão (seção 7)? A música não repete a de nenhum dos três dias anteriores? Peças novas reaproveitáveis voltaram para o `motor/`? CHANGELOG atualizado e push feito?
- **Render:** sem `PAGEERR` no console; quadro do storyboard igual ao do render final.
- Folha de contato a cada 0,5 s, mais frames em cada transição e evento. Confira:
  - Nada sobreposto (cabeçalho, frase fixa, legenda, partículas, cartões), nada importante abaixo de y 1536 nem à direita de x 940.
  - Ícone do Claude só nos momentos certos; laranja e cores de terceiros sem dominar a cena.
  - Eventos no tempo da palavra; nenhuma tela parada nem quadro quase vazio.
  - Legenda presente em todo quadro com fala, sem piscadas e sem bloco com menos de ~9 frames fora da fala real.
  - Barra de progresso com a curva dinâmica; cartões com dados reais.
  - Prompts internos, chaves, dados pessoais e conteúdo das skills borrados; nenhuma estratégia revelada; nada de profissão, diploma ou formação do Luis.
- Roteiro: nenhuma palavra repetida na mesma frase, nada de "Dia N de trinta" na fala, Humanizer aplicado.
- Áudio: −14 LUFS, pico ≤ −1,2 dBTP, música do começo ao fim, efeitos audíveis, música abaixo da voz.
- MP4 decodificado inteiro sem erro, duração, 30 fps, 1080×1920; leve abaixo de 25 MB.
- Pasta `postar/` completa, site atualizado, cópia no PC e push no repositório.

## 12. Código e fontes

- **Motor:** `motor/` (LEIAME.md): `lib.js` (mola, ruído, grão, texto), `synth.py` (instrumentos e foley sintetizados, mix), `icons.js` (logos vetoriais), `fonts.css` + `fonts/`, `perfil.jpg`, `render.cjs` / `render-paralelo.cjs` / `storyboard.cjs` (Playwright), `folha.py`, `enc.sh`, `enc-leve.sh`, `novo-dia.sh` e `voz/` (transcrição, alinhamento e corte).
- **Referências:** `DOSSIE.md` (regra principal), `referencia/dia10-v3/` (acabamento do motion), `referencia/dia09/`, `estudos/` (análise das 5 referências de fluid motion e a síntese 07), `exemplos/dia11-paleta-gta/` (só como exemplo de troca de paleta).
- **Fontes dos vídeos feitos:** `producoes/diaNN/fonte/` (consulta; o vídeo novo nasce do `novo-dia.sh`).
- Formatos: `formatos/motion/` e `formatos/face-cam/regras.md` (direção de gravação de rosto e quadro de novidades).

## 13. Registro de mudanças (obrigatório)

Sempre que o Luis pedir uma alteração ou melhoria (vídeo, roteiro, cena, áudio, processo ou regra), em qualquer conta:
1. **Atualize a regra** na seção certa desta skill (`skill/SKILL.md` do repositório), substituindo a regra antiga que conflite. Se for peça reaproveitável, atualize também o `motor/`.
2. **Acrescente uma entrada no topo do `CHANGELOG.md`**: data, conta que fez, o pedido do Luis resumido fielmente e o que mudou (arquivos). Nunca apague entradas antigas.
3. **Commit e push no mesmo dia** (`git pull --rebase` antes do push).
4. **Atualize a skill instalada na conta** pela ferramenta de propor skill (`cobaia-dev-videos`), com o conteúdo do `skill/SKILL.md`.

O histórico de mudanças fica só no `CHANGELOG.md`.
