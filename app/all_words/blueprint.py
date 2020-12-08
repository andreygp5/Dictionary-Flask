from flask import Blueprint

from flask import render_template, request
import sys
# sys.path.append(r"C:\Users\andre\Desktop\clone_test\English-Study-Flask\app")
from models import Words
from app import db
import view


all_words = Blueprint('all_words', __name__, template_folder='templates')

@all_words.route('/', methods=('POST', 'GET'))
def index():
    if request.method == 'POST':
        button = request.form['btn']
        if button == 'clear':
            Words.query.delete()
            db.session.commit()
        if button == 'delete_words':
            delete_words = request.form.getlist('checked_words')
            for word in delete_words:
                delete_word = Words.query.filter_by(eng_word=word).first()
                db.session.delete(delete_word)
                db.session.commit()
    
    page = request.args.get('page', 1, type=int)
    words = Words.query.paginate(page=page)
    
    return render_template('all_words/index.html', words=words)