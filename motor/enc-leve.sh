#!/bin/bash
# Versão leve (< 25 MB) a partir do MP4 HQ.
# uso: bash motor/enc-leve.sh cobaia-diaNN-final.mp4 cobaia-diaNN-final-leve.mp4
set -e
IN=$1; OUT=$2
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
VB=$(python3 -c "print(int(192000/$DUR-160))")
MAX=$(python3 -c "print(int($VB*1.5))")
LOG=$(mktemp -u)
ffmpeg -v error -y -i "$IN" -c:v libx264 -preset slow -b:v ${VB}k -maxrate ${MAX}k -bufsize $((MAX*2))k -pix_fmt yuv420p -profile:v high -g 60 -pass 1 -passlogfile $LOG -an -f mp4 /dev/null
ffmpeg -v error -y -i "$IN" -c:v libx264 -preset slow -b:v ${VB}k -maxrate ${MAX}k -bufsize $((MAX*2))k -pix_fmt yuv420p -profile:v high -g 60 -pass 2 -passlogfile $LOG -c:a aac -b:a 160k -movflags +faststart "$OUT"
rm -f $LOG*
ls -lh "$OUT"
