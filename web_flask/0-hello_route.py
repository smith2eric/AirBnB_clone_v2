#!/usr/bin/python3
<<<<<<< HEAD
""" This script starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return two words"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
