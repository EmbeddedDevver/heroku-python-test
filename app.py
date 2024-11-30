import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Heroku!"

if __name__ == "__main__":
    # Lees de poort uit de omgeving (standaard Heroku-port)
    port = int(os.environ.get("PORT", 5000))
    # Zorg ervoor dat de app op 0.0.0.0 draait
    app.run(host="0.0.0.0", port=port)