#!/usr/bin/python3
'''
Flask Module
'''
from flask import Flask, render_template

web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def homepage():
    ''' return home message'''
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' return home message'''
    return "HBNB"


@web_app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    ''' return text '''
    text = text.replace("_", " ")
    return "C {}".format(text)


@web_app.route("/python", strict_slashes=False)
@web_app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    ''' return text '''
    text = text.replace("_", " ")
    return "Python {}".format(text)


@web_app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    ''' return number '''
    if isinstance(n, int):
        return"{} is a number".format(n)


@web_app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    ''' return html page '''

    return render_template("5-number_template.py", header_body="Number is {}".format(n))

if __name__ == "__main__":
    web_app.run(debug=True, host="0.0.0.0")
