import jwt
import os
import grpc

from app.grpc.client import grpc_channel
from app.grpc.generated import jwt_pb2_grpc, jwt_pb2


def authenticated(func):
    def inner(self, request, context):
        with grpc_channel() as channel:
            stub = jwt_pb2_grpc.JwtServiceStub(channel)

            try:
                response = stub.ValidToken(jwt_pb2.ValidRequest(**{"token": _authorization_key(context)}))

                if response.valid is True:
                    user_id = _get_user_id_from_token(_authorization_key(context))
                    context.user_id = user_id

                    return func(self, request, context)
                else:
                    raise Exception()
            except Exception:
                raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED)

    return inner


def _authorization_key(context):
    metadict = dict(context.invocation_metadata())
    return metadict['authorization']


def _get_user_id_from_token(token):
    access_token = os.getenv("JWT_ACCESS_SECRET")

    payload = jwt.decode(token, key=access_token, algorithms=["HS256"])

    if not payload or not payload['user_id']:
        raise Exception

    return payload['user_id']
