#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def index() -> str:
    """handles / route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
