from mongoengine import DoesNotExist, Q
from app.model.user import User


def create_user(data):
    full_name = data.get('full_name')
    password = data.get("password")
    if not User.valid_password(password):
        raise Exception("Password is not valid")

    data["username"] = full_name
    data["password"] = User.generate_hash_password(password)
    data["ID"] = User.objects.count() + 1

    return User(**data).save()


def find_user_by_credential(data):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    try:
        user = User.objects.get(Q(username=username) | Q(email=email))
        if user.verify_password(password):
            return user
    except DoesNotExist:
        return None

    return None
