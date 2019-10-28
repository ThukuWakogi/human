import os

class Config:
  '''
  general class configurations
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
  '''
  production configuration child class

  args:
    config: parent configuration class with general configuration settings
  '''

  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# class TestConfig(Config):
#   '''
#   test configutration child class

#   args:
#     config parent configuration class with general configuration settings
#   '''

#   SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')

class DevConfig(Config):
  '''
  development configutration child class

  args:
    config parent configuration class with general configuration settings
  '''

  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

  DEBUG = True


config_options = {
  'development': DevConfig,
  'production': ProdConfig
}
