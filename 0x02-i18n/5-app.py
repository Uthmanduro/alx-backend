#!/usr/bin/env python3
""" Basic Babel setup with jinja Version: 3.1.2"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ returns a user dictionary or None"""
    user = request.args.get('login_as')
    if user:
        return users.get(int(user))
    else:
        return None


@app.before_request
def before_request():
    """executes before request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ gets locale from request and determines the best match"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ index route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
