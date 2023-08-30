#!/usr/bin/env python3

"""
Config class for flask application wide
"""


class Config(object):
    """
    Config class bearing attributes for the application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
