#!/usr/bin/env python3
"""Flask Module handling Babel"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration for Flask-Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False
app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    """Retrieves locale and returns best_mathc languae
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_ = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """Returns Template 1-index"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
