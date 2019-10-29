from . import main
from flask import render_template, request, redirect, url_for
from .. import db
from ..models import Blog, Comment
from .forms import StoryForm
from flask_login import login_required, current_user

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
  print('-' * 50)
  print(stories)

  return render_template('stories.html', stories=stories, number_of_stories=len(stories))

@main.route('/story/add')
@login_required
def story_add():
  '''
  loads blog form
  '''

  form = StoryForm()

  return render_template('story-form.html', form=form)

@main.route('/story/add', methods=['POST'])
@login_required
def story_post():
  '''
  picks blog data and pushes it to database
  '''

  title = request.form.get('title')
  body = request.form.get('body')

  new_blog = Blog(title=title, body=body, created_by=current_user.id)
  db.session.add(new_blog)
  db.session.commit()

  return redirect(url_for('main.stories'))
