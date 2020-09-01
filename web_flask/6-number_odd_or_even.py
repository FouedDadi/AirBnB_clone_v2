#!/usr/bin/python3
"""
script that starts a Flask web application:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of
        the text variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
"""


from flask import Flask, escape, request
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def H1(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def HTML(n):
    return render_template("6-number_odd_or_even.html", n=n)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
