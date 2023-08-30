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
    :return: 5-index.html template
    """
    return render_template('5-index.html')


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
