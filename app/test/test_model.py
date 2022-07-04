import unittest
from app.model.user import User
from mongoengine import connect, disconnect


class TestModelUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        disconnect()
        print("Connecting to mongomock")
        connect('test_mongoengine', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def testModelUser(self):
        userID = User.objects.count() + 1
        userPassword = User.generateHashPassword('eatiplaner01!123')

        user = User(
            ID=userID,
            username='eatiplaner01',
            password=userPassword,
            first_name='eatiplaner',
            last_name='01',
            email='eatiplaner01@gmail.com'
        )
        user.save()

        inserted_user = User.objects().first()
        assert inserted_user.username == 'eatiplaner01'
        assert inserted_user.password == userPassword
