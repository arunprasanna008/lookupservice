FROM python:3.8-alpine

MAINTAINER "Arun <arunprasanna008@gmail.com>"

COPY . /app

WORKDIR /app

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

CMD python main.py

EXPOSE 50