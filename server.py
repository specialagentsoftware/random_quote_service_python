from flask import Flask
from quote_client import quote_client

app = Flask(__name__)
qc = quote_client.quote_client()


@app.route("/")
def quotes():
    quote = qc.randomquote()
    return quote


if __name__ == "__main__":
    app.run()
