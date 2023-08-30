#!/usr/bin/env python3

"""
Module that contains definitions for application routes
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Returns the basic index page for the application
    :return: 0-index.html template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
