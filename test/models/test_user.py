from app.model.user import User
from test import BaseMock
from test.utils import random_email
from datetime import datetime


class TestUserModel(BaseMock):
    def test_create_user_with_valid_data(self):
        user1 = User(
            password="Aa@123456!",
            full_name='Stephen Jamson',
            email=random_email()
        )
        user1.save()

        user2 = User(
            password="Aa@123456!",
            full_name='Stephen Jamson',
            email=random_email(),
            dob=datetime(1998, 5, 6)
        )
        user2.save()

        assert User.objects.count() == 2

        # Check Generated User name
        assert user1.username == "stephen_jamson"
        assert user1.username != user2.username

        # Check Generated ID
        assert user1.ID == 1
        assert user2.ID == 2

        # Check day of birth
        assert user2.dob is not None

    def test_create_user_with_invalid_email_format(self):
        user = User(
            password="Aa@123456!",
            full_name='Stephen Jamson',
            email="test.com"
        )

        with self.assertRaises(Exception):
            user.save()

    def test_create_user_with_weak_passwords(self):
        assert User.valid_password("123456789") is False
        assert User.valid_password("abcde") is False
        assert User.valid_password("abcde@12") is False

    def test_create_user_with_missing_fields(self):
        with self.assertRaises(Exception):
            User(
                password="123456789",
                full_name='Stephen Jamson',
            ).save()

        with self.assertRaises(Exception):
            User(
                full_name='Stephen Jamson',
                email=random_email()
            ).save()

        with self.assertRaises(Exception):
            User(
                password="abcde@12",
                email=random_email()
            ).save()

    def test_create_user_with_invalid_birthday_format(self):
        user = User(
            password="Aa@123456!",
            full_name='Stephen Jamson',
            email=random_email(),
            dob="06/05/1998"
        )

        with self.assertRaises(Exception):
            user.save()
