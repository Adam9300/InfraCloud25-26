FROM python:3.10-alpine

WORKDIR /app

COPY app.py .

RUN mkdir -p /var/log/myapp

ENTRYPOINT ["python", "app.py"]
