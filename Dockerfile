FROM python:3.8.15-slim-bullseye

COPY . /code

WORKDIR /code

CMD ["python", "main.py"]