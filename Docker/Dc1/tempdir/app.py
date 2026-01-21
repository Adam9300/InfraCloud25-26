from flask import Flask, request, render_template
import os
from datetime import datetime

app = Flask(__name__)

MESSAGE = os.getenv("APP_MESSAGE", "Hello from container!")
LOG_PATH = os.getenv("APP_LOG_PATH", "/var/log/myapp/app.log")

def log_line(line: str):
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a") as f:
            f.write(f"{datetime.utcnow().isoformat()}Z {line}\n")
    except Exception:
        pass

@app.route("/")
def main():
    log_line(f"GET / from {request.remote_addr}")
    return render_template("index.html", message=MESSAGE)

@app.route("/health")
def health():
    return "OK\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)