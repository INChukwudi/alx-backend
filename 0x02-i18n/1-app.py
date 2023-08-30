#!/usr/bin/env python3

"""
Module that contains definitions for application routes
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Class bearing config attributes for the application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello_world():
    """
    Returns the basic index page for the application
    :return: 1-index.html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
