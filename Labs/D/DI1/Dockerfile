FROM python:3.10-alpine

RUN pip install --no-cache-dir flask

WORKDIR /app
COPY sample_app.py /app
COPY templates /app/templates
COPY static /app/static

EXPOSE 8080

CMD ["python3", "sample_app.py"]

