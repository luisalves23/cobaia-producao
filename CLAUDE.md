# @cobaia.dev: produção de vídeos

Este repositório é a fonte única de como o @cobaia.dev produz vídeos hoje. Qualquer conta do Claude que editar vídeos do canal trabalha a partir daqui e devolve para cá o que melhorar. Duas contas usam o mesmo repositório, então ele é a memória compartilhada entre elas.

## Regra de sincronia (obrigatória)

1. **Antes de qualquer produção ou mudança:** `git pull`. Depois, leia no `CHANGELOG.md` as entradas que você ainda não conhece.
2. **Depois de qualquer melhoria** (regra nova, ajuste da skill, peça nova do motor, correção de processo, pedido do Luis): edite o arquivo certo, acrescente uma entrada **no topo** do `CHANGELOG.md` e faça commit e push no mesmo dia.
   - Formato da entrada: `## AAAA-MM-DD · conta (principal ou secundária) · título curto`, depois o pedido do Luis em uma ou duas linhas e a lista do que mudou (arquivos).
   - Mensagem de commit: o mesmo título curto.
   - Antes do push: `git pull --rebase`. Em conflito, mantenha as duas mudanças e registre no CHANGELOG.
3. **Mudou a skill?** Além do commit, atualize a skill instalada na sua conta com o conteúdo de `skill/SKILL.md` (ver `skill/COMO-INSTALAR.md`).
4. Nunca apague entradas do CHANGELOG nem reescreva histórico (`push --force` proibido).

Prioridade em caso de conflito: o que o Luis disser na conversa, depois `skill/SKILL.md`, depois este arquivo, depois o resto.

## Quando o Luis pedir uma mudança

Vale para qualquer pedido que altere o jeito de produzir (visual, roteiro, áudio, processo, regra), mesmo dito de passagem durante um vídeo.
1. `git pull`.
2. Aplique no vídeo em andamento, se for o caso.
3. Leve para o lugar certo, substituindo a regra antiga que conflite (nunca deixe duas regras contraditórias):
   - regra, identidade, motion, roteiro, áudio ou post → `skill/SKILL.md`, na seção certa;
   - peça ou função reaproveitável → `motor/` + linha no `motor/LEIAME.md`;
   - passo do processo, setup ou sincronia → este `CLAUDE.md`;
   - regra só de vídeo com rosto → `formatos/face-cam/`.
4. Entrada no topo do `CHANGELOG.md` com as palavras do Luis resumidas fielmente e a lista do que mudou.
5. Commit, `git pull --rebase`, push.
6. Atualize a skill instalada na sua conta (`skill/COMO-INSTALAR.md`) e diga ao Luis, em uma linha, o que mudou e onde.

Se o pedido for só para um vídeo ("neste vídeo, faz assim"), aplique no vídeo e não mude a regra. Na dúvida, pergunte se vale para os próximos.

## Como trabalhar com o Luis

- Português do Brasil, frases simples, resposta primeiro.
- Um roteiro por vez, do próximo dia. Roteiro passa pela skill `humanizer` antes de ir para ele. O áudio da fala sempre vem pronto dele (ElevenLabs com a voz dele clonada ou celular), junto com o texto aprovado; você nunca gera voz e só pergunta se o arquivo não vier.
- Nunca renderize sem roteiro e storyboard estático aprovados, a não ser que ele avise antes que vai estar ausente e quer receber pronto.
- Ajustes de um vídeo: junte numa lista única antes de refazer.
- Formato, ângulo, gancho e edição não se perguntam: quem decide é a pesquisa de referências virais.
- PDF do material só quando ele pedir.
- Publicar o site só com o ok escrito dele.

## Ordem de leitura

1. Este arquivo.
2. `skill/SKILL.md` inteira (regras, identidade, motion, roteiro, áudio, QA).
3. `CHANGELOG.md` (o que mudou recentemente) e `skill/historico-pedidos.md` (todos os pedidos do Luis desde 01/11, para entender por que cada regra existe).
4. `referencia/dia10-v3/`: assista `postar/cobaia-dia10-final-leve.mp4` e leia `fonte/d10.html`. É o padrão aprovado.
5. `motor/LEIAME.md` e `motor/voz/LEIAME.md`.
6. Quando for roteirizar: `roteiro/banco-ganchos-virais.md` e `roteiro/plano-30-dias.md`.

## Instalação (uma vez por ambiente)

