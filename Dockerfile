FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt
COPY WorldOfBooks /WorldOfBooks

WORKDIR /WorldOfBooks

EXPOSE 8000

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /temp/requirements.txt

RUN adduser --disabled-password service-user
USER service-user
