# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local code imports
from config import app_config

# db initialization
db = SQLAlchemy()

login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config = True)
    """
    Load configuration from instance/config.py
    """
    app.config.from_object(app_config[config_name])
    """
    Load configuration from config.py
    """
    app.config.from_pyfile('config.py')
    """
    Create the db object
    """
    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"
    
    migrate = Migrate(app, db)
    
    from app import models
    #BluePrints Registration
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
