from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']='sqllite:///pitch'
app.config['SECRET_KEY']='vivioonana123'


db = SQLAlchemy(app)

from app import views
    