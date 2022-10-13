#!/usr/bin/python3
<<<<<<< HEAD
"""This script starts a Flask web application"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', defaults={'state_id': 'None'}, strict_slashes=False)
@app.route('/states/<path:state_id>', strict_slashes=False)
def states(state_id):
    """Returns a rendered html template at the /states route,
    listing all states and cities"""
    states = storage.all('State').values()
    for state in states:
        if escape(state_id) == state.id:
            return render_template('9-states.html',
                                   states=state, name=state.name)
    return render_template('9-states.html', states=states, name=state_id)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
=======
"""
starts a Flask web application
"""

from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_given_id(id):
    states = storage.all("State")
    found_state = ""
    for s_id in states:
        if s_id == id:
            found_state = states[s_id]

    return render_template('9-states.html',
                           state=found_state)


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5