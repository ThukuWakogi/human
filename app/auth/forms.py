from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
  name = StringField('name', validators=[Required()])
  email = StringField('email', validators=[Required()])
  password = PasswordField('password', validators=[Required(), EqualTo('password_confirm', message='passwords must match')])
  password_confirm = PasswordField('confirm password', validators=[Required()])
  submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
  email = StringField('email', validators=[Required()])
  password = PasswordField('password', validators=[Required()])
  submit = SubmitField('Log in')
