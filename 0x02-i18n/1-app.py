#!/usr/bin/env python3
"""Flask Module handling Babel"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Returns Template 1-index"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
