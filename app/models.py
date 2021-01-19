from typing import Dict
from werkzeug.security import generate_password_hash

from app import db

from datetime import datetime


words = db.Table('words',
    db.Column('word_id', db.Integer, db.ForeignKey('word.id'), primary_key=True),
    db.Column('dict_id', db.Integer, db.ForeignKey('dictionary.id'), primary_key=True)
)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    code = db.Column(db.String(4))
    default_dict = db.Column(db.String(30))
    dicts = db.relationship('Dictionary', backref='user', lazy='dynamic')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = generate_password_hash(self.password)

    def __repr__(self):
        return '{0} - {1}'.format(self.email, self.id)

class Dictionary(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    dict_name = db.Column(db.String(30), nullable=False)
    add_time = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    words = db.relationship('Word', secondary=words, lazy='dynamic',
        backref=db.backref('dict_words', lazy='dynamic'))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '{0} - {1} - {2}'.format(self.dict_name, self.id, self.add_time)

class Word(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    base_word = db.Column(db.String(100), nullable=False)
    translation_word = db.Column(db.String(100), nullable=False)
    add_time = db.Column(db.DateTime, nullable=False, default=datetime.now())


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '{0} - {1}'.format(self.base_word, self.translation_word)

# db.create_all()

# word_wsr = Word.query.all()
# print(word_wsr)
# for word in word_wsr:
#     db.session.delete(word)
#     db.session.commit()

# some_word = Word.query.filter_by(eng_word='ttwwwwt').first()
# some_dict = Dictionary.query.filter_by(dict_name='All words').first()
# print(some_dict.words)
# some_dict.words.append(some_word)
# db.session.add(some_dict)
# db.session.commit()
# print(some_dict.words)

# test_word = Word(eng_word='ttwwwwt',ru_word='erwwwwrr')
# db.session.add(test_word)
# db.session.commit()


# t = Words.query.delete()
# db.session.delete(t)
# db.session.commit()
# print(t)
# admin = User(email="andriiglazkovstudy@gmail.com", password="qwerty")
# # all_words_dict = Dictionary(dict_name="test", user_id=1)
# db.session.add(admin)
# db.session.commit()
# print(User.query.all())

# from pickle import load

# with open('words.txt', 'rb') as f:
#     old_words = load(f)

# dict_to_append = Dictionary.query.filter_by(dict_name='All words').first()

# word = Word(id=old_words[0][0], eng_word=old_words[0][1], ru_word=old_words[0][2])
# dict_to_append.words.append(word)
# db.session.add(word)
# db.session.commit()