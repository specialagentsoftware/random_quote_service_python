from flask import Flask
from quote_client import quote_client

"""instantiate flask app and the quote client for use"""
app = Flask(__name__)
qc = quote_client.quote_client()


@app.route("/")
def quotes():
    """quote function runs when web root is called by an http request.
    The function utilizes the quote client and calls the randomquote method
    and returns the formatted string to the requestor
    """
    quote = qc.randomquote()
    return quote


if __name__ == "__main__":
    app.run()
