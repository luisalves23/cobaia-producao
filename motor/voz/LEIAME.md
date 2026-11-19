# Voz: do arquivo do Luis até o vídeo

Aqui está o que foi feito nos Dias 9, 10 e 11, medido nos arquivos deles. Não é um processo novo.

## 1. Entrada

- **O Luis sempre manda o áudio pronto da fala**, como arquivo anexado na conversa (mp3 ou wav). Ele gera no ElevenLabs, com a voz dele clonada, ou grava no celular. **O Claude nunca gera nem clona voz.**
- Junto com o áudio vem o **texto aprovado do roteiro**. É dele que saem as palavras, a grafia e os tempos.
- Chegou o arquivo, não pergunte "gravada ou IA". Só pergunte se o áudio não vier.
- **Trabalhe sempre numa cópia do upload.** Copie para `producoes/diaNN/fonte/voz.mp3` (ou `voz.wav`) e aponte a variável `VOZ` do `aNN.py` para essa cópia.

## 2. Áudio do ElevenLabs (o caso dos Dias 9, 10 e 11)

**O arquivo entra no `aNN.py` como chegou.** Não tem corte de silêncio, nem atempo, nem normalização antes. O ElevenLabs já entrega a fala sem silêncios longos: as pausas do Dia 10 têm cerca de 0,25 s.

Medido no `referencia/dia10-v3/fonte/voz.mp3`: é o upload original do Luis, sem nenhuma mudança (byte a byte igual ao anexo de 17/11). Tem −18,4 LUFS, pico −0,9 dBFS, 52,43 s, mono, 44,1 kHz, 128 kbps. A fala vai de **0,06 s a 52,26 s**, porque o `a10.py` coloca a voz no tempo 0 do vídeo. O vídeo tem 54,8 s, e depois da fala vem a tela roxa sem fala (52,4 a 54,4 s) e o quique do loop.

O que acontece com a voz, em ordem, sem nenhum passo manual:
1. **`aNN.py`**, ao decodificar com ffmpeg, aplica `highpass=f=80, equalizer=f=3500:t=q:w=1:g=1.5, acompressor=threshold=-20dB:ratio=2.5:attack=5:release=80`, em mono e 48 kHz.
2. **`mix()` do `synth.py`** normaliza a voz pelo RMS (`voz / rms × 0,12`). Por isso o volume de entrada não muda o equilíbrio voz × música × efeitos. A música entra com ducking pela voz (até −50%).
3. **`write()`** normaliza o pico do mix em 0,89.
4. **`enc.sh`** aplica `loudnorm=I=-14:TP=-1.2:LRA=11` no MP4 final.

**Volume de entrada:** não existe um alvo obrigatório, porque o passo 2 iguala. O único ponto que depende do volume é o compressor do passo 1 (limiar de −20 dB). Os uploads do ElevenLabs usados ficaram entre −19 e −17 LUFS, com pico perto de −1 dBFS, e o compressor trabalhou assim. Se um arquivo chegar bem mais baixo (o do Dia 8 tem −23,8 LUFS), o resultado continua equilibrado, só que o compressor atua menos. Para ficar igual ao Dia 10, traga a cópia para perto de −18 LUFS com ganho linear antes de entrar no `aNN.py`:
```bash
ffmpeg -i upload.mp3 -af "volume=5.8dB" -ar 44100 -ac 1 voz.wav   # 5,8 dB = −18 − (−23,8); confira o pico ≤ −1 dBFS
```
Saída: o `aNN.py` lê qualquer formato e converte para 48 kHz mono. O mix final é WAV estéreo de 48 kHz.

**"corrigindo":** não aparece em áudio do ElevenLabs. Se o Luis errar, ele gera a frase de novo e manda o arquivo inteiro.

**Variação do Dia 9:** a voz tinha −24,9 LUFS e pico −4,2 dBFS, e o `a9.py` usou uma cadeia um pouco mais forte: `highpass 80, afftdn nf=-25, EQ 3,5 kHz +2 dB, EQ 250 Hz −2 dB, acompressor −20 dB 3:1`. O padrão é o do Dia 10.

## 3. Gravação de celular

Nos Dias 9, 10 e 11 a voz veio do ElevenLabs. A receita de celular é a que estava na skill (seção 9) e nos scripts, dos vídeos anteriores:

