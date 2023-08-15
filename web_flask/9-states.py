#!/usr/bin/python3

"""This is a script thats starts a Flask web applications"""

from models import storage
from models.state import State
from flask import Flask, render_template

blog_app = Flask(__name__)


@blog_app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Responds with a message 'Hello HBNB!' to HTTP requests
    to the root URL ("/").
    """
    return "Hello HBNB!"


@blog_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Responds with a message 'HBNB' to HTTP requests to the '/hbnb' URL.
    """
    return "HBNB"


@blog_app.route("/c/<text>", strict_slashes=False)
def c_text(text="is cool"):
    """
    Responds with a modified text 'C <modified_text>' to requests
    to the '/c/<text>' route.
    """

    underscore_by_a_space = text.replace('_', ' ')
    return "C " + underscore_by_a_space


@blog_app.route("/python/", strict_slashes=False)
@blog_app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    Responds with a text 'Python <modified_text>'
    based on the provided text parameter.
    """
    underscore_by_a_space = text.replace("_", " ")
    return "Python " + underscore_by_a_space


@blog_app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@blog_app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_n(n):
    return render_template("5-number.html", number_t=n)


@blog_app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", number_t=n)


@blog_app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", states=storage.all(State))


@blog_app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    return render_template("/8-cities_by_states.html", sts=storage.all(State))


@blog_app.route("/states", strict_slashes=False)
def states():
    return render_template('9-states.html', states=storage.all(State))


@blog_app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    return render_template('9-states.html', state_c_id=storage.get(State, id))


@blog_app.teardown_appcontext
def teardown(e):
    storage.close()


if __name__ == "__main__":
    blog_app.run(host="0.0.0.0", port=5000)
