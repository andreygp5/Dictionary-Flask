from flask import Blueprint, render_template, request, redirect, url_for, g
from flask_login import login_required, current_user
from models import User, Dictionary

from app import db

 
learn_words = Blueprint('learn_words', __name__, template_folder='templates')

@learn_words.route('/', methods=('GET', 'POST'))
@login_required
def index():
    user = User.query.filter_by(email=current_user.id).first()
    dicts = Dictionary.query.filter_by(user_id=user.id).all()

    return render_template('learn_words/index.html', dicts=dicts)