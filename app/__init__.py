from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)
    db.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Will add the views and forms

    return app