from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_materialize import Material
from sassutils.wsgi import SassMiddleware

db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)
  Material(app)

  app.config.from_object(config_options[config_name])

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/sass', 'static/css', '/static/css')
  })
  db.init_app(app)

  return app
