FROM python:3.12-slim

RUN pip install poetry

COPY pyproject.toml poetry.lock /src/ 

WORKDIR /src

RUN poetry config virtualenvs.create false && poetry install --no-root 

COPY . /src/
CMD ["python","main.py"]