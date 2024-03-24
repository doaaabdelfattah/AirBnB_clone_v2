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


if __name__ == "__main__":
    web_app.run(debug=True, host="0.0.0.0")
