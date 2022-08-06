from mongoengine import DoesNotExist
from app.model.user import User
from app.services.confirmation import find_user_info_by_email, active_user, check_activation
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

    def test_find_user_info_by_email_with_valid_params(self):
        user = User.objects.get(email=email)
        user_info = find_user_info_by_email(email)

        assert user_info == {"id": user.ID, "full_name": user.full_name}

    def test_find_user_info_by_email_with_not_found_user_id(self):
        with self.assertRaises(DoesNotExist):
            find_user_info_by_email('fake_email@gmail.com')

    def test_active_user_with_user_already_activate(self):
        user = User.objects.get(email=email)
        user.update(is_active=True)

        with self.assertRaises(Exception):
            active_user(user.ID)

    def test_active_user_with_valid_params(self):
        user = User.objects.get(email=email)
        user.update(is_active=False)

        is_active = active_user(user.ID)

        assert is_active is True

    def test_active_user_with_not_found_user_id(self):
        with self.assertRaises(DoesNotExist):
            active_user(1000)

    def test_check_activation_with_valid_params(self):
        User.objects.get(email=email).update(is_active=False)
        is_active = check_activation(User.objects.get(email=email).ID)

        assert is_active is False

        active_user(User.objects.get(email=email).ID)
        is_active = check_activation(User.objects.get(email=email).ID)

        assert is_active is True


def test_check_activation_with_not_found_user_id(self):
    with self.assertRaises(DoesNotExist):
        check_activation(1000)
