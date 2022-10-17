FROM quay.io/centos/centos:stream8

RUN dnf -y module install python39 && dnf -y install python39 python39-pip
RUN mkdir /app
ADD https://raw.githubusercontent.com/arcalot/arcaflow-plugins/main/LICENSE /app
ADD metadata_plugin.py /app
ADD test_metadata_plugin.py /app
ADD requirements.txt /app
WORKDIR /app

RUN pip3 install -r requirements.txt

RUN mkdir /htmlcov
RUN pip3 install coverage
RUN python3 -m coverage run test_metadata_plugin.py
RUN python3 -m coverage html -d /htmlcov --omit=/usr/local/*

VOLUME /config

ENTRYPOINT ["python3", "/app/metadata_plugin.py"]
CMD []

LABEL org.opencontainers.image.source="https://github.com/arcalot/arcaflow-plugin-metadata"
LABEL org.opencontainers.image.licenses="Apache-2.0+GPL-2.0-only"
LABEL org.opencontainers.image.vendor="Arcalot project"
LABEL org.opencontainers.image.authors="Arcalot contributors"
LABEL org.opencontainers.image.title="Python Plugin Template"
LABEL io.github.arcalot.arcaflow.plugin.version="1"
