#!/usr/bin/python3

"""This is a script thats starts a Flask web applications"""


from flask import Flask

blog_app = Flask(__name__)


@blog_app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@blog_app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@blog_app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    underscore_by_a_space = text.replace('_', ' ')
    return "C" + underscore_by_a_space


if __name__ == "__main__":
    blog_app.run(host="0.0.0.0", port=5000)
