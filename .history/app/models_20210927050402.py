from . import db

# connect class user to pitchperfect database

class User(db.Model):
    __table__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column()