from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash, g
from flask_login import UserMixin, current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from models import Word, User, Dictionary
from app import login_manager, db
from .email_verification import SendVerificationCode
import view


user_enter = Blueprint('user_enter', __name__, template_folder='templates')

class UserClass(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    db_user = User.query.filter_by(email=email).first()
    if db_user.email is None:
        return
    user = UserClass()
    user.id = db_user.email
    user.default_dict = db_user.default_dict
    return user

@user_enter.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user is None:
            flash("Wrong email")
            return render_template("user_enter/sign_in.html")
        if check_password_hash(user.password, password):
            user = UserClass()
            user.id = email
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
    code = User.query.filter_by(email=request.form['email']).first()
    if entered_code == code.code:
        def_dict = Dictionary(dict_name="All Words", user_id=code.id)
        db.session.add(def_dict)
        code.default_dict.update = "All Words"
        db.session.commit()
        return "Successful registration"
    else:
        user = User.query.filter_by(email=request.form['email']).first()
        db.session.delete(user)
        db.session.commit()
        return "Wrong code"

@user_enter.route('/verify_email', methods=['POST'])
def verify_email():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()
    if user is not None:
        return 'Status - Email already exists'
    else:
        sender = SendVerificationCode(email)
        sender.send_code()
        temp_user = User(email=email, password=password,
                        code=sender.get_code())
        db.session.add(temp_user)
        db.session.commit()
        return 'Status - The message was sent'

@user_enter.route('/sign_out')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("enter_words.index"))


@user_enter.route('/profile', methods=["GET"])
@login_required
def profile():

    user = User.query.filter_by(email=current_user.id).first()
    dicts = Dictionary.query.filter_by(user_id=user.id).all()

    return render_template("user_enter/profile.html", dicts=dicts)


@user_enter.route('/create-new-dict', methods=["POST"])
@login_required
def create_new_dict():

    dict_name = request.form["dict-name"]
    user = User.query.filter_by(email=current_user.id).first()
    dict = Dictionary(dict_name=dict_name, user_id=user.id)
    db.session.add(dict)
    db.session.commit()

    return "Created successfully"

@user_enter.route('/delete-dict', methods=["POST"])
@login_required
def delete_dict():

    dict_name = request.form["dict-name"]
    user = User.query.filter_by(email=current_user.id).first()
    dict = Dictionary.query.filter_by(user_id=user.id, dict_name=dict_name).first()
    db.session.delete(dict)
    db.session.commit()

    return "Deleted successfully"