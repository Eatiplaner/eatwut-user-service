from app.model.address import Address
from test import BaseMock
from test.setup.data import address1


class TestAddressModel(BaseMock):
    def test_create_address_with_valid_data(self):
        address = Address(**address1)
        address.save()

        assert Address.objects.count() == 1

    def test_create_address_with_missing_fields(self):
        with self.assertRaises(Exception):
            Address(
                city="Ho Chi Minh City",
                type="home"
            ).save()

        with self.assertRaises(Exception):
            Address(
                district="District 1",
                type="home"
            ).save()

        with self.assertRaises(Exception):
            Address(
                district="District 1",
                city="Ho Chi Minh City",
            ).save()
