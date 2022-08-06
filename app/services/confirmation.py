from app.model.user import User


def find_user_info_by_email(email):
    user = User.objects.get(email=email)
    return {"id": user.ID, "full_name": user.full_name}


def active_user(user_id):
    user = User.objects.get(ID=user_id)

    if user.is_active:
        raise Exception("User already activated")

    user.update(is_active=True)

    return True


def check_activation(user_id):
    user = User.objects.get(ID=user_id)
    return user.is_active
