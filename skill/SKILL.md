---
name: "cobaia-dev-videos"
description: "Roteiros, cenas e vídeos curtos do @cobaia.dev (série 30 dias, 30 experimentos com Claude) com a identidade visual, animações, áudio e processo aprovados pelo Luis."
---

# @cobaia.dev: vídeos curtos

Esta skill guarda tudo que o Luis aprovou nos vídeos do @cobaia.dev: identidade, animações, áudio, roteiro, chamada final e o processo técnico. Leia inteira antes de produzir qualquer roteiro, cena ou vídeo do canal.

Prioridade: o que o Luis pedir na conversa vence o que está aqui. Logo em seguida, registre a mudança nesta skill (seção 13).

Meta permanente: **cada vídeo precisa superar o anterior**, sem quebrar nenhuma regra desta skill.

## 0. Repositório primeiro (regra que vale para todas as seções)

Tudo o que se repete entre os vídeos mora no repositório privado `luisalves23/cobaia-producao`, que é a fonte única para todas as contas do Claude que produzem o canal. Comece pelo `CLAUDE.md` da raiz.

1. **Antes de cada produção: `git pull`.** Outra conta pode ter melhorado a skill, o motor ou as regras. Leia as entradas novas do `CHANGELOG.md` antes de começar.
2. **Todo vídeo novo nasce com `bash motor/novo-dia.sh NN`**, que cria `producoes/diaNN/` com o motor e a base do Dia 10 v3. A base serve para a estrutura (paleta, palavras grandes, leque, elemento vermelho, chamada final, roxo e loop); as cenas são sempre novas.
3. **O storyboard indica, cena por cena, de onde veio a peça** (referência, peça do motor ou "nova").
4. **Peça nova e reaproveitável volta para `motor/`** no fim do vídeo, com uma linha no `motor/LEIAME.md`.
5. **Mudou a identidade ou o processo?** Mude aqui (skill, motor ou CLAUDE.md), registre no `CHANGELOG.md` e dê push no mesmo dia.

## 1. O canal

- Perfil **@cobaia.dev**, lema "testo antes de você". Redes: Instagram Reels, TikTok e YouTube Shorts.
- **Propósito: ensinar o Claude.** Palavras do Luis: "na maior parte das vezes eu quero ensinar Claude para as pessoas". Cada vídeo explica um recurso (skills, conectores, MCP, Cowork, Claude Desktop, projetos, memória...) ou um conceito que parece difícil (tokens, janela de contexto, alucinação), de forma dinâmica e lúdica, com um exemplo da vida real. De vez em quando entra uma demonstração impressionante. Ferramentas de fora só aparecem quando ajudam a explicar o Claude.
- **O Luis também aprende com os vídeos.** A pessoa sai sabendo o que é, como funciona por dentro e como usar.
- **Exemplo da vida real (a régua do Luis):** o pão de queijo. Duas clientes querem o último pão de queijo; se as duas "compram" ao mesmo tempo, o estoque fica em −1, e por isso o banco de dados precisa de controle. Todo conceito ganha uma analogia assim: do dia a dia, visual, brasileira e fácil de lembrar.
- Série atual: **"30 dias, 30 experimentos com Claude"**. Ensina sem cara de aula: nada de "curso chato" nem "30 aulas". O plano dos 30 dias fica no Doc da série "30 dias de Claude".
- Formato: o Claude faz o vídeo inteiro (motion, legendas, música e efeitos). Toda tela do Claude é **simulada**, nunca gravação de tela.
- **Voz: o Luis sempre manda o áudio pronto** (ElevenLabs com a voz dele clonada, ou gravação de celular), anexado na conversa, junto com o texto aprovado do roteiro. O Claude nunca gera nem clona voz. Todo roteiro sai pronto para os dois jeitos (texto para gravar e texto para a IA de voz). Com o arquivo em mãos, não pergunte "gravada ou IA"; só pergunte se o áudio não vier.
- Mascote: rato de laboratório branco **de brinquedo**, com cara de impresso em 3D (4 cores de filamento), estilo miniatura de desenho animado antigo. O avatar do perfil é esse rato.
- Nunca revelar que algum cenário foi gerado por IA.
- Inspiração de ritmo: canal Sanji Chien (cortes ~3,7 s, ~190 palavras/min, zero silêncio vazio). Inspiração, nunca cópia.

## 2. Regras invioláveis

