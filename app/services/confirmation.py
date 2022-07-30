from app.model.user import User


def find_user_id_by_email(email):
    user = User.objects.get(email=email)
    return user.ID


def active_user(user_id):
    user = User.objects.get(ID=user_id)
    user.update(is_active=True)

    return True


def check_activation(user_id):
    user = User.objects.get(ID=user_id)
    return user.is_active
