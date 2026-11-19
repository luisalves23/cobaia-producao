#!/bin/bash
# enc.sh framesdir audio.wav out.mp4
ffmpeg -v error -y -framerate 30 -i $1/f%04d.jpg -i $2 -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -profile:v high -movflags +faststart -af "loudnorm=I=-14:TP=-1.2:LRA=11" -ar 48000 -c:a aac -b:a 256k -shortest $3
