from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
import grpc
from mongoengine import DoesNotExist

from app.grpc.client.decorators.auth import authenticated

from app.grpc.generated import profile_pb2_grpc, profile_pb2
from app.services.profile import change_password, update_profile


class ProfileService(profile_pb2_grpc.ProfileService):
    @authenticated
    def UpdateProfile(self, request, context):
        try:
            user = update_profile(
                user_id=context.user_id,
                data=MessageToDict(request.data)
            )

            return profile_pb2.UpdateProfileResponse(**user.proto_data())
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return profile_pb2.UpdateProfileResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details(repr(e))

            return profile_pb2.UpdateProfileResponse()

    @authenticated
    def ChangePassword(self, request, context):
        try:
            change_password(
                user_id=context.user_id,
                new_password=request.new_password
            )

            return empty_pb2.Empty()
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return empty_pb2.Empty()
        except Exception as e:
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details(repr(e))

            return empty_pb2.Empty()
