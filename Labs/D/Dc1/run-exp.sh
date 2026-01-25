#!/bin/bash
set -e

IMAGE_NAME="myapp-exp"
CONTAINER_NAME="myapp-running"
NET_NAME="myapp-net"

# Cleanup oude container
docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true

# Maak network als het nog niet bestaat
docker network inspect "$NET_NAME" >/dev/null 2>&1 || docker network create "$NET_NAME" >/dev/null

# Temp build context
rm -rf tempdir
mkdir -p tempdir/templates tempdir/static

cp app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# Dockerfile met HEALTHCHECK + non-root user
cat > tempdir/Dockerfile <<'DOCKER'
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
DOCKER

# Build image
cd tempdir
docker build -t "$IMAGE_NAME" .
cd ..

# Host volume voor logs
mkdir -p logs

# Run container met env vars + volume + custom network + port mapping
docker run -d \
  --name "$CONTAINER_NAME" \
  --network "$NET_NAME" \
  -p 8080:8080 \
  -e APP_MESSAGE="Hallo uit mijn Run Containers experiment!" \
  -e APP_LOG_PATH="/var/log/myapp/app.log" \
  -v "$(pwd)/logs:/var/log/myapp" \
  "$IMAGE_NAME"

# Toon status
docker ps --filter "name=$CONTAINER_NAME"
echo
echo "Test:"
curl -s http://127.0.0.1:8080/health