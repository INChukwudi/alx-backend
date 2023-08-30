#!/usr/bin/env python3

"""
Module that contains definitions for application routes
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.config.from_object('config.Config')

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the user id from the query parameter
    and checks against the users' dictionary
    :return: UserDetails : Dict | None : NoneObject
    """
    try:
        user_id = int(request.args.get('login_as'))
    except (ValueError, TypeError):
        return None

    try:
        return users[user_id]
    except KeyError:
        return None


@app.before_request
def before_request():
    """
    Method runs before every request
    and gets the user passed in the query parameter
    :return: None
    """
    g.user = get_user()


@app.route('/')
def hello_world():
    """
    Returns the basic index page for the application
    :return: 6-index.html template
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Checks for the current locale according to this priority order
    - Locale from URL parameters
    - Locale from user settings
    - Locale from request header
    - Default locale
    :return: the current locale: str
    """
    language = request.args.get('locale')
    if language in app.config["LANGUAGES"]:
        return language

    try:
        language = g.user["locale"]
        if language in app.config["LANGUAGES"]:
            return language
    except TypeError:
        pass

    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run()
