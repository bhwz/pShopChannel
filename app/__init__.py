import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

migrate = Migrate()
db = SQLAlchemy()
login = LoginManager()
csrf = CSRFProtect()


def create_app():
    app = Flask('pShopChannel', static_folder=f'{BASE_DIR}/static', static_url_path='',
                template_folder=f'{BASE_DIR}/templates')
    app.config.from_object('app.settings')

    register_extensions(app)

    from app.views import register_blueprints
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login.init_app(app)
    login.login_view = 'auth.login'
