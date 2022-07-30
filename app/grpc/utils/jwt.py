import jwt
import os


def get_user_id_from_token(token):
    access_token = os.getenv("JWT_ACCESS_SECRET")

    payload = jwt.decode(token, key=access_token, algorithms=["HS256"])

    if not payload or not payload['user_id']:
        raise Exception

    return payload['user_id']
