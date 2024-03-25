#!/usr/bin/python3
'''
Flask Module
'''
from flask import Flask, render_template
from models import storage


web_app = Flask(__name__)


@web_app.route("/states", strict_slashes=False)
def states_():
    ''' return list of states'''
    states = storage.all('State')
    return render_template("9-states.html", state=states)


@web_app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    ''' return list of states with id'''
    for state in storage.all('State').values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@web_app.teardown_appcontext
def teardown(exc):
    '''when the application context is torn down
    '''
    storage.close()


if __name__ == "__main__":
    web_app.run(debug=True, host="0.0.0.0")
