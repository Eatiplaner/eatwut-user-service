import grpc

from google.protobuf.json_format import MessageToDict
from app.grpc.rpc_pb import login_signup_pb2_grpc, login_signup_pb2
from app.services.login_signup import create_user, find_user_by_credential


class LoginSignupService(login_signup_pb2_grpc.LoginSignupService):
    def CreateUser(self, request, context):
        try:
            user = create_user(MessageToDict(request))

            return login_signup_pb2.UserResponse(**user.proto_data())
        except Exception as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(repr(e))

            return login_signup_pb2.UserResponse()

    def FindUserByCredential(self, request, context):
        user = find_user_by_credential(MessageToDict(request))

        if user is not None:
            return login_signup_pb2.UserResponse(**user.proto_data())
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return login_signup_pb2.UserResponse()
