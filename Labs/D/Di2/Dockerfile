FROM alpine:3.19

# Python + Flask via apk (GEEN pip, GEEN apt)
RUN apk add --no-cache python3 py3-flask

WORKDIR /app

COPY app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
