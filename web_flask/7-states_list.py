#!/usr/bin/python3
"""
script that starts a Flask web application:
    You must use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    Routes:
    /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted by
name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from models.state import State
from models import storage
from flask import Flask, escape, request
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def sts_list():
    sts = storage.all(State).values()
    return render_template("7-states_list.html", sts=sts)


@app.teardown_appcontext
def td(self):
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
