FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /app


ENV FLASK_APP=app


EXPOSE 8000

CMD ["python", "app.py"]
