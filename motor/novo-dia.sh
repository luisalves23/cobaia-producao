#!/bin/bash
# Cria producoes/diaNN/ com o motor e a base limpa (motor/base/, Dossiê Cobaia 2.0).
# uso (na raiz do repositório): bash motor/novo-dia.sh 12
set -e
N=$(printf "%02d" "$1"); n=$((10#$N))
ROOT=$(cd "$(dirname "$0")/.." && pwd); D="$ROOT/producoes/dia$N"
[ -e "$D" ] && { echo "já existe: $D"; exit 1; }
mkdir -p "$D/fonte" "$D/postar" "$D/storyboard" "$D/brutos"
cp "$ROOT"/motor/{lib.js,synth.py,icons.js,perfil.jpg} "$D/fonte/"
sed 's#fonts/#../../../motor/fonts/#' "$ROOT/motor/fonts.css" > "$D/fonte/fonts.css"
# base limpa do Dossiê Cobaia 2.0 (motor/base/), tirada do acabamento do Dia 10 v3 sem a cena de calendário,
# sem gancho palavra por palavra, sem frase de envio no CTA e já com frase-tema fixa, selo e legenda.
# Trocar todas as cenas e tempos; manter paleta, leque, elemento vermelho, chamada final, roxo e loop.
for f in dNN.html dNNlegenda.js aNN.py; do sed "s/dNN/d${n}/g; s/aNN/a${n}/g; s/DIA NN/DIA $N/g" "$ROOT/motor/base/$f" > "$D/fonte/${f/NN/$n}"; done
echo "const CHUNKS=[];" > "$D/fonte/d${n}chunks.js"
cat > "$D/LEIAME.md" <<EOT
# Dia $n

- Roteiro aprovado: (link ou texto)
- Palavra-chave:
- Voz: gravada pelo Luis / IA
- Música: sintetizada / faixa (crédito em CREDITOS.txt)
- Tema passa nas 4 perguntas do dossiê? (ganho, público, prova, mandaria)
- Próximo episódio (card final):
- Página no ar: (link)
- Gravações recebidas (tela, aparelho, rosto): em \`brutos/\` (fora do git)

Antes de entregar: checklist da seção 11 do \`DOSSIE.md\` preenchido. Depois de 48 h: \`revisao-48h.md\` (seção 12).

Arquivos: \`corrente.md\` (veio de → vira), \`mapa-musica.md\`, \`storyboard/\`, \`fonte/\`, \`postar/\` (MP4 fora do git).
EOT
touch "$D/CREDITOS.txt"
echo "criado: $D"
