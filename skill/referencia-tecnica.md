# Referência técnica da skill cobaia-dev-videos

Trechos tirados da `skill/SKILL.md` em 21/11/2026 para a skill caber no limite de tamanho. Continuam valendo; em conflito, o `DOSSIE.md` e a skill vencem.

## Áudio: gravação de celular

**Gravação de celular:**
1. WAV 48 kHz. Transcrição com faster-whisper (`motor/voz/transcribe.py`: modelo small, cpu int8, `language="pt"`, tempos por palavra, `initial_prompt` com os termos do canal). Se o download do modelo for bloqueado na rede, use o alinhamento pelo texto (abaixo).
2. Corte de silêncios (`motor/voz/cut3.py`): limiar relativo ao ruído (−32 dB quando o fundo está em ~−40 dB), janelas de 10 ms, junta falas com intervalo < 0,12 s, margens de 0,05 s antes e 0,09 s depois, fades de 8 ms. **O fim de cada frase vem do envelope de energia**, não do fim da palavra do whisper: sílabas finais fracas ("grá-tis", "impor-tam") somem com limiar alto. Não comprima pausas de vírgula em listas.
3. Tratamento: `highpass=f=80, afftdn=nf=-30, equalizer 250 Hz −2 dB, equalizer 4 kHz +2 dB, acompressor thr −20 dB ratio 3, atempo (até ~1,18 em gravação limpa), loudnorm I=-16`.
4. **"Corrigindo":** quando o Luis erra, ele fala "corrigindo" e repete. Corte do início da tentativa errada até o fim de "corrigindo". Se gravar a mesma frase duas vezes, fique com a que bate com o roteiro.
5. Corrija a transcrição pelo roteiro antes das legendas (ex.: "chefe" → "chef", "Tropic" → "Anthropic", "a risca" → "à risca"). Pausas dramáticas ficam definidas à mão onde o roteiro pedir, e os tempos das palavras são recalculados depois do corte e da aceleração.
6. Confira por nova transcrição com prompt neutro (um prompt com a frase faz o whisper pular a frase). Se a transcrição longa cortar uma sílaba, confira numa janela curta antes de mexer no mix.
7. Regravação parcial: mantenha a voz aprovada até o ponto de troca e anexe a parte nova, cada parte em −16 LUFS. Se houver risco de diferença de timbre, peça para regravar inteiro.

## Entrega: capa, site e PDF

13. **Capa 1080×1920 (identidade nova, 17/11):** gerador em `capas/capas.html` (`node shot_capas.cjs <saída>`; dia novo = entrada em `DAYS` + ilustração em `ILL`, e o número do dia na lista do `shot_capas.cjs`). Fundo preto com brilho vermelho e grão, HUD de cantos e barra de progresso da série; "DIA NN" Anton vermelho 132 px com "/30" apagado; gancho encurtado em duas linhas (serif itálico + Anton, palavra-chave vermelha, "Claude" laranja); cartão 900×700 com leque de 3 vermelhos e ilustração flat da coisa real, ponto vermelho guiando o olho; rodapé com foto + "+", "@cobaia.dev" e "comenta PALAVRA" em pílula vermelha. Tudo entre y 240 e 1680. Destaque do Instagram: ícone grande no círculo central com leque circular (`destaque(kind)`).
14. **Site (obrigatório, no ar antes de postar):** sempre que um vídeo for criado ou editado, atualize a página da palavra-chave e o calendário em cobaia-dev.vercel.app (repo `luisalves23/cobaia-site`; a Vercel publica a cada push na `main`): capa reduzida em `assets/img/capa-diaNN.jpg`, entrada em `DIAS` no `src/build.py`, miolo em `src/dias/<palavra>.html` com o guia prometido, `python3 src/build.py` e `node src/og.js`. Todo card e modal do site usa o Liquid Glass. Identidade nova: `.fan` (leque), `.okl` (certinho verde), `.pf` (foto com +), `em` serif em h1/h2, `.claude` laranja, fechamento roxo. `HOLD` tranca, `EARLY[n]` libera num horário (UTC), `?lab` mostra a prévia. Publicar na `main` só com o ok escrito do Luis (PR com a prévia antes).
15. **PDF da palavra-chave, só quando o Luis pedir:** páginas 1080×1920, 6 a 8 páginas (Playwright `page.pdf` com `printBackground`), fundo da marca, títulos em Anton, texto em Inter, pedidos ao Claude em bolhas vermelhas, passo a passo real conferido na ajuda do Claude (plano, nome da opção, botão), imagens só de frames do vídeo (nunca código), última página com a colinha e o convite pra marcar o @cobaia.dev, brilhos com `radial-gradient` (sem `filter: blur`).

## Exemplo de gancho denso (Dia 09)

