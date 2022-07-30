import grpc
from mongoengine import DoesNotExist

from app.grpc.generated import confirmation_pb2_grpc, confirmation_pb2
from app.services.confirmation import check_activation, find_user_id_by_email


class ConfirmationService(confirmation_pb2_grpc.ConfirmationService):
    def FindUserIdByEmail(self, request, context):
        try:
            id = find_user_id_by_email(request.email)

            return confirmation_pb2.FindUserIdByEmailResp(id=id)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return confirmation_pb2.FindUserIdByEmailResp()

    def CheckActivation(self, request, context):
        try:
            is_active = check_activation(request.user_id)
            return confirmation_pb2.CheckActivationResp(is_active=is_active)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return confirmation_pb2.CheckActivationResp()
