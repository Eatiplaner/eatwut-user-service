from google.protobuf import empty_pb2
import grpc

from app.grpc.client import grpc_channel
from app.grpc.generated import jwt_pb2_grpc
from app.grpc.utils.jwt import authorization_key, get_user_id_from_token


def activated(func):
    def inner(self, request, context):
        with grpc_channel() as channel:
            stub = jwt_pb2_grpc.JwtServiceStub(channel)

            try:
                response = stub.ValidActivationToken(empty_pb2.Empty(), metadata=(
                    ('authorization', authorization_key(context)),
                ))

                if response.valid is True:
                    user_id = get_user_id_from_token(authorization_key(context))
                    context.user_id = user_id

                    return func(self, request, context)
                else:
                    raise grpc.RpcError()
            except grpc.RpcError as rpc_error:
                if rpc_error is not None:
                    context.set_details(repr(rpc_error.details()))
                raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED)

    return inner


def authenticated(func):
    def inner(self, request, context):
        with grpc_channel() as channel:
            stub = jwt_pb2_grpc.JwtServiceStub(channel)

            try:
                response = stub.ValidToken(empty_pb2.Empty(), metadata=(
                    ('authorization', authorization_key(context)),
                ))

                if response.valid is True:
                    user_id = get_user_id_from_token(authorization_key(context))
                    context.user_id = user_id

                    return func(self, request, context)
                else:
                    raise grpc.RpcError()
            except grpc.RpcError as rpc_error:
                if rpc_error is not None:
                    context.set_details(repr(rpc_error.details()))
                raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED)

    return inner
