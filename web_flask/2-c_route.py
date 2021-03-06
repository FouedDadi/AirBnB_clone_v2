#!/usr/bin/python3
"""
script that starts a Flask web application:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of
        the text variable (replace underscore _ symbols with a space )
"""


from flask import Flask, escape, request

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
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
