import os

class Config:
    debug = True
    SECRET_KEY = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TDATABASE_URI = 'postgresql+psycopg2://graceinyua:gee@localhost/pitch-perfect'
