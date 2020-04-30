import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY =  os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'books.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class TestConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'test_books.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProductionConfig(Config):
    pass


create_config = dict(dev=DevelopmentConfig, test=TestConfig, prod=ProductionConfig)