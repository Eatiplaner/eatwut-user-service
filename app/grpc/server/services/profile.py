import grpc
from mongoengine import DoesNotExist

from google.protobuf.json_format import MessageToDict
from app.grpc.client.decorators.auth import authenticated, _authorization_key
from app.grpc.generated import profile_pb2_grpc, profile_pb2
from .concerns.process import get_userid_from_token
from app.services.profile import update_profile


class ProfileService(profile_pb2_grpc.ProfileService):
    @authenticated
    def UpdateProfile(self, request, context):
        try:
            user_id = get_userid_from_token(_authorization_key(context))
            user = update_profile(user_id=user_id, data=MessageToDict(request.data))

            return profile_pb2.UpdateProfileResponse(**user.proto_data())
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(repr(e))

            return profile_pb2.UpdateProfileResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details(repr(e))

            return profile_pb2.UpdateProfileResponse()
