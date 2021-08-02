# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends firefox

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY /app .

CMD [ "python", "app.py"]
