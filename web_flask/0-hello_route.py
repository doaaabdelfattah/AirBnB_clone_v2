#!/usr/bin/python3
'''
Flask Module
'''
from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def homepage():
    ''' return home message'''
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
