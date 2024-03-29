from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_materialize import Material
from sassutils.wsgi import SassMiddleware
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)
  Material(app)

  app.config.from_object(config_options[config_name])

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

  app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'app': ('static/sass', 'static/css', '/static/css')
  })
  db.init_app(app)
  login_manager.init_app(app)

  return app
