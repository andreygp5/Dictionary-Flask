from app import app
from flask import url_for, redirect


@app.route('/')
def index():
    return redirect(url_for('enter_words.index'))