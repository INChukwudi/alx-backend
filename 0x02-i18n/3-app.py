#!/usr/bin/env python3

"""
Module that contains definitions for application routes
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.config.from_object('config.Config')


@app.route('/')
def hello_world():
    """
    Returns the basic index page for the application
    :return: 3-index.html template
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """
    Checks for the current locale
    :return: str
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run()