```bash
git clone https://github.com/luisalves23/cobaia-producao && cd cobaia-producao
pip install numpy scipy pillow          # áudio e folhas de contato
# Node + Playwright com Chromium (nos ambientes do Claude já vem instalado; senão: npm i -g playwright && npx playwright install chromium)
# ffmpeg
# opcional, para transcrever voz gravada: pip install faster-whisper
```

Confira que tudo bate com o vídeo aprovado (seção "Verificar uma instalação nova" do `motor/LEIAME.md`). Se o quadro não bater, não produza: algo no ambiente está diferente (fonte, navegador).

## Pipeline de um vídeo

Voz → mapa da música → corrente do elemento vermelho → storyboard → render → capa → textos do post. Em detalhe:

| # | Etapa | O que fazer | Sai em |
|---|---|---|---|
| 0 | Sincronizar | `git pull`, ler o CHANGELOG | |
| 1 | Roteiro | Gancho do banco com referência viral citada, vinheta "Dia N dos trinta experimentos com Claude" logo depois, até 60 s (170 a 195 palavras), humanizer, texto para gravar e texto para IA de voz. **Aprovação do Luis.** | `producoes/diaNN/roteiro.md` |
| 2 | Pasta do dia | `bash motor/novo-dia.sh NN` | `producoes/diaNN/` |
| 3 | Voz | O Luis manda o áudio pronto + o texto aprovado. Copie o upload para `fonte/voz.mp3` (ou `.wav`, ajustando `VOZ` no `aNN.py`). ElevenLabs: entra como chegou, palavras com tempo pelo `align.py`. Celular: `transcribe.py` (ou `align.py`) + `cut3.py`. Receita, volumes e plano B sem whisper: `motor/voz/LEIAME.md`. | `fonte/voz.*`, palavras com tempo |
| 4 | Palavras grandes | Escrever à mão o `fonte/dNNchunks.js` a partir das palavras com tempo (passo a passo no `motor/LEIAME.md`): uma palavra ou frase curta por bloco, fonte alternando, destaques 1/2/3 | `fonte/dNNchunks.js` |
| 5 | Mapa da música | Trilha sintetizada no `aNN.py` (como no Dia 10) ou faixa medida com `medir-musica.py` e remontada por trechos (como no Dia 11). Drop no gancho, respiro antes da virada, drop na revelação, cheio na chamada final. | `mapa-musica.md` |
| 6 | Corrente do elemento vermelho | Tabela tempo · fala · "veio de → vira" · cena, batida por batida, até o loop | `corrente.md` |
| 7 | Cenas | Reescrever as cenas do `fonte/dNN.html` (a base do Dia 10 já traz paleta, palavras, leque, bola vermelha, chamada final, roxo e loop) | `fonte/dNN.html` |
| 8 | Storyboard | `cd producoes/diaNN/fonte && node ../../../motor/storyboard.cjs dNN.html ../storyboard <um tempo por cena>` e `python3 ../../../motor/folha.py ../storyboard ../storyboard.jpg`. **Aprovação do Luis antes de renderizar.** | `storyboard.jpg` |
| 9 | Render | `node ../../../motor/render-paralelo.cjs dNN.html frames I N` (N processos) | `fonte/frames/` (fora do git) |
| 10 | Áudio | `python3 aNN.py` (trilha + foley + voz, som do elemento vermelho a ×0,7) | `dNN.wav` (fora do git) |
| 11 | Encode | `bash ../../../motor/enc.sh frames dNN.wav ../postar/cobaia-diaNN-final.mp4` e `bash ../../../motor/enc-leve.sh ../postar/cobaia-diaNN-final.mp4 ../postar/cobaia-diaNN-final-leve.mp4` | `postar/` |
| 12 | Capa | Entrada em `DAYS` e ilustração em `ILL` no `capas/capas.html`, depois `cd capas && DIAS=NN node shot_capas.cjs ../producoes/diaNN/postar/` | `postar/capa-diaNN.jpg` |
| 13 | Textos | Instagram, TikTok, YouTube Shorts, comentários fixados e DM com o link sozinho numa linha (modelo: `referencia/dia10-v3/postar/textos-postagem-dia10.txt`) | `postar/textos-postagem-diaNN.txt` |
| 14 | QA | Checklist da seção 11 da skill | |
| 15 | Site | Página da palavra-chave em `luisalves23/cobaia-site` (skill seção 10, item 14), por PR, publicar só com o ok do Luis | |
| 16 | Fechar | Commit de `producoes/diaNN/` (os MP4 ficam fora do git, ver `.gitignore`), peças novas no `motor/`, CHANGELOG, push | |

