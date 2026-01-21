#!/bin/bash
set -e

APP_NAME="imgexp-sql"
CONTAINER_NAME="imgexp-sql-running"

rm -rf tempdir
mkdir -p tempdir/templates tempdir/static

cp app.py requirements.txt tempdir/.
cp -r templates/* tempdir/templates/
cp -r static/* tempdir/static/

# Dockerfile genereren (zoals in lab)
cat > tempdir/Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /home/myapp

COPY requirements.txt /home/myapp/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY app.py /home/myapp/

EXPOSE 8080
ENV PORT=8080
ENV DATA_DIR=/home/myapp/data
CMD ["python3", "/home/myapp/app.py"]
EOF

cd tempdir
docker build -t ${APP_NAME} .

# Oude container opruimen
docker rm -f ${CONTAINER_NAME} >/dev/null 2>&1 || true

# Data volume: sqlite + uploads/results blijven bewaard tussen restarts
mkdir -p ../data

docker run -d \
  -p 8080:8080 \
  -v "$(pwd)/../data:/home/myapp/data" \
  --name ${CONTAINER_NAME} \
  ${APP_NAME}

echo
echo "Running: http://localhost:8080"
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}"
