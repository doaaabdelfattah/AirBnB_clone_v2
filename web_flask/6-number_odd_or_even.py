#!/usr/bin/python3
'''
Flask Module
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def homepage():
    ''' return home message'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' return home message'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    ''' return text '''
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    ''' return text '''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    ''' return number '''
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    ''' return html page '''
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    ''' return html page '''
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
