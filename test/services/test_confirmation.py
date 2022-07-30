from mongoengine import DoesNotExist
from app.model.user import User
from app.services.confirmation import find_user_id_by_email, check_activation
from test import BaseMock
from test.setup.data import full_name, email, password


class TestConfirmationService(BaseMock):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        user = User(
            password=password,
            full_name=full_name,
            email=email,
            is_active=False,
        )
        user.save()

    def test_find_user_id_by_email_with_valid_params(self):
        user_id = find_user_id_by_email(email)

        assert user_id == User.objects.get(email=email).ID

    def test_find_user_id_by_email_with_not_found_user_id(self):
        with self.assertRaises(DoesNotExist):
            find_user_id_by_email('fake_email@gmail.com')

    def test_check_activation_with_valid_params(self):
        is_active = check_activation(User.objects.get(email=email).ID)

        assert is_active is False

        User.objects.get(email=email).update(is_active=True)
        is_active = check_activation(User.objects.get(email=email).ID)

        assert is_active is True


def test_check_activation_with_not_found_user_id(self):
    with self.assertRaises(DoesNotExist):
        check_activation(1000)