1. **Nada sobrepõe nada.** Palavras do Luis: "Não coloque elementos para sobrescrever elementos." Nenhum elemento fica em cima de outro, do cabeçalho ou da legenda, nem confete ou partículas sobre texto. Única exceção: uma transição breve.
2. **Nunca inventar exemplos.** Mostre o que existe de verdade: o arquivo real, o print real, a música realmente usada. Se precisar de um exemplo, baixe o real.
3. **Só música e efeitos próprios ou gratuitos com licença.** Padrão do Dia 10 v3: trilha e efeitos sintetizados no próprio vídeo com `motor/synth.py` (sem banco de efeitos genérico). Quando o Luis manda uma faixa, ela é remontada por trechos (exemplo no Dia 11). Faixa baixada: Mixkit direto por `https://assets.mixkit.co/music/<ID>/<ID>.mp3`, medida com `motor/voz/medir-musica.py`, crédito em `producoes/diaNN/CREDITOS.txt`. Pixabay bloqueia download automático. Nunca uma trilha "padrão de IA".
4. Sem marcas registradas em prompts de imagem (ex.: LEGO vira "blocos de montar"), sem Star Wars e sem plágio.
5. **Ícone do Claude:**
   - Aparece só quando "Claude" é falado (ou "ele", referindo-se ao Claude). No resto do tempo fica oculto ou num canto, sem cobrir nada.
   - Use o ícone oficial (o desenho `CLAUDE_PATH` de `motor/icons.js`), nunca um genérico. **Toda vez que "Claude" é falado, a logo aparece** (inclusive na chamada final): as pessoas batem o olho e reconhecem. A palavra "Claude" vai em Instrument Serif itálico laranja, e a transição de slime que chega nela também é laranja (nunca vermelha).
   - **A palavra vira a logo (Dia 10 v3):** "Claude" escrito se transforma, girando e de forma orgânica, na logo laranja (~0,1 s depois da fala, ~0,28 s de transformação). Palavra e logo nunca competem, e a logo nunca fica escondida. Só a palavra "Claude" faz isso ("Code" não).
   - **Outras ferramentas com a cara oficial delas:** falou GitHub, aparece a logo do GitHub, a tipografia e um formato que lembre o GitHub (estrelas no amarelo-ouro característico dele). Vale para qualquer marca citada: logo oficial (desenho vetorial em `motor/icons.js`; acrescente lá a que faltar), nunca caixa genérica com o nome escrito.
   - Em "foi o Claude", ele entra forte. No carimbo "ESCRITO PELO CLAUDE", ele **tomba**.
6. **Só os elementos que estão sendo falados naquele momento.** Muita informação no frame faz a pessoa rolar a tela.
7. **Nenhuma tela parada.** Cenas ligadas por transições de câmera com rastro, da esquerda para a direita. Nunca mais de ~1 s sem movimento relevante, e nenhuma tela quase igual por mais de ~2,5 s (no Dia 5 o chat ficou 4 a 5 s parado).
8. **Respeitar a área útil** das plataformas (seção 4).
9. **Aprovação antes de renderizar:** roteiro aprovado e storyboard estático (imagens) aprovado. Nunca amostra animada nem teste de animação. **Sem aprovação, não renderiza.** A única exceção é quando o Luis avisa antes que vai estar ausente e quer receber pronto.
10. **Estratégia é segredo da casa.** Palavras do Luis: "A gente usa, mas a gente não revela." Nunca explique na fala, na tela ou nas legendas do post as táticas do canal: a barra dinâmica, a curva de retenção, a fórmula dos ganchos e loops, a chuva de dopamina.
11. **Nada de código ou arquivo interno legível na tela.** Código, o texto da skill, o changelog e prompts grandes aparecem só como representação abstrata (retângulos em forma de palavra, blocos coloridos, rolagem rápida). Números reais podem aparecer.
12. **Canal dark.** Nunca mostrar o nome, a profissão ou qualquer dado do Luis: nada de nome na saudação da tela simulada, foto dele ou e-mail real. Saudações sem nome e avatares com letra genérica. **Exceção pedida em 17/11:** a foto de perfil nova do canal (`motor/perfil.jpg`) aparece **em todos os vídeos** (no mínimo no "segue o cobaia" da chamada final, com "@cobaia.dev" logo abaixo), nas capas e no site. Moldura branca redonda com o "+" **por cima da moldura**, nunca coberto pelo leque. Avatares de quem comenta continuam genéricos.
13. **Vídeo em loop.** O último frame emenda no primeiro.
14. **Verde só para o que é positivo:** acertou, certinhos do gabarito, grátis, R$ 0, dinheiro. "Nota máxima" e destaques de ênfase continuam vermelhos.
15. **Laranja é do Claude.** O laranja (`--or`) só aparece no ícone do Claude, na palavra "Claude" e no brilho dele. Nenhuma cena pode ser dominada por laranja, amarelo, azul ou verde: o vídeo é preto, off-white e vermelho (com fundo vermelho permitido nas inversões de ritmo), e cores de terceiros ficam dentro das telas simuladas. Exceção: o roxo escuro da chamada final padrão (seção 7).

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
- **Liquid Glass** (aprovado em 09/11/2026, referência: a barra do topo do site). Hoje vale para o site e para cartões de vidro quando o vídeo pedir; o Dia 10 v3 usa cartões flat (`#1D1D21`) com o contorno em leque e não tem vidro. Se for usar no vídeo:
  - Miolo só desfocado (3,5 px; 6 px em barras baixas). O fundo não aumenta.
  - Borda fina (22% do menor lado, 6 a 22 px) funcionando como lupa: o conteúdo de trás aparece espelhado e nítido. Lente gerada no tamanho e raio de cada cartão.
  - Reflexo em diagonal, brilho fino em cima e embaixo, varredura de luz ao entrar .
  - Preenchimento quase transparente, nunca cinza fosco. Sempre com conteúdo atrás e com movimento, senão a lente não aparece.
  - Nunca `backdrop-filter` no pai do vidro.
  - Telas claras grandes (chat, editor) também ganham vidro em volta ou por cima de uma peça falada; no Dia 5 elas entraram sem vidro nenhum.
