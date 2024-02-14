FROM python:3.10

ENV PYTHONWRITEBYECODE 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .