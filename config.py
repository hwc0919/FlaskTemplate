import json
import os

import mysql.connector

basedir = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(basedir, '.env.json')) as f:
        envs = json.load(f)
    new_envs = envs[os.getenv('FLASK_CONFIG') or 'development']
    os.environ.update(new_envs)
except Exception:
    print('Load .env.json Failed.')
    raise


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(20)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{passwd}@{host}:{port}/{dbname}?charset=utf8mb4'.format(
        username=os.environ.get('DBUSER'),
        passwd=os.environ.get('DBPASSWD'),
        host=os.environ.get('DBHOST'),
        port=os.environ.get('DBPORT'),
        dbname=os.environ.get('DBNAME'))

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
