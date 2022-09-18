#!/usr/bin/python3
<<<<<<< HEAD
"""This script starts a Flask web application"""
from flask import Flask, escape, render_template
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


@app.route('/number/<int:num>', strict_slashes=False)
def route_number(num):
    """Return only if num is a int"""
    return "{} is a number".format(escape(num))


@app.route('/number_template/<int:num>', strict_slashes=False)
def route_template(num):
    """Return a file HTML only if num is a int"""
    return render_template("5-number.html", n=num)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""

from flask import Flask
from flask import render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_a_number(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', num=n)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
