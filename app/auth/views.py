from . import auth
from flask import render_template, redirect, url_for
from flask_login import current_user
from .forms import RegistrationForm, LoginForm

@auth.route('/login')
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.stories'))

  form = LoginForm()
  
  return render_template('auth/login.html', form=form)

@auth.route('/register')
def register():
  if current_user.is_authenticated:
    return redirect(url_for('main.stories'))

  form = RegistrationForm()

  return render_template('auth/register.html', form=form)
