#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """ Returns Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB """
    return "HBNB"


@app.route('/c/<path:text>', strict_slashes=False)
def c(text):
    """ Returns C with text passed to the URL """
    return "C {}".format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
