from app import db
from werkzeug.security import generate_password_hash


class User(db.Model):

    login = db.Column(db.String(200), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(4))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = generate_password_hash(self.password)

    def __repr__(self):
        return '{0} - {1}'.format(self.login, self.password)


class Words(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    eng_word = db.Column(db.String(200), nullable=False)
    ru_word = db.Column(db.String(200), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '{0} - {1}'.format(self.eng_word, self.ru_word)

class LearningWords(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    eng_word = db.Column(db.String(200), nullable=False)
    ru_word = db.Column(db.String(200), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '{0} - {1}'.format(self.eng_word, self.ru_word)

# admin = User(login="andreygp555@gmail.com", password="admin")
# db.session.add(admin)
# db.session.commit()
# print(User.query.all())