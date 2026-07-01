import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "The Real Deployment with Self hosted platform"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)