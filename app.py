from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, the content of my configuration is: "+os.environ.get("CONTENT")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
