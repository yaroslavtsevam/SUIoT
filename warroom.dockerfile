ARG PY_VERSION=3.12.6


FROM python:${PY_VERSION}

RUN pip install uv

WORKDIR /app
COPY /warroom_app/requirements.lock ./
RUN uv pip install --no-cache --system -r requirements.lock

COPY /warroom_app/* .
#COPY main.py README.md ./
#COPY examples ./examples
#COPY website ./website
RUN mkdir /resources
COPY /warroom_app/docker-entrypoint.sh /resources
RUN chmod 777 /resources/docker-entrypoint.sh

EXPOSE 8182
ENV PYTHONUNBUFFERED=True

ENTRYPOINT ["/resources/docker-entrypoint.sh"]
CMD ["python", "main.py"]
