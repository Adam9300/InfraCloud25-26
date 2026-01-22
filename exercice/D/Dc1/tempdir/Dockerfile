FROM python:3.12-slim

RUN pip install --no-cache-dir flask \
 && useradd -m appuser

WORKDIR /home/appuser/myapp

COPY ./static ./static
COPY ./templates ./templates
COPY app.py .

EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health').read()"

USER appuser

CMD ["python3", "app.py"]