- **Peças do motor:** mola (`spring`), texto com mola (`springText`), grão, ruído suave, retângulo arredondado (`rr`); no `d10.html`: palavras grandes com transformação em slime, leque de 3 vermelhos (`FAN`), elemento vermelho que vira bola e viaja, logo do Claude girando, chamada final, tela roxa e loop. Lista em `motor/LEIAME.md`.
- **Glitch** sempre em neon (cópias deslocadas e barras ciano `#00F0FF` e magenta `#FF2BD6`, com brilho), nunca nas cores das letras, senão parece texto riscado.
- **Desenho:** nada que lembre forma fálica (nada de dedo solitário com unha). Mão é mão aberta, cinco dedos, sem unhas.

## 4. Layout: 1080×1920, 30 fps

| Zona | Coordenadas |
|---|---|
| Topo da plataforma | y < 200: nada importante |
| Cabeçalho próprio | barra, selo e handle (abaixo) |
| **Conteúdo** | x 90–940, y 340–1400 |
| **Legenda** | top 1452, largura 850 |
| UI da plataforma | y > ~1560 e x > 940: nada importante |

- **Barra de progresso:** x 90–940, top 212, 12 px, cantos 6, trilho `rgba(242,238,230,.13)`, vermelho com glow. **Barra dinâmica:** `largura = 850 · (1 − e^(−K·u)) / (1 − e^(−K))`, `u = t/T`, `K = ln 25`, presa entre 0 e 850. Enche rápido no começo e quase para no fim, porque aí a pessoa já está presa.
- **Selo** "DIA NN/30": Anton 40 px numa pílula vermelha (left 90, top 246), com pop quando "dia N" é falado. **Handle** "@cobaia.dev": Mono 700 30 px `#bdbdbd` (right 140, top 253).
- O conteúdo nasce abaixo do cabeçalho (y ≥ 340).

**Legendas** (modelo antigo; no padrão atual as palavras grandes do `diaNNchunks.js` substituem a legenda):
- Inter 800 46 px, centradas, **sutis**. Palavra ativa com sublinhado vermelho; as outras com opacidade .8 e sombra escura. Blocos curtos sincronizados palavra a palavra.
- **Escondidas quando o texto falado já está grande na tela** : gancho tipográfico, digitação, título falado ("jeito lento", "sem código nenhum"), pergunta e palavra da chamada final. No Dia 5 a legenda repetiu vários desses textos.
- **Sem piscadas:** cada faixa escondida termina no início do bloco seguinte, e nenhum bloco fica menos de ~0,3 s na tela fora da fala real .
- O destaque do vídeo são as palavras que surgem e os motions, não a legenda. Na estética aprovada (seção 5.0), as palavras grandes em karaokê substituem a legenda pequena.

## 5. Movimento e transições

### 5.0 Estética de motion aprovada (16/11/2026, vale para todo vídeo)
Referência aprovada: teste "07 · Síntese" (`estudos/sintese-07/`, na versão com a identidade nova). Palavras do Luis: "Essa é a estética que eu quero nos próximos vídeos daqui pra frente." Não precisa repetir a mesma ordem de cores, cenas ou fontes; pode trazer algo a mais mantendo essa identidade.
- **O vídeo conta o que está sendo falado, literalmente:** cada fala vira a coisa de verdade na tela ("plano" abre um plano com checklist, "código" abre um terminal com código, "ganha vida" vira um app rodando), não só o lettering.
- **Cada roteiro pede a sua dinâmica.** Nada de ordem fixa de animações: o vídeo é fluido e está sempre em movimento. As regras abaixo são o padrão de qualidade, não um roteiro de cenas.
- **Gancho (0 a 3 s) é o trecho mais denso do vídeo:** mais dinâmico, mais efeitos, mais entrega e dopamina. Uma coisa nova por segundo; no segundo 2 a cena já mudou. Exemplo do Luis (Dia 09, "foi mal no Enem"): s1 prova do Enem minimalista sendo marcada e a nota caindo com números rolando rápido; s2 a prova vira uma caneta vermelha que escreve uma página num caderno branco pautado com espiral, rabisca, desenha, risca e reescreve; s3–4 a caneta vira uma nota 1000 gigante que encolhe e pousa na prova como nota escrita à mão, sublinhada como correção, com o gabarito cheio de certinhos verdes.
- **Um único elemento vermelho do começo ao fim (Dia 10 v3):** o destaque vermelho de cada cena é sempre o mesmo personagem. Palavras do Luis: "o elemento de destaque da cena anterior é deformado e comprimido até virar uma bola, e dessa bola ele se transforma no próximo elemento, sempre de forma orgânica." Nunca animação padrão ou engessada.
  - Passagem: comprime em bola (~0,16 s) e **deixa o lugar vazio**; a bola viaja em arco com uma voltinha (oscila, estica na velocidade, rastro e respingos); chegando, abre no destaque novo com mola. **A cena se monta ao redor dela**: é a bola que dá o start da construção.
  - Antes do storyboard, escreva a corrente "veio de → vira" batida por batida. Dia 10: ponto do Wi-Fi → play → caneta no calendário → seta → sinal de atenção → cursor do prompt → escrita do Claude Code → logo → lupa → ponteiro → lupa → cereja → casa → bola da briga → seta 6→11 → ponteiro → carregando → Wi-Fi → + de seguir → coração → base do Wi-Fi → ralo → roxo sem bola → loop.
  - Em fundo vermelho, o destaque troca de cor (off-white ou preto).
