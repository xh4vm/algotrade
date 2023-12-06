FROM python:3.10-slim AS notebook-builder

WORKDIR /opt
COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-dev \
     && pip install --upgrade pip \
     && pip install wheel && pip3 wheel -r requirements.txt --wheel-dir=/opt/wheels


FROM jupyter/datascience-notebook:python-3.10

USER root
COPY --from=notebook-builder /opt /opt

RUN apt-get update && apt-get install -y --no-install-recommends whois netbase

COPY requirements.txt ./

RUN pip install --no-index --find-links=/opt/wheels -r requirements.txt