from flask import Flask
from file_client import file_client

app = Flask(__name__)

@app.route("/")
def hello_world():
    fc = file_client
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()