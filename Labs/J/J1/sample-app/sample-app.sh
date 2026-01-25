#!/bin/bash

mkdir -p tempdir/{templates,static}

cp sample_app.py tempdir/
cp templates/index.html tempdir/templates/
cp static/style.css tempdir/static/

echo "FROM python:3.10-alpine" > tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t sampleapp .
docker run -d -p 8080:8080 --name samplerunning sampleapp

