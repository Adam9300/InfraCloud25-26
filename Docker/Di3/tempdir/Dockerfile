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
