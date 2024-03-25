#!/usr/bin/python3
'''
Flask Module
'''
from flask import Flask, render_template
from models import storage


web_app = Flask(__name__)


@web_app.route("/states_list", strict_slashes=False)
def state_list():
    ''' return list of states'''
    states = storage.all('State')
    return render_template("7-states_list.html", states=states)


@web_app.route("/cities_by_states", strict_slashes=False)
def state_list():
    ''' return list of states'''
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@web_app.teardown_appcontext
def teardown(exc):
    '''when the application context is torn down
    '''
    storage.close()


if __name__ == "__main__":
    web_app.run(debug=True, host="0.0.0.0")
