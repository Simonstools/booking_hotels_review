FROM python:3.12

ENV POETRY_VERSION=2.0.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock entrypoint.sh ./

RUN poetry install --no-root

WORKDIR /app/src

COPY ./booking_service .

EXPOSE 8000

