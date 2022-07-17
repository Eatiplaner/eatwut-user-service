import jwt
import os


def get_userid_from_token(token):
    access_token = os.getenv("JWT_ACCESS_SECRET")
    payload = jwt.decode(token, key=access_token, algorithm=["HS256"])
    return payload.user_id
