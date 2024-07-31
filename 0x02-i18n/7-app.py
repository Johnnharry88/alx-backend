#!/usr/bin/env python3
""" Flask app that handles user"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """Returns appropriate languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# app configuration for Flask
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


# User login Databas
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> str:
    """returns the users dictionary or none if no id"""
    id_login = request.args.get('login_as')
    if id_login:
        return users.get(int(id_login))
    return None


@app.before_request
def before_request() -> None:
    """Assigns user to a global variable g"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """gets the locale language specific to a user"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    header_locale = request.headers.get('locale')
    if header_locale in app.config['LANGUAGES']:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves timezone for web pages"""
    timezone = request.args.get('timezone').strip()
    if g.user and not timezone:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def index() -> str:
    """Returns the index page requested"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0', debug=True)
