# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# local code imports
from config import app_config

# db initialization
db = SQLAlchemy()

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
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
