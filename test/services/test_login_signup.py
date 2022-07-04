import unittest
from app.model.user import User
from app.services.login_signup import create_user, find_user_by_credential

password = "eatiplaner01!123"
email = 'eatiplaner01@gmail.com'


class TestLoginSignupService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        userPassword = User.generate_hash_password(password)

        user = User(
            ID=1,
            username='eatiplaner01',
            password=userPassword,
            first_name='stephen',
            last_name='jamson',
            email=email
        )
        user.save()

    def test_find_user_by_credential_with_correct_name(self):
        result = find_user_by_credential({"username": "eatiplaner01", "password": password})

        assert result.username == 'eatiplaner01'
        assert result.first_name == 'stephen'
        assert result.last_name == 'jamson'
        assert result.email == 'eatiplaner01@gmail.com'
        assert result.ID == 1

    def test_find_user_by_credential_with_correct_email(self):
        result = find_user_by_credential({"username": "eatiplaner01", "password": password})

        assert result.username == 'eatiplaner01'
        assert result.first_name == 'stephen'
        assert result.last_name == 'jamson'
        assert result.email == 'eatiplaner01@gmail.com'
        assert result.ID == 1

    def test_find_user_by_credential_with_incorrect_credential(self):
        result = find_user_by_credential({"username": "fake", "password": password})

        assert result is None

    def test_create_user_with_valid_params(self):
        my_password = 'Aa@123456!'
        my_email = "test@gmail.com"
        data = {
            "username": "username",
            "email": my_email,
            "password": my_password,
            "first_name": "jame",
            "last_name": "david"
        }

        create_user(data)
        assert User.objects.count() == 2
        my_account = User.objects.get(email=my_email)

        assert my_account.first_name == "jame"

    def test_create_user_with_email_existed(self):
        my_password = 'Aa@123456!'
        data = {
            "username": "username",
            "email": email,
            "password": my_password,
            "first_name": "jame",
            "last_name": "david"
        }

        with self.assertRaises(Exception):
            create_user(data)
