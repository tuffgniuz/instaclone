FROM python:3.10.2-slim-buster

ENV PYTHONBUFFERED=1

WORKDIR /src

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000


