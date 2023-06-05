from flask import Flask
from quote_client import quote_client

app = Flask(__name__)

@app.route("/")
def quotes():
    qc = quote_client.quote_client()
    quote = qc.randomquote()
    return quote

if __name__ == "__main__":
    app.run()