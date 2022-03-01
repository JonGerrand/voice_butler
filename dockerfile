FROM continuumio/miniconda3

RUN apt update

RUN apt install build-essential libsndfile1 -y

RUN pip install -U tts

ENTRYPOINT [ "tts-server", "--model_name"]

CMD [ "tts_models/en/vctk/vits" ]
