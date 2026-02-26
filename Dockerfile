FROM python:3.12.8

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

CMD ["python", "test1.py"]
