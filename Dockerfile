FROM python:3.12

WORKDIR /app

COPY . /app

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt
