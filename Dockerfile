FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PYTHON_VERSION=3.11
ENV DEPLOY_TIME=$(date)

EXPOSE 8080