Exemplo do Luis (Dia 09, "foi mal no Enem"): s1 prova do Enem minimalista sendo marcada e a nota caindo com números rolando rápido; s2 a prova vira uma caneta vermelha que escreve uma página num caderno branco pautado com espiral, rabisca, desenha, risca e reescreve; s3–4 a caneta vira uma nota 1000 gigante que encolhe e pousa na prova como nota escrita à mão, sublinhada como correção, com o gabarito cheio de certinhos verdes.

## Corrente do elemento vermelho do Dia 10

Dia 10: ponto do Wi-Fi → play → caneta no calendário → seta → sinal de atenção → cursor do prompt → escrita do Claude Code → logo → lupa → ponteiro → lupa → cereja → casa → bola da briga → seta 6→11 → ponteiro → carregando → Wi-Fi → + de seguir → coração → base do Wi-Fi → ralo → roxo sem bola → loop.

## Telas: detalhes de animação

- Só o conteúdo da tela, cantos levemente arredondados e sombra, **sem moldura** de monitor ou celular falso. Parece gravação de tela editada.
  - Entram giradas (rotateY 25 a 40°, escala .8) e assentam inclinadas (±6 a 8°).
  - **Zoom inclinado no ponto falado:** a cada clique ou detalhe, a tela inteira corre e inclina até o ponto (`foco()`, ~0,4 s). **Raramente a tela inteira**, só quando o assunto é geral. Anime a escala do contêiner, nunca amplie bitmap pequeno.
  - **Zoom na ênfase (pedido do Luis em 11/11):** onde a fala dá ênfase ou mostra algo, a câmera dá zoom nesse ponto, e os frames de aprovação já mostram esse zoom. Em demonstração de sistema ou app (vários apps abrindo, teste de velocidade, player), o zoom é **leve** (1,15 a 1,35x) e **acompanha o mouse**.
  - **Antes e depois lado a lado:** em comparação de velocidade, tela dividida com o jeito antigo travando (carregando, erro, fechando) e o novo abrindo na hora, cada lado com seu cronômetro.
  - **Cursor branco** guiando tudo o que é falado: vai até o item e clica com leve encolhida.
  - Pedido digitado no ritmo da fala, palavras-chave em vermelho; a legenda continua embaixo.
  - Em reprodução, fiel à tela real e aos números reais; fora da prova, telas de apoio podem ser genéricas.
  - **Cliques em sequência** (ex.: "Cancelar inscrição"): botão vermelho com texto branco; o cursor clica num, desce, clica no próximo; cada linha clicada vira "✓ Cancelada" e some; o zoom acompanha cada clique.

## Movimento: detalhes

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

## Áudio: alinhamento sem whisper

**Sem whisper:** `motor/voz/align.py` alinha pelo texto do roteiro (frases pela pontuação, programação dinâmica por duração esperada de sílaba, palavras distribuídas por sílaba; ajuste a contagem de siglas como MCP). Foi o caminho do Dia 11. Em voz do ElevenLabs os tempos já são os do vídeo; o `motor/voz/cut.py` (corte + atempo) só entra em gravação. Gravação com "corrigindo" sem whisper: plano B no `motor/voz/LEIAME.md`.

## Fundo: versão antiga

Versão antiga, para cartões e telas: gradiente radial escuro, grade de pontos rolando devagar, 2 blobs desfocados (vermelho .20, off-white .07), vinheta e grão muito leve (.03; chiado forte parece vídeo sem definição).

## Áudio: efeitos

**Efeitos que fogem do óbvio:** nada do whoosh, pop, ding e confete que todo vídeo com IA usa. Prefira sub_drop, reverse_swell, glass_chime, bloom, tape_whirl, tick_wood, power_down; e no visual, vinheta que respira na tensão, luz vazada na revelação, separação RGB na falha, linha de varredura, anel de onda e soco de zoom no drop.

**Efeitos ("chuva de dopamina"):** todos sincronizados com palavras ou eventos, gerados pelos instrumentos de foley do `motor/synth.py` (waterdrop, tink, glass, relay, keyclick, subdrop, swell, tapestop, pluck_bend etc.; lista no `motor/LEIAME.md`). As passagens alternam sons diferentes. Instrumento novo entra no `synth.py`, nunca solto dentro de um vídeo.

## Exemplos de flat minimalista

- **Explicar em flat minimalista (fora da prova):** prova do Enem = folha de prova de verdade, simplificada; mapa = papel que se desdobra e vira mapa tradicional com rotas, depois a bolinha entra nele e quica até uma bifurcação (um lado sem saída, outro no objetivo, com certo e errado); exercícios = lista estilo prova, um embaixo do outro, rolando, com opções A/B/C em barras arredondadas; professor = bonequinho minimalista com quadro, terno e gravata vermelha (chapéu de formatura não é professor).
