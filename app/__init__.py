from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options




db=SQLAlchemy()

def create_app(config_name):

    app=Flask(__name__)

    # seting up configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # initializing flask extensions

    db.init_app(app)
    

    # Registering main Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    




    return app