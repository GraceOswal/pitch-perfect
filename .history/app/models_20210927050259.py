from . import db

# connect class user to pitchperfect database

class User(db.Model):
    __table__ = 'users'
    id = d