- **O elemento da cena anterior constrói a próxima** (fluidez): o contorno traça a nova forma (pontos com mola e atraso ao longo da linha) e o preenchimento chega logo depois.
- **Contorno em leque de 3 vermelhos:** pelo menos 3 contornos (vermelho vivo, médio e opaco), cada um num tempo e velocidade diferentes, formando um espectro/leque até assentarem na forma e sumirem. A abertura (a quebra) do contorno fica no **canto inferior esquerdo**, nunca em cima.
- **Contorno rente ao elemento**: segue exatamente a forma de baixo. Card arredondado → mesmo raio (nunca quadrado); estrela → colado na estrela. Gerar os pontos da forma real.
- **O contorno não fica parado na tela**: monta a forma e some (~1 s depois). Volta só para construir a próxima coisa.
- **Alternar janela e cena, nunca caixa-caixa-caixa:** o card/quadrado é só para janela de app ou quando é mesmo necessário. Intercale com cenas livres, ilustradas, sem caixa (um caminho, um mapa, um personagem). Card → cena → outra cena → card, por exemplo.
- **Mostrar a coisa de verdade, em flat minimalista:** prova do Enem = folha de prova de verdade, simplificada; calendário = calendário com páginas empilhadas embaixo (fundo), ponta inferior dobrada, faixa vermelha no topo ("experimento"), quadradinhos no lugar dos dias da semana, dias anteriores riscados à caneta de forma orgânica e o dia circulado à caneta quando é falado; mapa = papel que se desdobra e vira mapa tradicional com rotas, depois a bolinha entra nele e quica até uma bifurcação (um lado sem saída, outro no objetivo, com certo e errado); exercícios = lista estilo prova, um embaixo do outro, rolando, com opções A/B/C em barras arredondadas; professor = bonequinho minimalista com quadro, terno e gravata vermelha (chapéu de formatura não é professor).
- **Ligar duas coisas é uma animação, não uma caixa:** ex.: "ligo ele no Claude" = logo do GitHub com o repositório embaixo, a bolinha faz zigue-zague e encaixa na logo do Claude, e a ligação entre os dois aparece.
- **Números que caem:** nota ou valor diminuindo com dígitos rolando bem rápido (estilo caça-níquel).
- **Grafo de conhecimento** com partículas, e a linha vermelha ganha neon quando conecta.
- **Neon só se for neon de verdade** (bem vivo, brilho forte). Se não ficar convincente, sem neon.
- **Perspectiva leve** nas telas e cartões (rotação de 5 a 7°, nunca exagerada), mantendo a identidade.
- **Física de mola** (overshoot e assentamento), bolinha que quica com sombra no chão e squash no contato.
- **Fundo e tipografia invertendo no ritmo** (preto, vermelho, off-white) nos momentos de ênfase; o vídeo nunca fica estático.
- **Textura jateada/granulada** (como tinta borrifada): alternar contornos nítidos (em repouso, no contato) com contornos esfumaçados (em movimento). Nunca deixar um elemento só borrado, que parece baixa qualidade.
- **Palavras grandes no lugar da legendinha:** uma palavra ou frase curta por vez, bem grande, com a palavra falada acesa (karaokê) e a palavra-chave em vermelho. **Várias fontes** alternando (Anton, Instrument Serif itálico, Inter 900, JetBrains Mono); nunca o vídeo todo numa fonte só, e nada de título final em fonte tipo Helvética.
- **Duas fontes na mesma frase** quando ajuda: "de 30" numa fonte e "experimentos" em outra, vermelho; "com" na fonte da frase e "Claude" em serif laranja.
- **Cada fonte tem a sua animação de entrada** (não é sempre a mesma): a mono (código) é digitada, com o elemento vermelho virando o cursor; a serif acende; a Anton bate com peso; etc.
- **Uma palavra se transforma na outra como slime:** transição orgânica, sutil e rápida (~0,15 a 0,2 s, desfoque + limiar), nunca palavra que só surge.
- **HUD de ficha técnica** discreto (rótulos nos cantos, contador de tempo, marcador de batida) e uma interação por batida nos trechos de demonstração.
- **Cor oficial: vermelho** (`--rd`); verde só no que é positivo (regra 14).
- **Área segura e desfoque de lente:** o principal fica dentro da área de conteúdo (seção 4). Elementos podem passar para a borda, mas tudo o que sai da área segura ganha desfoque progressivo: leve perto dela e bem borrado na borda do vídeo, como lente. Pode ter uma distorção de luz sutil (tipo glassmorphism), sem chamar atenção.
- **Ritmo agitado**, com batida que mantém o vídeo vivo.

