from google.protobuf import empty_pb2
import grpc
from mongoengine import DoesNotExist

from app.grpc.generated import confirmation_pb2_grpc, confirmation_pb2
from app.grpc.utils.jwt import get_user_id_from_rpc_context
from app.services.confirmation import active_user, check_activation, find_user_info_by_email


class ConfirmationService(confirmation_pb2_grpc.ConfirmationService):
    def FindUserInfoByEmail(self, request, context):
        try:
            user_info = find_user_info_by_email(request.email)

            return confirmation_pb2.FindUserByEmailResp(**user_info)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return confirmation_pb2.FindUserByEmailResp()

    def ActiveUser(self, request, context):
        try:
            active_user(get_user_id_from_rpc_context(context))
            return empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return empty_pb2.Empty()

    def CheckActivation(self, request, context):
        try:
            user_id = get_user_id_from_rpc_context(request.token)
            is_active = check_activation(user_id)
            return confirmation_pb2.CheckActivationResp(is_active=is_active)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return confirmation_pb2.CheckActivationResp()
        except Exception as e:
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details(repr(e))
