from . import db
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
class User(UserMixin, db.Model):
  '''
  maps to users table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), index=True, nullable=False)
  email = db.Column(db.String(255), index=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
  blogs = db.relationship('Blog', backref='blogs', lazy=True)

class Blog(db.Model):
  '''
  maps to blogs table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'blogs'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), index=True, nullable=False)
  body = db.Column(db.String(), index=True, nullable=False)
  created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
  user = db.relationship('User', backref='user', lazy=True)

class Comment(db.Model):
  '''
  maps to comments table in database

  Args:
    db.Model: class from which sqlAlchemy properties are inherited
  '''

  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key=True)
  blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
  title = db.Column(db.String(255), index=True, nullable=False)
  comment = db.Column(db.String(), index=True, nullable=False)
  deleted = db.Column(db.Boolean, unique=False, default=True)
  created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
