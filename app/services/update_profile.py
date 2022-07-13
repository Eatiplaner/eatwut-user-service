from app.model.address import Address
from app.model.provider import Provider
from app.model.user import User
from .concerns.data_manipulate import convert_array_to_class


def update_profile(user_id, data):
    if "addresses" in data:
        addresses_data = data["addresses"]
        data["addresses"] = convert_array_to_class(addresses_data, Address)

    if "providers" in data:
        providers_data = data["providers"]
        data["providers"] = convert_array_to_class(providers_data, Provider)

    User.objects(ID=user_id).update(**data)
    return User.objects.get(ID=user_id)
