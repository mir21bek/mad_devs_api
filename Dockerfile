FROM python:3.12

WORKDIR /app

COPY req.txt .

RUN  pip install --upgrade pip

RUN pip install --no-cache-dir -r req.txt

COPY . /app
