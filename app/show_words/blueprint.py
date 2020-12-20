from flask import Blueprint
from flask import render_template, request
from flask_login import login_required, current_user

from models import Word, Dictionary, User
from app import db
import view


show_words = Blueprint('show_words', __name__, template_folder='templates')

@show_words.route('/<string:dict_name>?<int:page>', methods=('POST', 'GET'))
@login_required
def index(dict_name, page):
    if request.method == 'POST':
        button = request.form['btn']
        if button == 'clear':
            Word.query.delete()
            db.session.commit()
        if button == 'delete_words':
            delete_words = request.form.getlist('checked_words')
            for word in delete_words:
                delete_word = Word.query.filter_by(eng_word=word).first()
                db.session.delete(delete_word)
                db.session.commit()
    
    user = User.query.filter_by(email=current_user.id).first()
    dictionary = Dictionary.query.filter_by(user_id=user.id, dict_name=dict_name).first()
    words = dictionary.words
    words = words.paginate(page=page)
    
    return render_template('show_words/index.html', words=words, dict_name=dict_name)