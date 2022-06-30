from app.model.user import User


def create_user(data):
    password = data.get("password")
    if not User.validPassword(password):
        raise Exception("Password is not valid")

    data["password"] = User.generateHashPassword(password)

    return User(**data).save()


def verify_user_credential(data):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # TODO: query by username or email
    user = User.objects.get(username=username, email=email)

    if user.verifyPassword(password):
        return user
    else:
        return False
