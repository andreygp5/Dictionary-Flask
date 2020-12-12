from app import app

from enter_words.blueprint import enter_words
from learn_words.blueprint import learn_words
from all_words.blueprint import all_words
from user_enter.blueprint import user_enter


app.register_blueprint(enter_words, url_prefix='/enter-words')
app.register_blueprint(learn_words, url_prefix='/learn-words')
app.register_blueprint(all_words, url_prefix='/all-words')
app.register_blueprint(user_enter, url_prefix='/user-enter')


if __name__ == "__main__":
    app.run()