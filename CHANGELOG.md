# Changelog

Entradas novas no topo. Formato: `## AAAA-MM-DD · conta · título`, o pedido do Luis e o que mudou. Nunca apague entradas.

## 2026-11-19 · principal · Trilha montanha-russa

Pedido do Luis: a música do Dia 12 estava boa, mas estática, "mais do mesmo", numa linha reta. Ele quer a trilha como uma montanha-russa, acompanhando a narrativa e o motion, e músicas mais eletrônicas. Pediu opções para ouvir. No mesmo dia: a etiqueta de $20 do gancho passou a ficar pendurada no ícone do Claude (só neste vídeo).

O que mudou:
- `motor/trilha.py` (novo): curva de energia, drops com riser, paradas, impactos, subida de tom; estilos electro, dnb e futurebass.
- `skill/SKILL.md`, seção 9: regra da trilha montanha-russa reescrita (mínimo de drops, parada e vale; três estilos; mandar as três quando o Luis não escolher).
- `motor/LEIAME.md`: linha do `trilha.py`.
- `producoes/dia12/fonte/a12.py`: música trocada pelo `trilha.py` com a narrativa do Dia 12 (`ESTILO=` escolhe a versão); `d12.html`: etiqueta pendurada no ícone do Claude.

## 2026-11-19 · principal · Dia 12 (OmniRoute) e peças novas no motor

Pedido do Luis: o Dia 12 virou o roteiro dele sobre o OmniRoute (Claude Code de graça com limite gigante), com o áudio inteiro do ElevenLabs e a última frase regravada para a palavra-chave CLAUDE. Ele aprovou o storyboard e pediu para produzir.

O que mudou:
- `producoes/dia12/`: roteiro, voz montada (frase corrigida colada no fim; pausas acima de 0,3 s encurtadas e atempo 1,03 para caber em 60 s), palavras grandes, corrente, mapa da música, cenas, trilha electro 124 BPM em lá menor, capa e textos do post. Os roteiros que o Luis descartou ficaram em `producoes/dia12/roteiros-descartados/`.
- `motor/icons.js`: logo do GitHub (`GITHUB_PATH`, octicon mark-github).
- `motor/folha.py`: rótulo dos quadros nomeados `tNNN.NN` (o `storyboard.cjs` grava assim) deixou de quebrar a folha.
- `capas/capas.html`: capa do Dia 12.
- `CLAUDE.md`: Dia 12 na tabela do que já foi feito.

## 2026-11-19 · principal · Como se sabe o texto falado sem whisper

Pergunta do Luis (conta secundária sem reconhecimento de voz): como a conta principal lê o conteúdo de um áudio anexado e o que fazer quando vem só o áudio.

O que mudou:
- `motor/voz/LEIAME.md`: seção "Como se sabe o que está sendo dito". O Claude não ouve o anexo. O whisper também está bloqueado na conta principal (huggingface.co recusado). O texto sempre vem do roteiro aprovado, e o `align.py` acha os tempos. Também explica o que fazer quando vem só o áudio, como ligar a transcrição se a rede liberar e onde está o Dia 8 (não transcrito, não guardado aqui).

## 2026-11-19 · principal · Fluxo real de áudio e montagem das palavras grandes

Pedido do Luis (dúvidas da conta secundária): o áudio da fala sempre vem pronto dele (ElevenLabs com a voz clonada ou celular), anexado e junto com o texto aprovado; o Claude nunca gera voz e só pergunta se o arquivo não vier. Documentar a receita de tratamento, o volume de entrada do `a10.py`, como montar o `dNNchunks.js` e o plano B sem faster-whisper. Orientação dele: entregar o que já fazemos, sem mudar o processo.

O que mudou:
- `motor/voz/LEIAME.md` (novo): entrada, ElevenLabs (como chegou, sem corte, sem atempo; medidas do Dia 10: −18,4 LUFS, pico −0,9 dBFS, fala de 0,06 a 52,26 s), cadeia do `aNN.py` → `mix()` → `enc.sh`, volume de entrada, receita de celular com "corrigindo", entradas e saídas de `transcribe.py`, `align.py`, `cut.py` e `cut3.py`, e o plano B testado na voz do Dia 11.
- `motor/LEIAME.md`: passo a passo de como os blocos do `dNNchunks.js` são escritos (agrupamento, fonte por bloco, destaques 1/2/3), tirado do Dia 10.
- `skill/SKILL.md`: seção 1 (voz), seção 9 (entrada, ElevenLabs e sem whisper), seção 10 item 2 e o caminho da foto de perfil na seção 7.
- `CLAUDE.md`: etapas 3 e 4 do pipeline, "Como trabalhar com o Luis" e a ordem de leitura.

## 2026-11-19 · principal · Histórico de pedidos e protocolo de mudança

Pedido do Luis: tudo o que ele pediu e mudou até hoje precisa estar no repositório, para a outra conta partir de onde a principal está, e ela precisa saber o que fazer quando receber um pedido de mudança.

O que mudou:
- `skill/historico-pedidos.md`: todos os pedidos desde 01/11, com o que foi substituído pela identidade nova.
- `CLAUDE.md`: seções "Quando o Luis pedir uma mudança" e "Como trabalhar com o Luis"; histórico na ordem de leitura.
- `PROMPT-NOVA-CONTA.md`: o prompt de entrada para uma conta nova.

## 2026-11-19 · principal · Criação do repositório

Pedido do Luis: juntar tudo o que aprendemos e melhoramos na produção (identidade nova, skill, arquivos) num repositório privado, para que a conta secundária produza com o mesmo resultado e as duas contas sigam sincronizadas. Deixar de fora a identidade antiga; o Dia 11 (GTA VI) entra só como exemplo de troca de paleta; preparar espaço para vídeos com rosto.

O que entrou:
- `skill/SKILL.md`: skill `cobaia-dev-videos` como estava em 18/11 (Dia 10 v3 aprovado), com os caminhos trocados para o repositório e as seções 0, 9, 10, 11, 12 e 13 reescritas para o fluxo que de fato gerou o Dia 10 v3 (canvas + Playwright + áudio sintetizado), no lugar da biblioteca `telas/` e do HyperFrames. Liquid Glass ficou registrado como regra do site e opcional no vídeo, porque o Dia 10 v3 não usa vidro.
- `motor/`: `lib.js`, `synth.py`, `icons.js`, fontes, foto de perfil, render, storyboard, folha de contato, encode HQ e leve, `novo-dia.sh` e ferramentas de voz.
- `referencia/dia10-v3/` (padrão, conferido: quadro e mix reproduzem o vídeo aprovado) e `referencia/dia09/`.
- `capas/`: gerador da identidade nova (conferido: reproduz a capa do Dia 10) e as capas dos Dias 1 a 10.
- `roteiro/`: banco de ganchos virais (09/11) e o plano dos 30 dias (cópia do Doc).
- `estudos/`: análise das 5 referências e o teste 07 na identidade nova.
- `exemplos/dia11-paleta-gta/`, `formatos/motion/`, `formatos/face-cam/` (reservado) e `producoes/`.
