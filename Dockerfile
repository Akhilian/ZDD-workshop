FROM tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11

COPY ./app /app

WORKDIR /app

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip install -r ./requirements.txt

ENV MODULE_NAME "presentation.api"
ENV VARIABLE_NAME "api"