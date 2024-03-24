#!/usr/bin/python3
'''
Flask Module
'''
from flask import Flask

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


if __name__ == "__main__":
    web_app.run(debug=True, host="0.0.0.0")
