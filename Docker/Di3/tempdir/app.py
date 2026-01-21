import os
import sqlite3
from datetime import datetime, timezone
from uuid import uuid4

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
from PIL import Image

APP_PORT = int(os.environ.get("PORT", "8080"))

# Persistente paden (werken lokaal én in Docker met volume mount)
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.getcwd(), "data"))
DB_PATH = os.environ.get("DB_PATH", os.path.join(DATA_DIR, "images.db"))
UPLOAD_DIR = os.path.join(DATA_DIR, "uploads")
RESULT_DIR = os.path.join(DATA_DIR, "results")

ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_EXPERIMENTS = {"grayscale"}

app = Flask(__name__)

def ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs(RESULT_DIR, exist_ok=True)

def db_connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def db_init():
    ensure_dirs()
    with db_connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_name TEXT NOT NULL,
                stored_name   TEXT NOT NULL,
                result_name   TEXT NOT NULL,
                experiment    TEXT NOT NULL,
                client_ip     TEXT,
                created_at    TEXT NOT NULL
            );
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_images_created_at ON images(created_at);")
        conn.commit()

def allowed_file(filename: str) -> bool:
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED_EXT

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def process_image(in_path: str, out_path: str, experiment: str):
    img = Image.open(in_path)

    if experiment == "grayscale":
        out = img.convert("L")
        out.save(out_path)
        return

    raise ValueError("Unknown experiment")

@app.before_request
def _startup():
    # Zorgt dat DB/dirs bestaan vóór de eerste request
    if not getattr(app, "_db_ready", False):
        db_init()
        app._db_ready = True

@app.route("/", methods=["GET"])
def index():
    # Laat laatste 5 records zien
    with db_connect() as conn:
        rows = conn.execute(
            "SELECT * FROM images ORDER BY id DESC LIMIT 5"
        ).fetchall()
    return render_template("index.html", recent=rows)

@app.route("/gallery", methods=["GET"])
def gallery():
    with db_connect() as conn:
        rows = conn.execute(
            "SELECT * FROM images ORDER BY id DESC LIMIT 50"
        ).fetchall()
    return render_template("gallery.html", items=rows)

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file field", 400

    f = request.files["file"]
    if not f.filename:
        return "No selected file", 400

    experiment = (request.form.get("experiment") or "grayscale").strip().lower()
    if experiment not in ALLOWED_EXPERIMENTS:
        return f"Unsupported experiment: {experiment}", 400

    if not allowed_file(f.filename):
        return "Unsupported file type (use jpg/png/webp)", 400

    _, ext = os.path.splitext(f.filename.lower())
    fid = str(uuid4())
    stored_name = f"{fid}{ext}"
    result_name = f"{fid}_{experiment}{ext}"

    in_path = os.path.join(UPLOAD_DIR, stored_name)
    out_path = os.path.join(RESULT_DIR, result_name)

    f.save(in_path)

    try:
        process_image(in_path, out_path, experiment)
    except Exception as e:
        # Cleanup als processing faalt
        try:
            if os.path.exists(in_path):
                os.remove(in_path)
        except:
            pass
        return f"Processing failed: {e}", 500

    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    created_at = utc_now_iso()

    with db_connect() as conn:
        conn.execute("""
            INSERT INTO images (original_name, stored_name, result_name, experiment, client_ip, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (f.filename, stored_name, result_name, experiment, client_ip, created_at))
        conn.commit()

    return redirect(url_for("view_item_by_name", stored_name=stored_name))

@app.route("/view/<stored_name>", methods=["GET"])
def view_item_by_name(stored_name):
    with db_connect() as conn:
        row = conn.execute(
            "SELECT * FROM images WHERE stored_name = ?",
            (stored_name,)
        ).fetchone()

    if not row:
        abort(404)

    return render_template("view.html", item=row)

@app.route("/uploads/<path:filename>")
def uploads(filename):
    return send_from_directory(UPLOAD_DIR, filename)

@app.route("/results/<path:filename>")
def results(filename):
    return send_from_directory(RESULT_DIR, filename)

@app.route("/health", methods=["GET"])
def health():
    # simpele check voor container readiness
    return {"ok": True}, 200

if __name__ == "__main__":
    # Belangrijk voor Docker/VM: host=0.0.0.0
    app.run(host="0.0.0.0", port=APP_PORT, debug=False)
