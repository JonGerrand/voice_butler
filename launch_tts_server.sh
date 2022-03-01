#! /bin/bash

cd /home/jonathan/Data/Personal/repos/voice_butler

docker build --tag tts-server:latest .

docker run --rm -p 5002:5002 -e "HOME=${HOME}" \
            -v "$HOME:${HOME}" \
            -w "${PWD}" \
            --user "$(id -u):$(id -g)" \
            tts-server:latest