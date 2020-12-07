from flask import Blueprint, render_template, request, redirect, url_for, g
from models import Words, LearningWords
from app import db


learn_words = Blueprint('learn_words', __name__, template_folder='templates')

def generate_learn_db(learning_words):
    LearningWords.query.delete()
    db.session.commit()
    for learn_word in learning_words:
        full_word = Words.query.filter_by(eng_word=learn_word).first()
        l_word = LearningWords(eng_word=full_word.eng_word, ru_word=full_word.ru_word)
        db.session.add(l_word)
        db.session.commit()

@learn_words.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        learning_words = request.form.getlist('checked_words')
        if learning_words is None:
            pass
        else:
            generate_learn_db(learning_words)
            return redirect(url_for('learn_words.learning'))
    words = Words.query.all()
    words.reverse()
    return render_template('learn_words/index.html', words=words)

@learn_words.route('/learning_words', methods=('GET', 'POST'))
def learning():
    learn_words = LearningWords.query.all()
    return render_template('learn_words/learning.html', learn_words=learn_words)