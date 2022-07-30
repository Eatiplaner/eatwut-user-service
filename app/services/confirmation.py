from app.model.user import User


def find_user_id_by_email(email):
    user = User.objects.get(email=email)
    return user.ID


def check_activation(user_id):
    user = User.objects.get(ID=user_id)
    return user.is_active
