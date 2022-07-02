from app import grpc
from app.main import create_app
import os
import unittest

from flask_script import Manager
from dotenv import load_dotenv
load_dotenv()


app = create_app(os.getenv('TARGET_ENV') or 'dev')
app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    grpc.grpc_serve(os.getenv('GRPC_PORT') or 50051)


@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
