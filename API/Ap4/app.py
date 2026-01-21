from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_BASE_URL = "https://jsonplaceholder.typicode.com"


@app.route("/", methods=["GET", "POST"])
def index():
    user_data = None
    error = None

    if request.method == "POST":
        user_id = request.form.get("user_id")

        if not user_id.isdigit():
            error = "Voer een geldig nummer in."
        else:
            response = requests.get(f"{API_BASE_URL}/users/{user_id}")

            if response.status_code == 200:
                user_data = response.json()
            else:
                error = "Gebruiker niet gevonden."

    return render_template("index.html", user=user_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
