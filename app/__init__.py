from flask_sqlalchemy import SQLAlchemy
from flask.app import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


from config import Config
from flask import app

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

#create db instance
def create_app(config_name):
    app = Flask(__name__)

# initialize init file
bootstrap.init_app(app)
db.init_app(app)

#