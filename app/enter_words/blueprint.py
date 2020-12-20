from flask import Blueprint
from flask import render_template, request
from flask_login import login_required, current_user

from models import Word, User, Dictionary
from app import db


enter_words = Blueprint('enter_words', __name__, template_folder='templates')

@enter_words.route('/', methods=('GET', 'POST'))
@login_required
def index():

    user_email = current_user.id
    user = User.query.filter_by(email=user_email).first()
    dictionaries = Dictionary.query.filter_by(user_id=user.id)

    if request.method == 'POST':
        english_word = request.form['english_word']
        russian_translate = request.form['russian_translate']

        user = User.query.filter_by(email=user_email).first()

        word = Word(eng_word=english_word.lower().strip(), ru_word=russian_translate.lower().strip())
        dict_to_add = Dictionary.query.filter_by(user_id=user.id, dict_name=user.default_dict).first()
        dict_to_add.words.append(word)
        db.session.add(dict_to_add)
        db.session.commit()
        
    return render_template('enter_words/index.html', dictionaries=dictionaries)


@enter_words.route('/change-default-dict', methods=['POST'])
def change_default_dict():
    dict_to_change = request.form["dict"]
    user = User.query.filter_by(email=current_user.id).first()
    user.default_dict = dict_to_change
    db.session.commit()
    current_user.default_dict = dict_to_change
    return "Dictionary was changed successfully to {0}".format(dict_to_change)