from datetime import datetime

from app.model.address import Address
from app.model.provider import Provider
from app.model.user import User
from .concerns.data_manipulate import convert_array_to_class
from app.constants.date import dateTimeFormat


def update_profile(**kwargs):
    user_id = kwargs['user_id']
    data = kwargs['data']

    if "addresses" in data:
        addresses_data = data["addresses"]
        data["addresses"] = convert_array_to_class(addresses_data, Address)

    if "providers" in data:
        providers_data = data["providers"]
        data["providers"] = convert_array_to_class(providers_data, Provider)

    if "dob" in data:
        data["dob"] = data["dob"] and datetime.strptime(data["dob"], dateTimeFormat) or None

    user = User.objects.get(ID=user_id)
    user.update(**data)

    return user.reload()


def change_password(**kwargs):
    user_id = kwargs['user_id']
    new_password = kwargs['new_password']

    if not User.valid_password(new_password):
        raise Exception("New Password is not valid")

    user = User.objects.get(ID=user_id)
    user.password = new_password

    User.generate_hash_password(user)

    user.update(password=user.password)

    return


def record_login_time(user_id):
    user = User.objects.get(ID=user_id)
    user.update(last_login=date.today())

    return
