from mongoengine import Q
from app.model.address import Address
from app.model.provider import Provider
from app.model.user import User
from .concerns.data_manipulate import convert_array_to_class


def update_profile(**kwargs):
    user_id = kwargs['user_id']
    data = kwargs['data']

    if "addresses" in data:
        addresses_data = data["addresses"]
        data["addresses"] = convert_array_to_class(addresses_data, Address)

    if "providers" in data:
        providers_data = data["providers"]
        data["providers"] = convert_array_to_class(providers_data, Provider)

    user = User.objects.get(ID=user_id)
    user.update(**data)

    return user.reload()
