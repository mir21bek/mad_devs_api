FROM python:3.12

WORKDIR /app

COPY . /app

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8080", "--reload"]
