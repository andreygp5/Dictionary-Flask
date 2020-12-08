from flask import Blueprint
from flask import render_template, request
import sys
# sys.path.append(r"C:\Users\andre\Desktop\clone_test\English-Study-Flask\app")
from models import Words
from app import db


enter_words = Blueprint('enter_words', __name__, template_folder='templates')

@enter_words.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        english_word = request.form['english_word']
        russian_translate = request.form['russian_translate']
        word = Words(eng_word=english_word.lower().strip(), ru_word=russian_translate.lower().strip())
        db.session.add(word)
        db.session.commit()
        
    return render_template('enter_words/index.html')