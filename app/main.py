from app import app

from enter_words.blueprint import enter_words
from learn_words.blueprint import learn_words
from all_words.blueprint import all_words


app.register_blueprint(enter_words, url_prefix='/enter-words')
app.register_blueprint(learn_words, url_prefix='/learn-words')
app.register_blueprint(all_words, url_prefix='/all-words')


if __name__ == "__main__":
    app.run()