from . import main
from flask import render_template
from .. import db
from ..models import Blog

@main.route('/')
def index():
  '''
  loads landing page
  '''

  return render_template('index.html')

@main.route('/stories')
def stories():
  '''
  fetches stories and loads them into stories.html
  '''

  stories = Blog.query.all()

  return render_template('stories.html', stories=stories, number_of_stories=len(stories))
