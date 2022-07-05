from app.model.user import User
from test import BaseMock


class TestUserModel(BaseMock):
    def test_create_user_with_valid_data(self):
        user = User(
            ID=1,
            username='eatiplaner01',
            password="Aa@123456!",
            first_name='stephen',
            last_name='jamson',
            email="test@gmail.com"
        )

        user.save()
        assert User.objects.count() == 1

    def test_create_user_with_invalid_email_format(self):
        user = User(
            ID=1,
            username='eatiplaner01',
            password="Aa@123456!",
            first_name='stephen',
            last_name='jamson',
            email="test.com"
        )

        with self.assertRaises(Exception):
            user.save()

    def test_create_user_with_weak_passwords(self):
        user1 = User(
            ID=1,
            username='eatiplaner01',
            password="123456789",
            first_name='stephen',
            last_name='jamson',
            email="test@gmail.com"
        )

        with self.assertRaises(Exception):
            user1.save()

        user2 = User(
            ID=1,
            username='eatiplaner01',
            password="abcde",
            first_name='stephen',
            last_name='jamson',
            email="test@gmail.com"
        )

        with self.assertRaises(Exception):
            user2.save()

        user3 = User(
            ID=1,
            username='eatiplaner01',
            password="abcde@12",
            first_name='stephen',
            last_name='jamson',
            email="test@gmail.com"
        )

        with self.assertRaises(Exception):
            user3.save()

    def test_create_user_with_missing_fields(self):
        user1 = User(
            ID=1,
            password="123456789",
            first_name='stephen',
            last_name='jamson',
            email="test@gmail.com"
        )

        with self.assertRaises(Exception):
            user1.save()

        user2 = User(
            ID=1,
            username='eatiplaner01',
            password="abcde",
            last_name='jamson',
            email="test@gmail.com"
        )

        with self.assertRaises(Exception):
            user2.save()

        user3 = User(
            ID=1,
            username='eatiplaner01',
            password="abcde@12",
            first_name='stephen',
            email="test@gmail.com"
        )

        with self.assertRaises(Exception):
            user3.save()
