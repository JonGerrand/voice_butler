#! /bin/bash

# Load Python environment
source /home/jonathan/Data/anaconda3/etc/profile.d/conda.sh
conda activate tts

cd /media/jonathan/Data/jonathan/Personal/repos/voice_butler
prompt="$(python3 generate_butler_prompt.py)"
curl -G --output - --data-urlencode "text=$prompt" 'http://localhost:5002/api/tts?speaker_id=229' > /tmp/time.wav
mplayer -ao pulse /tmp/time.wav

# Voices to consider: 
# VCTK - p229 - Irish man
# VCTK - p323 - French man