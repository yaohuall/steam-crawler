FROM python:3.10-slim-buster
LABEL author="yaohual"
LABEL version="1.0"

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential default-libmysqlclient-dev \
  && pip install --no-cache-dir --upgrade pip setuptools wheel

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt && pip install --no-cache-dir Scrapy==2.7.1

