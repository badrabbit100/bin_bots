# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
RUN pip3 install telethon
RUN pip3 install python-dotenv
COPY . .
ENTRYPOINT ["bash","start.sh"]

