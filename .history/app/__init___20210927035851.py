from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

#create db instance
def create_app(config_name):
    app = Flask(__name__)

# initialize init file
bootstrap.init_app(app)
db.init_app