#!/bin/bash
set -e

rm -rf tempdir
mkdir -p tempdir/templates tempdir/static

cp app.py requirements.txt tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python:3.11-slim" > tempdir/Dockerfile
echo "WORKDIR /home/myapp" >> tempdir/Dockerfile
echo "COPY requirements.txt /home/myapp/" >> tempdir/Dockerfile
echo "RUN pip install --no-cache-dir -r requirements.txt" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t imgexp .

# stop + remove oude container indien aanwezig
docker rm -f imgexp-running >/dev/null 2>&1 || true

docker run -t -d -p 8080:8080 --name imgexp-running imgexp
docker ps -a | grep imgexp || true
