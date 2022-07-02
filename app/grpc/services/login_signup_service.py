from google.protobuf.json_format import MessageToDict
import grpc
from app.grpc.rpc_pb import login_signup_pb2_grpc, login_signup_pb2
from app.services.user_services import create_user, find_user_by_credential


class LoginSignupService(login_signup_pb2_grpc.LoginSignupService):
    def CreateUser(self, request, context):
        try:
            user = create_user(MessageToDict(request))

            return login_signup_pb2.UserResponse(
                id=user.username, # TODO: fix id
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            # TODO: better message back
            context.set_details(repr(e))

            return login_signup_pb2.UserResponse()

    def FindUserByCredential(self, request, context):
        print(request)
        user = find_user_by_credential(MessageToDict(request))

        print(user)
        if user is not None:
            return login_signup_pb2.UserResponse(
                id=user.username, # TODO: fix id
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return login_signup_pb2.UserResponse()
