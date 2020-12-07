from app import db


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
