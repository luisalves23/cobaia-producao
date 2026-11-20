# Changelog

Entradas novas no topo. Formato: `## AAAA-MM-DD · conta · título`, o pedido do Luis e o que mudou. Nunca apague entradas.

## 2026-11-20 · principal · Dia 13 (Anti-Robô) e trilha sempre para cima

Pedido do Luis: fazer o vídeo do Dia 13 com o áudio e o roteiro dele (humanizador Anti-Robô, palavra HUMANO), com capa, legendas e comentários; os 3 primeiros segundos com motion caprichado para viralizar; trilha que avança junto com o texto, sempre com o clima lá em cima, nunca depressiva, descendo e subindo de forma suave e orgânica. Palavra do vídeo: orgânico. Pediu o vídeo pronto para postar.

O que mudou:
- `producoes/dia13/`: roteiro, palavras grandes, corrente, mapa da música, cenas (gancho: robô quadrado imprimindo texto de robô, o pedido entra na boca dele e no "humanizar" ele derrete num rosto humano, as linhas rígidas viram ondas e sai um anel de onda), trilha future bass em fá maior a 128 BPM, capa e textos do post. Link do guia usado: https://cobaia-dev.vercel.app/humano/ (página ainda não estava no ar quando o vídeo foi feito).
- `motor/synth.py`: instrumento `supersaw` (acorde de serras desafinadas); linha no `motor/LEIAME.md`.
- `skill/SKILL.md`, seção 9: regra "clima sempre para cima".
- `capas/capas.html`: capa do Dia 13.
- `CLAUDE.md`: Dia 13 na tabela do que já foi feito.

## 2026-11-19 · principal · Dia 12: gancho mais viral

Pedido do Luis: os 3 primeiros segundos ficaram fracos; reformular o que aparece para ficar mais viral. Ele aprovou o storyboard novo e pediu o vídeo fechado para postar.

O que mudou:
- `producoes/dia12/fonte/d12.html`: gancho v2. O Claude abre acorrentado com um cadeado de $200/mês (a bola vermelha é a fechadura), a bola vira um corte que estoura as correntes no "de graça", o cadeado cai e entra o $0 verde; soco de zoom no frame 0, no corte e no "GIGANTE" (barra engrossa e atravessa a tela com linhas de velocidade). Loop volta para o Claude acorrentado.
- `producoes/dia12/fonte/a12.py`: sons do gancho (correntes, corte, elos estourando, cadeado, $0 carimbado).

## 2026-11-19 · principal · Dia 12 com a trilha suave aprovada

Pedido do Luis: aprovou o áudio com a trilha suave (mesma base, mudanças em rampa de 0,3 s no corte de cada cena) e pediu para trocar no vídeo. Salvou a skill atualizada na conta.

O que mudou:
- `producoes/dia12/fonte/a12.py`: agora é a versão suave (tabela `ST` por cena); vídeo final reencodado.
- `producoes/dia12/mapa-musica.md`: versão final descrita.
- `skill/SKILL.md`, seção 9: o `a12.py` do Dia 12 vira o modelo aprovado de trilha dinâmica.

## 2026-11-19 · principal · Fade da trilha no tempo da transição

Pedido do Luis: o fade-in e fade-out de 1 a 2 s está grande demais; tem que ser menor e combinar com o vídeo.

O que mudou:
- `skill/SKILL.md`, seção 9: o fade e as rampas de volume e filtro duram o mesmo que a transição da cena (0,2 a 0,5 s) e terminam junto com ela; crescendo longo só em build.

## 2026-11-19 · principal · Trilha dinâmica com fades, sem degraus

Pedido do Luis: não gostou das três opções da trilha montanha-russa. Ficaram "cheias de degrau", trocando de música de uma vez e com o volume cortando de baixo para alto. Deveria ter fade-in e fade-out nas trocas. O Dia 12 fica com a música original. Nos próximos vídeos a trilha tem que ser dinâmica, mas com transições suaves.

O que mudou:
- `skill/SKILL.md`, seção 9: a regra virou "trilha dinâmica, mas suave" (crossfade de 1 a 2 s, rampas de volume e filtro de pelo menos 1 s, uma base que evolui, amostra de áudio antes de montar no vídeo).
- `motor/LEIAME.md`: `trilha.py` marcado como experimental e reprovado.
- `producoes/dia12/fonte/a12.py` voltou para a trilha original; `mapa-musica.md` registra a tentativa reprovada.

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
