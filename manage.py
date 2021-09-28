
from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Post, Comment
import app
from flask_migrate import Migrate

app = create_app()

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

migrate = Migrate(app, db)
manager.add_command('db')

@manager.shell
def add_shell_context():
    return {'app': app, 'db' : db, 'User' : User, 'Post' : Post, 'Comment' : Comment }

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


if __name__ == '__main__':
    manager.run()