- **Estações (modelo antigo):** cada bloco do roteiro é uma estação de 1080 px num "mundo" horizontal. A câmera passa em **0,36 s** , com borrão horizontal de no máximo 5 px. Use só quando a transformação do objeto (5.0) não couber.
- **Várias etapas numa estação:** faixa rígida que desliza para a esquerda; elementos persistentes ficam fixos abaixo.
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
- **Telas simuladas** :
  - Só o conteúdo da tela, cantos levemente arredondados e sombra, **sem moldura** de monitor ou celular falso. Parece gravação de tela editada.
  - Entram giradas (rotateY 25 a 40°, escala .8) e assentam inclinadas (±6 a 8°).
  - **Zoom inclinado no ponto falado:** a cada clique ou detalhe, a tela inteira corre e inclina até o ponto (`foco()`, ~0,4 s). **Raramente a tela inteira**, só quando o assunto é geral. Anime a escala do contêiner, nunca amplie bitmap pequeno.
  - **Zoom na ênfase (pedido do Luis em 11/11):** onde a fala dá ênfase ou mostra algo, a câmera dá zoom nesse ponto, e os frames de aprovação já mostram esse zoom. Em demonstração de sistema ou app (vários apps abrindo, teste de velocidade, player), o zoom é **leve** (1,15 a 1,35x) e **acompanha o mouse**.
  - **Antes e depois lado a lado:** em comparação de velocidade, tela dividida com o jeito antigo travando (carregando, erro, fechando) e o novo abrindo na hora, cada lado com seu cronômetro.
  - **Cursor branco** guiando tudo o que é falado: vai até o item e clica com leve encolhida.
  - Pedido digitado no ritmo da fala, palavras-chave em vermelho, legenda escondida nesse trecho.
  - Mockups genéricos, nunca print nem réplica exata de terceiros.
  - **Cliques em sequência** (ex.: "Cancelar inscrição"): botão vermelho com texto branco; o cursor clica num, desce, clica no próximo; cada linha clicada vira "✓ Cancelada" e some; o zoom acompanha cada clique.
- **Gancho desde o frame 0**, sem fade do preto.
- **Retomada do dia anterior** só entra onde o Luis fala dela no áudio.
- Pode acelerar a voz se ajudar no ritmo (seção 9).
- **Reação real do Luis:** quando ele manda um vídeo da própria reação, ele entra curto (até ~3 s), em vertical 1080×1920, podendo acelerar até 1,15x. Antes de usar, confira quadro a quadro e borre o que for sensível (nome de Wi-Fi, IPs, nomes, e-mails).

## 6. Cenas aprovadas (referência de nível)

Referência atual: Dia 10 v3 (`referencia/dia10-v3/postar/cobaia-dia10-final-leve.mp4`, fonte em `referencia/dia10-v3/fonte/`). Também na nova estética: Dia 9 (`referencia/dia09/`) e o teste "07 · Síntese" (`estudos/sintese-07/`). Reaproveite a ideia com elemento novo; nunca repita o exemplo ou o app de um vídeo anterior. Temas já usados nos Dias 1 a 11 estão no `CLAUDE.md`.

## 7. Chamada final e material de quem comenta

**Chamada final padrão (atualizada em 17/11/2026):** a chamada ainda é o vídeo: mesmo estilo (preto, vermelho e branco), e o elemento vermelho continua construindo as cenas.
1. **"Segue o cobaia":** foto de perfil do canal (`motor/perfil.jpg`) com **"@cobaia.dev" logo embaixo** (nunca escondido no rodapé). Botão "+" como no TikTok: o cursor vai e clica (ou aparece o clique), o ícone vibra e vira ✓.
2. **"Curte":** a foto com o ✓ desliza para a esquerda; à direita, o coração cresce com pop de bolha e fica curtido.
3. **"Comenta PALAVRA":** abre uma caixa de comentário, a palavra é digitada e enviada; depois aparece embaixo o card do material ("guia completo").
4. **Fim sem fala (~2 s), sempre igual:** corte seco para a tela roxa escura (`#0B0820`), clique e nota de vidro, "comenta" em Inter e a PALAVRA em Instrument Serif itálico acesa (neon só se for vivo de verdade).
5. **Loop:** a bolinha volta para a posição do primeiro frame, emendando no começo.
- Se "Claude" é falado na chamada, a logo do Claude aparece.
- Fala: "Quer saber mais sobre o Claude? Segue o cobaia, curte e comenta PALAVRA que eu te mando [o material]."
- Animação: "QUER SABER MAIS / SOBRE O [ícone] CLAUDE?" em Anton; avatar 330 px centralizado com "+" que vira ✓ e fogos; coração branco que fica vermelho; só o campo de comentário em vidro digitando a palavra; cartão da mensagem com o material; no fim, "COMENTA / PALAVRA" gigante. Só o elemento que está sendo falado. Nunca print ou réplica da tela do TikTok.
- Cada dia tem uma palavra-chave diferente (lista no Doc). Sem palavra-chave, pergunta aberta, nunca sim/não.
- **Entrega do material:** cada palavra-chave tem uma página no site (`cobaia-dev.vercel.app/<palavra>`). **O Luis manda o link à mão** para quem comenta: entregue a mensagem de DM com o **link sozinho numa linha** (a prévia vira o botão) e um atalho de resposta salva (ex.: `wifi`). Não existe automação de DM (o plano dela está salvo no documento "Plano: link do guia por comentário").
- **PDF só quando o Luis pedir.** Palavras dele: "esse pdf deve ser solicitado, enquanto não for solicitado não produza, pois posso pedir alterações nos vídeos". O roteiro pode prometer o material; a página do site leva o guia.
- Pedido extra de engajamento só quando o Luis pedir (custa segundos).

## 8. Roteiro e textos do post

