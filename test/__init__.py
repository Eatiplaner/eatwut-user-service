import unittest
from mongoengine import connect, disconnect


class BaseMock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        connect('test_mongoengine', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()
