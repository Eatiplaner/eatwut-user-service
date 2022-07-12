from app.model.address import Address
from app.model.provider import Provider
from app.model.user import User


def saving_array_data(data, cls):
    new_data = []
    for i_data in data:
        new_data.append(cls(**i_data).save())
    return new_data


def update_profile(user_id, data):
    if "addresses" in data:
        addresses_data = data["addresses"]
        data["addresses"] = saving_array_data(addresses_data, Address)

    if "providers" in data:
        providers_data = data["providers"]
        data["providers"] = saving_array_data(providers_data, Provider)

    User.objects(ID=user_id).update(**data)
    return User.objects.get(ID=user_id)
