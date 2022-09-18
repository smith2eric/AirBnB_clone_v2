#!/usr/bin/python3
<<<<<<< HEAD
"""This script starts a Flask web application"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """Return two words"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    """Return a word"""
    return "HBNB"


@app.route('/c/<path:subpath>', strict_slashes=False)
def route_c(subpath):
    """Return subpath"""
    return "C {}".format(escape(subpath).replace('_', ' '))


@app.route('/python', defaults={'subpath': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:subpath>', strict_slashes=False)
def route_python(subpath):
    """Return subpath"""
    return "Python {}".format(escape(subpath).replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
def python():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def Python_is_magic(text):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
