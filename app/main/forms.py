from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Email, EqualTo

class StoryForm(FlaskForm):
  title = StringField('title', validators=[Required()])
  body = TextAreaField('body', validators=[Required()])
  submit = SubmitField('submit')
