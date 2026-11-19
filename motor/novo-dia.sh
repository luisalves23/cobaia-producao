#!/bin/bash
# Cria producoes/diaNN/ com o motor e a base do Dia 10 v3.
# uso (na raiz do repositório): bash motor/novo-dia.sh 12
set -e
N=$(printf "%02d" "$1"); n=$((10#$N))
ROOT=$(cd "$(dirname "$0")/.." && pwd); D="$ROOT/producoes/dia$N"
[ -e "$D" ] && { echo "já existe: $D"; exit 1; }
mkdir -p "$D/fonte" "$D/postar" "$D/storyboard"
cp "$ROOT"/motor/{lib.js,synth.py,icons.js,perfil.jpg} "$D/fonte/"
sed 's#fonts/#../../../motor/fonts/#' "$ROOT/motor/fonts.css" > "$D/fonte/fonts.css"
# base de estrutura (trocar todas as cenas; manter paleta, palavras, leque, elemento vermelho, chamada final, roxo e loop)
sed "s/d10chunks.js/d${n}chunks.js/; s#// DIA 10 — detetive de Wi-Fi.*#// DIA $n — base copiada do Dia 10 v3: refazer as cenas#" "$ROOT/referencia/dia10-v3/fonte/d10.html" > "$D/fonte/d$n.html"
echo "const CHUNKS=[];" > "$D/fonte/d${n}chunks.js"
sed "s/d10chunks.js/d${n}chunks.js/g" "$ROOT/referencia/dia10-v3/fonte/a10.py" > "$D/fonte/a$n.py"
cat > "$D/LEIAME.md" <<EOT
# Dia $n

- Roteiro aprovado: (link ou texto)
- Palavra-chave:
- Voz: gravada pelo Luis / IA
- Música: sintetizada / faixa (crédito em CREDITOS.txt)

Arquivos: \`corrente.md\` (veio de → vira), \`mapa-musica.md\`, \`storyboard/\`, \`fonte/\`, \`postar/\` (MP4 fora do git).
EOT
touch "$D/CREDITOS.txt"
echo "criado: $D"
