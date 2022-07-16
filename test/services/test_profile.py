from mongoengine import DoesNotExist
from app.model.user import User
from app.model.address import Address
from app.model.provider import Provider
from app.services.profile import update_profile
from test import BaseMock
from test.utils import random_string_specific_length
from test.setup.data import full_name, email, password, \
    address1, address2, provider_tiktok, provider_youtube, provider_facebook


class TestUpdateProfileService(BaseMock):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        addresses = Address(**address1).save()
        providers = Provider(**provider_facebook).save()

        user = User(
            password=password,
            full_name=full_name,
            email=email,
            addresses=[addresses],
            providers=[providers]
        )
        user.save()

    def test_update_profile_with_valid_params(self):
        user_pre_update = User.objects.get(ID=1)
        data_update = {
            "username": "stephen_jamson_differ",
            "bio": "It's my Faliur",
            "dob": "06-05-1998 00:00:00",
            "phone": "0123456789",
            "is_kol": True,
            "addresses": [address1, address2],
            "providers": [provider_youtube, provider_tiktok],
            "prefer_categories": ["3", "4", "5", "6"]
        }
        user_updated = update_profile(user_id=1, data=data_update)

        assert user_updated.username != user_pre_update.username
        assert user_updated.bio != user_pre_update.bio
        assert user_updated.dob != user_pre_update.dob
        assert user_updated.phone != user_pre_update.phone
        assert user_updated.is_kol != user_pre_update.is_kol
        assert user_updated.email == user_pre_update.email
        assert user_updated.addresses[1].type == "office"
        assert len(user_updated.providers) == 2
        assert len(user_updated.prefer_categories) != len(user_pre_update.prefer_categories)

        # TODO: make sure old address and provider has been removed
        # assert Address.objects.count() == 2
        # assert Provider.objects.count() == 2

    def test_update_profile_with_not_found_user_id(self):
        with self.assertRaises(DoesNotExist):
            update_profile(user_id=2, data={})

    def test_update_profile_with_invalid_params(self):
        data_update = {
            "username": random_string_specific_length(31),
            "bio": random_string_specific_length(501),
            "dob": "1998/05/07",
        }

        with self.assertRaises(Exception):
            update_profile(user_id=1, data=data_update)

    def test_update_profile_with_missing_params(self):
        my_address = {
            "district": "District 1",
            "city": "Ho Chi Minh City"
        }
        my_provider = {
            "display_on_profile": False
        }

        data_update = {
            "addresses": [my_address],
            "providers": [my_provider]
        }

        with self.assertRaises(Exception):
            update_profile(user_id=1, data=data_update)
