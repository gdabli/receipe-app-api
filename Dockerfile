FROM python:3.7-alpine

ENV PYTHONBUFFERED 1

COPY ./requirementes.txt /requirementes.txt
RUN pip install -r /requirementes.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app/

RUN adduser -D adminuser
USER adminuser