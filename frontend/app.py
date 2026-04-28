from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend-service:5000/api")

@app.route("/", methods=["GET", "POST"])
def index():
    backend_message = None

    try:
        res = requests.get(BACKEND_URL, timeout=3)
        backend_message = res.json().get("message")
    except Exception:
        backend_message = "Backend unavailable"

    if request.method == "POST":
        name = request.form.get("name", "world")
        return render_template("message.html", name=name, backend_message=backend_message)

    return render_template("index.html", backend_message=backend_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)