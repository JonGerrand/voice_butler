#! /bin/bash

cd /media/jonathan/Data/jonathan/Personal/repos/voice_butler

prompt="$(python generate_butler_prompt.py)"

curl -G --output - --data-urlencode "text=$prompt" 'http://localhost:5002/api/tts' | aplay