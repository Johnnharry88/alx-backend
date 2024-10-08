#!/usr/bin/env python3
""" Flask App that handles template """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Prints Hello world page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
