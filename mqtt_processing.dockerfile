FROM python:3.11.3-slim as builder

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN python -m pip install --upgrade pip

RUN python -m pip install --upgrade libsass

FROM python:3.11.3-slim as release
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ARG VERSION

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install nicegui[plotly,matplotlib]==1.4.25 itsdangerous isort docutils requests
RUN python -m pip install -r requirements.txt
WORKDIR /app

COPY mqtt_processing_app/* /app
#COPY examples ./examples
#COPY website ./website
RUN mkdir /resources
COPY mqtt_processing_app/docker-entrypoint.sh /resources
RUN chmod 777 /resources/docker-entrypoint.sh

EXPOSE 8080
ENV PYTHONUNBUFFERED True

ENTRYPOINT ["/resources/docker-entrypoint.sh"]
CMD ["python", "main.py"]
