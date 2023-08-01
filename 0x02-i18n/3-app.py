#!/usr/bin/env python3
""" Basic Babel setup with jinja Version: 3.1.2"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ gets locale from request and determines the best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ index route"""
    home_title = _('Welcome to Holberton')
    home_header = _('Hello world!')
    return render_template('3-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run()
