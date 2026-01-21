from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Pf3 microservice",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.route("/info")
def info():
    return jsonify({
        "name": "Eigen microservice",
        "version": "1.0",
        "author": "devasc"
    })

if __name__ == "__main__":
    app.run(debug=True)
