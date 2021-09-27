
from app import create_app,db
from flask_script import Manager, Server
from app.models import User
import app

app = create_app()

manager = Manager(app)
manager.add_command('server', Server(use_debugger=True))

@manager.shell
def make_shell_context():
    return {'app': app, 'db' : db, 'User' : User }

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    manager.run()