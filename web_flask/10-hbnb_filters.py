#!/usr/bin/python3
"""
script that starts a Flask web application:
    To load all cities of a State:
    If your storage engine is DBStorage, you must use cities relationship
    Otherwise, use the public getter method cities
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    Routes:
    /cities_by_states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted
    by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag:
    with the list
    of City objects linked to the State sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """[filters method]

    Returns:
        [html]: [html page]
    """
    sts = storage.all("State")
    cts = storage.all("City")
    amen = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", sts=sts,
                           cts=cts,
                           amen=amen)


@app.teardown_appcontext
def clos(self):
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
