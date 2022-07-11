#!/usr/bin/bash

MOV_PATH=$1

STREAM_INDEX=$(ffprobe -v error -of json "$MOV_PATH" -of json -show_entries "stream=index:stream_tags=language" -select_streams s | grep "index\":" | grep -o '[[:digit:]]\+')

SRT_PATH=/tmp/$(date +"%s").srt
ffmpeg -i "$MOV_PATH" -map "0:${STREAM_INDEX}" "$SRT_PATH"
python3 print.py $SRT_PATH > "${MOV_PATH}.SUBTITLES.txt"
echo $SRT_PATH
exit 0