- **Gancho:** sempre do banco de ganchos virais (`roteiro/banco-ganchos-virais.md`, atualizado 1x por semana), com prova de alcance citada no plano. **Se a estrutura lembrar a de um dia anterior, escolha outro do banco.** Antes de cada roteiro, pesquise canais relevantes de fora (EUA e Europa) sobre o tema, veja os vídeos com maior alcance e replique o que comprovadamente funciona (gancho, estrutura, edição). Nada inventado do zero; tudo respaldado em referência viral real, citada no plano. Formato, ângulo, gancho e edição não se perguntam ao Luis: quem decide é a pesquisa.
- **Estrutura:** gancho nos 2 primeiros segundos; **logo depois do gancho, a vinheta "Dia N dos trinta experimentos com Claude"** (até uns 5 s); depois o tema, com um "trinta" só no vídeo inteiro. A vinheta nunca vai para o final.
- **Ingredientes, sem ordem fixa no resto:** o conceito com substância (o que é, como funciona por dentro, quando usar, exemplo concreto) explicado com analogia da vida real; a tela do Claude simulada mostrando na prática; "você não precisa fazer isso: o Claude ajuda a fazer o seu"; teaser do próximo dia quando couber; chamada final (seção 7).
- **Vida real, não conceito:** "eu não falo sobre o tema, eu falo sobre a vida das pessoas com o tema". Mostre o Claude resolvendo uma cena da rotina, com o resultado legível na tela (como o Dia 2). No máximo uma metáfora; sem aula de segurança fora do tema. Confira na documentação o que o recurso faz antes de prometer. Por ora tudo é simulado.
- **Vida real primeiro** funciona bem: começar pela analogia e só depois revelar que é sobre o Claude (Dia 3 v3: "O melhor chef do mundo perde pro feijão da sua vó. O Claude é igualzinho: entende de tudo, menos do seu jeito."). O conceito precisa de substância: o Dia 3 v2 foi vetado porque "não mandou nada demais sobre o tema".
- **No máximo 60 segundos** (regra do Luis desde 16/11/2026), bem prático. 170 a 195 palavras dão uns 52 a 60 s depois dos cortes e da aceleração. Acima disso, corte. Se não couber, corte frase de enchimento em vez de acelerar mais.
- **Não repetir exemplos nem apps de vídeos anteriores** (Gmail e Agenda já foram no Dia 4; Canva no Dia 5).
- **Sem fórmula:** nada de "o truque" ou "o segredo" em todo vídeo. Loop aberto, mito e quebra só quando cabem.
- **Sem palavra repetida** na mesma frase nem na seguinte (fora o tema e "Claude"). Rode uma checagem de repetição antes de entregar. Vetados: "Todo mundo tá falando de skill no Claude. E tá todo mundo complicando." e "Dia três de trinta. Trinta dias, trinta experimentos". Evite abrir de novo com negação (Dia 1 "Ninguém...", Dia 2 "Eu não...").
- **Senioridade:** nunca "eu não escrevi", "eu não fiz" ou "eu não sei", que fazem o Luis parecer leigo. Use "você não precisa fazer isso: o próprio Claude faz (ou ajuda)". Quando ele entrega um arquivo ou prompt grande, ele diz que fez, e que a pessoa não precisa de um desse tamanho porque o Claude ajuda a montar o dela.
- **Valor do perfil:** o Luis deixa simples o que outros vendem em curso pago ou explicam em vídeo longo. Isso aparece pela clareza, sem virar bordão. Se citar curso pago, confira antes que ele existe.
- **Teaser do dia seguinte** grave e curioso, sobre o tema real do próximo dia do plano, de preferência algo que atinge a própria pessoa (Dia 3 v3: "Amanhã: você pode passar a chave do seu e-mail pro Claude. A pergunta é: deveria?"). Ele trava a ordem do plano: se o Luis quiser trocar o próximo tema, ajuste antes de ele gravar.
- **Motion junto com o roteiro:** cada frase tem um evento visual forte, com transição e som.
- **Humanizer sempre:** todo roteiro e todo plano de roteiro passam pela skill `humanizer` antes de ir para o Luis.
- **Um roteiro por vez**, do próximo dia. Quando o dia depende de um teste, o texto final só sai com o resultado na mão.
- **Entrega do roteiro:** texto para o Luis gravar e texto para a IA de voz (sem tags, ou com tags animadas como [excited], [curious], [laughs]; nada de tom baixo astral), mais "Como gravar", "Onde estão os gatilhos" e "O que vai aparecer na tela" (Fala | Na tela | De onde vem a peça | Transição e som).
- **Textos de postagem do dia num único pedido:** legendas das 3 redes e comentário fixado.
  - **Instagram:** 1ª linha é um segundo gancho com emoji; 3 a 5 linhas que ensinam; "comenta PALAVRA"; 5 hashtags (1 grande, 2 médias, 2 de nicho).
  - **TikTok:** gancho com a palavra que as pessoas buscam, 1 ou 2 linhas, "comenta PALAVRA", uma pergunta e 3 a 5 hashtags.
  - **YouTube Shorts:** título de busca com até 60 caracteres, 2 linhas, "Inscreva-se: amanhã sai o Dia N+1" com o motivo, 2 ou 3 hashtags.
  - **Comentário fixado:** pergunta aberta no Instagram e no TikTok; no YouTube, pedido de inscrição com motivo.
  - Hashtags: grandes #inteligenciaartificial #ia #tecnologia; médias #claudeai #produtividade #automacao #dicasdetecnologia; nicho #claude #anthropic #skills #claudecode #semprogramar.
  - Nunca explicam as táticas do vídeo.
