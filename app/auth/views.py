from flask import render_template,redirect,url_for,flash, request
from app.models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, login_required, logout_user
from . import auth 
from ..email import mail_message

#Views
@auth.route('/register', methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    title  = "New User"
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        new_user = User(email = email,username = username, password =password)
        new_user.save_user()

        mail_message("Welcome to Pitcher", "email/welcome_user", new_user.email, user = new_user)
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html', registration_form = form)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    title = 'Pitcher login'

    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        remember = form.remember_me.data

        user = User.query.filter_by(email = user_email).first()

        if user is not None and user.verify_password(user_password):
            login_user(user,remember)
            flash("Welcome to Pitch Perfect")
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("Invalid username or pasword")
    return render_template("auth/login.html", login_form = form,title = title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))