1. **Palavras com tempo:** `transcribe.py` (faster-whisper small, cpu int8, pt). Sem whisper, veja a seção 5.
2. **Corte de silêncio, "corrigindo" e tratamento:** `cut3.py` faz tudo de uma vez:
   - corte por energia: limiar `thr` (−32 dB quando o fundo está em ~−40 dB), janela de 10 ms, junta falas com intervalo < 0,12 s, margens de 0,05 s antes e 0,09 s depois, fade de 8 ms, pausas longas viram `gap` (0,16 s) e pausas dramáticas ficam como foram definidas em `pauses`;
   - **"corrigindo":** corte do início da tentativa errada até o fim de "corrigindo", com `drop` (índices das palavras) ou `droptime` (segundos). Se a mesma frase foi gravada duas vezes, fique com a que bate com o roteiro;
   - cadeia: `highpass=f=80, afftdn=nf=-30, equalizer 250 Hz −2 dB, equalizer 4 kHz +2 dB, acompressor −20 dB 3:1 attack 5 release 80, atempo=speed (padrão 1,08, até ~1,18 em gravação limpa), loudnorm I=-16:TP=-1.5:LRA=7`, saída WAV 48 kHz mono;
   - remapeia os tempos das palavras para o áudio cortado e acelerado.
3. Confira com uma nova transcrição (prompt neutro). Depois a voz entra no `aNN.py` como no caso 2.

## 4. Formato de entrada e saída dos scripts

| Script | Entra | Sai |
|---|---|---|
| `transcribe.py MODELO audio.wav palavras.json` | WAV 16 bits mono; variável `PROMPT` opcional | `palavras.json` = `[{"w","s","e","p"}]` |
| `align.py` (sem argumentos) | na pasta atual: `texto.txt` (o roteiro aprovado, exatamente como foi falado) e `bruto.wav` (WAV 16 bits mono, **48 kHz**) | `align.json` = `{"W":[{"w","s","e"}], "M":[[início, fim] dos trechos com fala]}` e uma linha por frase no terminal |
| `cut.py TEMPO` | na pasta atual: `align.json` e `bruto.wav` | `cut.wav` (cortado), `voz_editada.wav` (tratado + atempo TEMPO + loudnorm −16) e `palavras.json` com os tempos remapeados |
| `cut3.py in48.wav words.json out.wav words_out.json cfg.json` | WAV 48 kHz, palavras `[{"w","s","e"}]` e cfg `{"thr":-32,"gap":0.16,"speed":1.08,"pauses":{"idx":seg},"drop":[[a,b]],"droptime":[[s,e]]}` | `out.wav` tratado e `words_out.json` = `{"words":[{"w","s","e","i"}],"dur","orig"}` |

O `align.py` divide o texto em frases pela pontuação, acha os trechos com fala por energia (−40 dB, junta vãos < 0,12 s) e casa frases com trechos por programação dinâmica, com a duração esperada por sílaba. Siglas contam como mais sílabas: MCP vale 3 e OpenAI vale 4; acrescente as novas na função `syl`.

## 5. Sem faster-whisper (plano B)

**Áudio do ElevenLabs:** o plano B é o caminho normal, e foi o que se fez no Dia 11 (o whisper estava bloqueado na rede). Exemplo de ponta a ponta com a voz do Dia 11:
```bash
mkdir -p /tmp/al && cd /tmp/al
# texto.txt = roteiro aprovado, uma linha, com a pontuação
ffmpeg -v error -i <cópia do upload> -ac 1 -ar 48000 -c:a pcm_s16le bruto.wav
python3 <repo>/motor/voz/align.py      # gera align.json
```
Conferido em 19/11: as 177 palavras do Dia 11 saíram em média a 0,13 s (no máximo 0,7 s) dos tempos usados no vídeo (`exemplos/dia11-paleta-gta/palavras-voz-dia11.json`). Como a voz do ElevenLabs não é cortada, os tempos de `align.json` já são os tempos do vídeo. Não rode o `cut.py` nesse caso.

**Gravação de celular com "corrigindo" e sem whisper:** sem transcrição não dá para achar o "corrigindo" com segurança. O alinhamento por texto não conhece a frase errada. Faça assim:
1. Peça ao Luis o segundo aproximado de cada "corrigindo" (ou que mande a frase certa num arquivo à parte).
2. Tire esses intervalos da cópia com ffmpeg (ex.: `-af "aselect='not(between(t,12.4,15.1))',asetpts=N/SR/TB"`), em WAV 48 kHz.
3. Rode o `align.py` sobre o áudio já limpo, com o roteiro aprovado no `texto.txt`.
4. Converta `align.json` → lista `W` e rode o `cut3.py` com `drop` vazio para cortar os silêncios e tratar.
5. Confira os pontos de corte em quadros curtos do storyboard antes de seguir.
