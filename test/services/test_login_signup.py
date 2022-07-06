from app.model.user import User
from app.services.login_signup import create_user, find_user_by_credential
from test import BaseMock

password = 'eatiplaner01!123'
email = 'eatiplaner01@gmail.com'
full_name = 'Stephen Jamson'
username = 'stephen_jamson'


class TestLoginSignupService(BaseMock):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        userPassword = User.generate_hash_password(password)

        user = User(
            ID=1,
            username=username,
            password=userPassword,
            full_name=full_name,
            email=email
        )
        user.save()

    def test_find_user_by_credential_with_correct_login_input(self):
        result = find_user_by_credential({"username": username, "password": password})

        assert result.username == username
        assert result.full_name == 'Stephen Jamson'
        assert result.email == 'eatiplaner01@gmail.com'
        assert result.ID == 1

    def test_find_user_by_credential_with_incorrect_credential(self):
        result = find_user_by_credential({"username": "fake", "password": password})

        assert result is None

    def test_create_user_with_valid_params(self):
        my_password = 'Aa@123456!'
        my_email = 'test@gmail.com'
        my_full_name = 'Jame David'
        my_username = 'jame_david'
        data = {
            "username": my_username,
            "email": my_email,
            "password": my_password,
            "full_name": my_full_name,
        }

        create_user(data)
        assert User.objects.count() == 2
        my_account = User.objects.get(email=my_email)

        assert my_account.full_name == "Jame David"

    def test_create_user_with_email_existed(self):
        my_password = 'Aa@123456!'
        my_full_name = 'Jame David'
        my_username = 'jame_david'
        data = {
            "username": my_username,
            "email": email,
            "password": my_password,
            "full_name": my_full_name,
        }

        with self.assertRaises(Exception):
            create_user(data)
