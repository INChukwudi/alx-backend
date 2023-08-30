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
    :return: 4-index.html template
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Checks for the current locale
    :return: str
    """
    language = request.args.get('locale')

    if language not in app.config["LANGUAGES"]:
        return request.accept_languages.best_match(app.config["LANGUAGES"])

    return language


if __name__ == '__main__':
    app.run()