Os MP4 finais não vão para o git. Entregue-os ao Luis pela própria conversa ou pela pasta do projeto.

## Regras que o Luis aprovou (resumo; o texto completo está na skill)

- **Cada vídeo supera o anterior**, sem quebrar nenhuma regra.
- **Aprovação antes de renderizar:** roteiro aprovado e storyboard estático aprovado. Nunca amostra animada.
- **Nada sobrepõe nada.** Só o que está sendo falado aparece. Nenhuma tela parada por mais de ~1 s.
- **O vídeo mostra literalmente o que está sendo falado**, com a coisa de verdade em flat minimalista.
- **Um único elemento vermelho do começo ao fim:** comprime em bola, deixa o lugar vazio, viaja em arco com uma voltinha e abre no próximo destaque com mola; a cena se monta em volta dele.
- **Contorno em leque de 3 vermelhos**, rente à forma, abertura no canto inferior esquerdo, monta e some.
- **Palavras grandes no lugar da legenda**, várias fontes (Anton, Instrument Serif itálico, Inter 900, JetBrains Mono), cada uma com sua entrada, transição em slime entre palavras.
- **"Claude" falado vira a logo laranja**, girando, ~0,1 s depois da fala. Laranja só do Claude. Verde só para o que é positivo. Vídeo em preto, off-white e vermelho, alternando o fundo no ritmo.
- **Chamada final padrão:** segue (foto + "@cobaia.dev", "+" vira ✓) → curte (coração) → comenta PALAVRA (caixa digitando, card do material) → corte seco para o roxo `#0B0820` → loop para o primeiro quadro.
- **Canal dark:** nada do nome, rosto ou dados do Luis; a única exceção é a foto de perfil do canal.
- **Estratégia é segredo da casa:** nunca explicar as táticas no vídeo ou no post. Nada de código legível na tela.
- **Música e efeitos próprios ou com licença**, nunca trilha "padrão de IA"; sem whoosh, ding e confete óbvios.
- **Máximo de 60 s.** Gancho de 0 a 3 s é o trecho mais denso do vídeo.

## O que já foi feito (não repetir tema, exemplo nem app)

| Dia | Tema | Palavra |
|---|---|---|
| 1 | Ninguém editou esse vídeo (o Claude edita um vídeo) | pergunta aberta |
| 2 | Uma frase virou um jogo | JOGO |
| 3 | Skill é a receita da vó | SKILL |
| 4 | 19 mil e-mails limpos em uma noite (Gmail e Agenda) | LIMPAR |
| 5 | O Claude montou meu post no Canva (MCP) | MCP |
| 6 | Não joga fora esse notebook | NOTEBOOK |
| 7 | O notebook do lixo roda seus apps? | QUAL APP? |
| 8 | Ressuscitei um tablet abandonado | TABLET |
| 9 | O Claude virou meu professor | PROFESSOR |
| 10 | Quem tá roubando seu Wi-Fi? (**padrão atual**) | WIFI |
| 11 | Cortes de live de GTA VI (paleta especial, não é padrão) | GTA |
| 12 | Claude Code de graça com o OmniRoute (352 provedores) | CLAUDE |

Mantenha esta tabela atualizada a cada vídeo novo.

## Mapa do repositório

| Pasta | O que é |
|---|---|
| `skill/` | Skill `cobaia-dev-videos`, como instalar e o histórico de pedidos do Luis |
| `motor/` | Código que renderiza: animação, áudio, fontes, ícones, render, encode, voz |
| `referencia/` | Dia 10 v3 (padrão) e Dia 9 |
| `capas/` | Gerador das capas e destaques na identidade nova |
| `roteiro/` | Banco de ganchos virais e plano dos 30 dias |
| `estudos/` | Análise das 5 referências de fluid motion e o teste de síntese aprovado |
| `exemplos/` | Dia 11 (troca de paleta GTA). Não é padrão |
| `formatos/` | `motion/` (atual) e `face-cam/` (reservado, o Luis vai definir) |
| `producoes/` | Um diretório por vídeo novo |

## Fora deste repositório, de propósito

- A identidade antiga (Dias 1 a 8 no estilo de antes, biblioteca `telas/`, modelo HyperFrames, "constituição"). Ela está no repositório antigo `kit-edicao-` e **não vale mais**. Não use nada de lá.
- MP4 pesados e os vídeos antigos.
