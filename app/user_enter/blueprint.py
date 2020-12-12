from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash, g
from flask_login import UserMixin, current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from models import Words, User
from app import login_manager, db
from .email_verification import SendVerificationCode
import view


user_enter = Blueprint('user_enter', __name__, template_folder='templates')

class UserClass(UserMixin):
    pass

@login_manager.user_loader
def user_loader(login):
    login = User.query.filter_by(login=login).first().login
    if login is None:
        return
    user = UserClass()
    user.id = login
    return user

# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized'

@user_enter.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        login = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(login=login).first()
        if user is None:
            flash("Wrong email")
            return render_template("user_enter/sign_in.html")
        if check_password_hash(user.password, password):
            user = UserClass()
            user.id = login
            login_user(user)
            return redirect(url_for('enter_words.index'))
        else:
            flash("Wrong password")
            render_template("user_enter/sign_in.html")
    return render_template("user_enter/sign_in.html")

@user_enter.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    return render_template("user_enter/sign_up.html")

@user_enter.route('/verify_code', methods=['POST'])
def verify_code():
    entered_code = request.form['code']
    code = User.query.filter_by(login=request.form['email']).first()
    if entered_code == code.code:
        return "Successful registration"
    else:
        return "Wrong code"

@user_enter.route('/verify_email', methods=['POST'])
def verify_email():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(login=email).first()
    if user is not None:
        return 'Status - Email already exists'
    else:
        sender = SendVerificationCode(email)
        sender.send_code()
        temp_user = User(login=email, password=password,
                        code=sender.get_code())
        db.session.add(temp_user)
        db.session.commit()
        return 'Status - The message was sent'

@user_enter.route('/sign_out')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("enter_words.index"))

@user_enter.route('/protected')
@login_required
def protected_page():
    return 'Logged in as: ' + current_user.id