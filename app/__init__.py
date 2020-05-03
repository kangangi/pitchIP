from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    #Creating app configuration
    app.config.from_object(config_options[config_name])

    #initializing flask extenxtion
    db.init_app(app)
