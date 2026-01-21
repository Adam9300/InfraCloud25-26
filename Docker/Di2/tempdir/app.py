import os
from uuid import uuid4
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image

app = Flask(__name__)

UPLOAD_DIR = "uploads"
RESULT_DIR = "results"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

ALLOWED = {".jpg", ".jpeg", ".png", ".webp"}

def allowed_ext(filename: str) -> bool:
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED

@app.route("/", methods=["GET"])
def index():
    # toont laatste resultaat als die in query params zit
    orig = request.args.get("orig")
    result = request.args.get("result")
    return render_template("index.html", orig=orig, result=result)

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(url_for("index"))

    f = request.files["file"]
    if not f.filename:
        return redirect(url_for("index"))

    if not allowed_ext(f.filename):
        return "Unsupported file type", 400

    _, ext = os.path.splitext(f.filename.lower())
    fid = str(uuid4())
    orig_name = f"{fid}{ext}"
    res_name = f"{fid}_gray{ext}"

    orig_path = os.path.join(UPLOAD_DIR, orig_name)
    res_path = os.path.join(RESULT_DIR, res_name)

    f.save(orig_path)

    # grayscale
    img = Image.open(orig_path)
    gray = img.convert("L")
    gray.save(res_path)

    return redirect(url_for("index", orig=orig_name, result=res_name))

@app.route("/uploads/<path:filename>")
def get_upload(filename):
    return app.send_static_file(f"../{UPLOAD_DIR}/{filename}")

@app.route("/results/<path:filename>")
def get_result(filename):
    return app.send_static_file(f"../{RESULT_DIR}/{filename}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
