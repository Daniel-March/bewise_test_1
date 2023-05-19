FROM python:3.11

ENV HOST=0.0.0.0
ENV PORT=8000

COPY ./ /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT python3.11 -u main.py