- Roteiros e decisões ficam no Doc da série.

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
- Troca de trecho ou de instrumento: fade-out de um e fade-in do outro (crossfade de 1 a 2 s), nunca corte seco.
- Volume e filtro mudam em rampa de pelo menos 1 s. Nada de degrau de volume entre cenas.
- Uma base musical só, que evolui (camadas entrando e saindo aos poucos, filtro abrindo e fechando). Não pular de uma música para outra.
- Silêncio ou parada só com fade curto na entrada e na saída, e só em momento forte do roteiro.
- `motor/trilha.py` não está aprovado como está: antes de reusar, suavize as transições (rampas e crossfades) e mande uma amostra de áudio para o Luis ouvir antes de montar no vídeo.

**Som do elemento vermelho:** squish na compressão, pluck no voo, pop com tink na abertura, **30% mais baixo que no Dia 10 v3** (×0,7, cerca de −3 dB).

**Efeitos que fogem do óbvio:** nada do whoosh, pop, ding e confete que todo vídeo com IA usa. Prefira sub_drop, reverse_swell, glass_chime, bloom, tape_whirl, tick_wood, power_down; e no visual, vinheta que respira na tensão, luz vazada na revelação, separação RGB na falha, linha de varredura, anel de onda e soco de zoom no drop.

**Efeitos ("chuva de dopamina"):** todos sincronizados com palavras ou eventos, gerados pelos instrumentos de foley do `motor/synth.py` (waterdrop, tink, glass, relay, keyclick, subdrop, swell, tapestop, pluck_bend etc.; lista no `motor/LEIAME.md`). As passagens alternam sons diferentes. Instrumento novo entra no `synth.py`, nunca solto dentro de um vídeo.

**Master:** `loudnorm I=-14 LUFS, TP=-1.2` (aplicado no `motor/enc.sh`).

## 10. Pipeline de produção

