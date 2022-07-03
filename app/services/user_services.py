from mongoengine import DoesNotExist, Q
from app.model.user import User


def create_user(data):
    password = data.get("password")
    if not User.validPassword(password):
        raise Exception("Password is not valid")

    data["password"] = User.generateHashPassword(password)
    data["ID"] = User.objects.count() + 1

    return User(**data).save()


def find_user_by_credential(data):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    try:
        user = User.objects.get(Q(username=username) | Q(email=email))
        if user.verifyPassword(password):
            return user
    except DoesNotExist:
        return None

    return None
