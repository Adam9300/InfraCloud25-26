from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("dashboard"))
        else:
            error = "Login mislukt"

    return render_template("login.html", error=error)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
