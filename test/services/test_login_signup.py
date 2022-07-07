from app.model.user import User
from app.services.login_signup import create_user, find_user_by_credential
from test import BaseMock

password = "eatiplaner01!123"
email = 'eatiplaner01@gmail.com'


class TestLoginSignupService(BaseMock):
    @ classmethod
    def setUpClass(cls):
        super().setUpClass()

        user = User(
            password=password,
            full_name='Stephen Jamson',
            email=email
        )
        user.save()

    def test_find_user_by_credential_with_correct_name(self):
        result = find_user_by_credential({"username": "stephen_jamson", "password": password})

        assert result.username == 'stephen_jamson'
        assert result.full_name == 'Stephen Jamson'
        assert result.email == 'eatiplaner01@gmail.com'
        assert result.ID == 1

    def test_find_user_by_credential_with_correct_email(self):
        result = find_user_by_credential({"email": email, "password": password})

        assert result.username == 'stephen_jamson'
        assert result.full_name == 'Stephen Jamson'
        assert result.email == 'eatiplaner01@gmail.com'
        assert result.ID == 1

    def test_find_user_by_credential_with_incorrect_credential(self):
        result = find_user_by_credential({"username": "fake", "password": password})

        assert result is None

    def test_create_user_with_valid_params(self):
        my_password = 'Aa@123456!'
        my_email = "test@gmail.com"
        data = {
            "email": my_email,
            "password": my_password,
            "full_name": "Stephen Jamson",
        }

        create_user(data)
        assert User.objects.count() == 2
        my_account = User.objects.get(email=my_email)

        assert my_account.full_name == "Stephen Jamson"
        assert my_account.email == my_email

    def test_create_user_with_email_existed(self):
        my_password = 'Aa@123456!'
        data = {
            "email": email,
            "password": my_password,
            "full_name": "Stephen Jamson",
        }

        with self.assertRaises(Exception):
            create_user(data)
