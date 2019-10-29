from . import auth
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, login_required, logout_user
from .forms import RegistrationForm, LoginForm
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

@auth.route('/login')
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.stories'))

  form = LoginForm()
  
  return render_template('auth/login.html', form=form)

@auth.route('/login', methods=['POST'])
def login_post():
  email = request.form.get('email')
  password = request.form.get('password')

  user = User.query.filter_by(email=email).first()

  if not user or not check_password_hash(user.password, password):
    flash('please check your login details and try again')

    return redirect(url_for('auth.login'))

  login_user(user, remember=True)

  return redirect(url_for('main.stories'))

@auth.route('/register')
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.stories'))

  form = RegistrationForm()

  return render_template('auth/register.html', form=form)

@auth.route('/register', methods=['POST'])
def register_post():
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')
  password_confirm = request.form.get('password_confirm')

  user = User.query.filter_by(email=email).first()

  if user:
    flash('Email address already exists')
    return redirect(url_for('register'))

  if password != password_confirm:
    flash('make sure your passwords match')
    return redirect(url_for('register'))
  
  new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
  db.session.add(new_user)
  db.session.commit()

  login_user(new_user, remember=True)

  return redirect(url_for('main.stories'))

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))
