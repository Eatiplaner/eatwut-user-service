import grpc
from app.grpc.client import grpc_channel
from app.grpc.generated import jwt_pb2_grpc


def authenticated(func):
    def inner(self, request, context):
        stub = jwt_pb2_grpc.JwtServiceStub(grpc_channel())

        try:
            response = stub.ValidToken(_authorization_key(context))

            if response.Result is True:
                return func(self, request, context)
            else:
                raise Exception()
        except Exception:
            raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED)

    return inner


def _authorization_key(context):
    metadict = dict(context.invocation_metadata())
    return metadict['authorization']