O passo a passo com comandos está no `CLAUDE.md`. Resumo:
1. `git pull` e leitura do `CHANGELOG.md`.
2. Roteiro aprovado (seção 8); o Luis manda o áudio pronto (ElevenLabs ou celular) com o texto aprovado.
3. `bash motor/novo-dia.sh NN` → `producoes/diaNN/` (fonte, postar e CREDITOS).
4. **Voz** (seção 9) → palavras com tempo → `fonte/dNNchunks.js` (palavras grandes: fonte por bloco, palavra-chave 1 = vermelho, 2 = "Claude" laranja, 3 = verde).
5. **Mapa da música:** medir a faixa (ou planejar a sintetizada) e escrever o mapa de trechos contra a fala (`mapa-musica.md`, modelo no Dia 11).
6. **Corrente do elemento vermelho:** tabela "veio de → vira" batida por batida (`corrente.md`, modelo no Dia 11).
7. **Cenas** no `fonte/dNN.html` em canvas, tudo função de `t` (sem `Date`, sem `Math.random` sem semente, sem CSS transition). `window.NFRAMES` e `window.ready` obrigatórios; `draw(t)` desenha o quadro.
8. **Storyboard estático:** `node ../../motor/storyboard.cjs dNN.html sb <tempos...>` e folha com `python3 ../../motor/folha.py sb storyboard.jpg`. Mande para aprovação. Não renderize sem aprovação (seção 2, regra 9).
9. **Render:** `node ../../motor/render-paralelo.cjs dNN.html frames I N` em N processos (ou `render.cjs` num só). Confira correções com o storyboard nos tempos alterados; o arquivo final sai de um render completo.
10. **Áudio:** `python3 aNN.py` gera o mix (trilha + foley + voz) com `motor/synth.py`. Som do elemento vermelho a ×0,7.
11. **Encode:** `bash ../../motor/enc.sh frames mix.wav ../postar/cobaia-diaNN-final.mp4` (x264 crf 17, yuv420p, AAC 256k, loudnorm −14 LUFS, TP −1,2). Leve (< 25 MB): `bash ../../motor/enc-leve.sh` (alvo `192000 ÷ duração − 160` kbps).
12. **Entrega em `producoes/diaNN/postar/`:** `cobaia-diaNN-final.mp4` (HQ), `cobaia-diaNN-final-leve.mp4`, `capa-diaNN.jpg` e `textos-postagem-diaNN.txt` (legendas das 3 redes, comentário fixado e DM). Os MP4 não vão para o git (ficam na pasta do projeto / Biblioteca); o resto vai.
    - **Cópia no PC (até o fim dos 30 dias):** a versão HQ vai para `C:\Users\Fernando\cobaia\diaNN\`. Sem ferramenta de transferência, avise o Luis para baixar.
13. **Capa 1080×1920 (identidade nova, 17/11):** gerador em `capas/capas.html` (`node shot_capas.cjs <saída>`; dia novo = entrada em `DAYS` + ilustração em `ILL`, e o número do dia na lista do `shot_capas.cjs`). Fundo preto com brilho vermelho e grão, HUD de cantos e barra de progresso da série; "DIA NN" Anton vermelho 132 px com "/30" apagado; gancho encurtado em duas linhas (serif itálico + Anton, palavra-chave vermelha, "Claude" laranja); cartão 900×700 com leque de 3 vermelhos e ilustração flat da coisa real, ponto vermelho guiando o olho; rodapé com foto + "+", "@cobaia.dev" e "comenta PALAVRA" em pílula vermelha. Tudo entre y 240 e 1680. Destaque do Instagram: ícone grande no círculo central com leque circular (`destaque(kind)`).
14. **Site (obrigatório):** sempre que um vídeo for criado ou editado, atualize a página da palavra-chave e o calendário em cobaia-dev.vercel.app (repo `luisalves23/cobaia-site`; a Vercel publica a cada push na `main`): capa reduzida em `assets/img/capa-diaNN.jpg`, entrada em `DIAS` no `src/build.py`, miolo em `src/dias/<palavra>.html` com o guia prometido, `python3 src/build.py` e `node src/og.js`. Todo card e modal do site usa o Liquid Glass. Identidade nova: `.fan` (leque), `.okl` (certinho verde), `.pf` (foto com +), `em` serif em h1/h2, `.claude` laranja, fechamento roxo. `HOLD` tranca, `EARLY[n]` libera num horário (UTC), `?lab` mostra a prévia. Publicar na `main` só com o ok escrito do Luis (PR com a prévia antes).
15. **PDF da palavra-chave, só quando o Luis pedir:** páginas 1080×1920, 6 a 8 páginas (Playwright `page.pdf` com `printBackground`), fundo da marca, títulos em Anton, texto em Inter, pedidos ao Claude em bolhas vermelhas, passo a passo real conferido na ajuda do Claude (plano, nome da opção, botão), imagens só de frames do vídeo (nunca código), última página com a colinha e o convite pra marcar o @cobaia.dev, brilhos com `radial-gradient` (sem `filter: blur`).
16. Ajustes de cada vídeo juntos numa lista única antes de refazer. Uma tarefa por thread.
17. **Fim:** commit de `producoes/diaNN/` (sem MP4), peças novas em `motor/`, entrada no `CHANGELOG.md` e push.

## 11. QA antes de entregar

- **Repositório:** fez `git pull` antes? A chamada final é a padrão (seção 7)? A música não repete a de nenhum dos três dias anteriores? Peças novas reaproveitáveis voltaram para o `motor/`? CHANGELOG atualizado e push feito?
- **Render:** sem `PAGEERR` no console; quadro do storyboard igual ao do render final.
- Folha de contato a cada 0,5 s, mais frames em cada transição e evento. Confira:
  - Nada sobreposto (cabeçalho, legenda, partículas, cartões) e conteúdo dentro de x 90–940, y 340–1400.
  - Ícone do Claude só nos momentos certos; laranja e cores de terceiros sem dominar a cena.
  - Eventos no tempo da palavra; nenhuma tela parada nem quadro quase vazio.
  - Legenda escondida onde o texto já está grande na tela, sem piscadas e sem bloco com menos de ~9 frames fora da fala real.
  - Barra de progresso com a curva dinâmica; cartões com dados reais.
  - Nenhum código, texto da skill ou prompt legível; nenhuma estratégia revelada; nenhum dado do Luis.
- Roteiro: nenhuma palavra repetida na mesma frase, um "trinta" só, vinheta logo depois do gancho, gancho do banco com referência citada, Humanizer aplicado.
- Áudio: −14 LUFS, pico ≤ −1,2 dBTP, música do começo ao fim, efeitos audíveis, música abaixo da voz.
- MP4 decodificado inteiro sem erro, duração, 30 fps, 1080×1920; leve abaixo de 25 MB.
- Pasta `postar/` completa, site atualizado, cópia no PC e push no repositório.

## 12. Código e fontes

- **Motor:** `motor/` (LEIAME.md): `lib.js` (mola, ruído, grão, texto), `synth.py` (instrumentos e foley sintetizados, mix), `icons.js` (logos vetoriais), `fonts.css` + `fonts/`, `perfil.jpg`, `render.cjs` / `render-paralelo.cjs` / `storyboard.cjs` (Playwright), `folha.py`, `enc.sh`, `enc-leve.sh`, `novo-dia.sh` e `voz/` (transcrição, alinhamento e corte).
- **Referências:** `referencia/dia10-v3/` (padrão), `referencia/dia09/`, `estudos/` (análise das 5 referências de fluid motion e a síntese 07), `exemplos/dia11-paleta-gta/` (só como exemplo de troca de paleta).
- **Fontes dos vídeos feitos:** `producoes/diaNN/fonte/` (consulta; o vídeo novo nasce do `novo-dia.sh`).
- Formatos: `formatos/motion/` (atual) e `formatos/face-cam/` (reservado; o Luis define as regras).

## 13. Registro de mudanças (obrigatório)

Sempre que o Luis pedir uma alteração ou melhoria (vídeo, roteiro, cena, áudio, processo ou regra), em qualquer conta:
1. **Atualize a regra** na seção certa desta skill (`skill/SKILL.md` do repositório), substituindo a regra antiga que conflite. Se for peça reaproveitável, atualize também o `motor/`.
2. **Acrescente uma entrada no topo do `CHANGELOG.md`**: data, conta que fez, o pedido do Luis resumido fielmente e o que mudou (arquivos). Nunca apague entradas antigas.
3. **Commit e push no mesmo dia** (`git pull --rebase` antes do push).
4. **Atualize a skill instalada na conta** pela ferramenta de propor skill (`cobaia-dev-videos`), com o conteúdo do `skill/SKILL.md`.

O histórico de mudanças fica só no `CHANGELOG.md`.
