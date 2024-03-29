# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from app.grpc.generated import profile_pb2 as app_dot_grpc_dot_generated_dot_profile__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ProfileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateProfile = channel.unary_unary(
                '/user.ProfileService/UpdateProfile',
                request_serializer=app_dot_grpc_dot_generated_dot_profile__pb2.UpdateProfileRequest.SerializeToString,
                response_deserializer=app_dot_grpc_dot_generated_dot_profile__pb2.UserProfileResponse.FromString,
                )
        self.GetProfileByToken = channel.unary_unary(
                '/user.ProfileService/GetProfileByToken',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=app_dot_grpc_dot_generated_dot_profile__pb2.UserProfileResponse.FromString,
                )
        self.ChangePassword = channel.unary_unary(
                '/user.ProfileService/ChangePassword',
                request_serializer=app_dot_grpc_dot_generated_dot_profile__pb2.ChangePasswordRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RecordLoginTime = channel.unary_unary(
                '/user.ProfileService/RecordLoginTime',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ProfileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProfileByToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecordLoginTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProfile,
                    request_deserializer=app_dot_grpc_dot_generated_dot_profile__pb2.UpdateProfileRequest.FromString,
                    response_serializer=app_dot_grpc_dot_generated_dot_profile__pb2.UserProfileResponse.SerializeToString,
            ),
            'GetProfileByToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProfileByToken,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=app_dot_grpc_dot_generated_dot_profile__pb2.UserProfileResponse.SerializeToString,
            ),
            'ChangePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePassword,
                    request_deserializer=app_dot_grpc_dot_generated_dot_profile__pb2.ChangePasswordRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RecordLoginTime': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordLoginTime,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.ProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProfileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.ProfileService/UpdateProfile',
            app_dot_grpc_dot_generated_dot_profile__pb2.UpdateProfileRequest.SerializeToString,
            app_dot_grpc_dot_generated_dot_profile__pb2.UserProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProfileByToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.ProfileService/GetProfileByToken',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            app_dot_grpc_dot_generated_dot_profile__pb2.UserProfileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.ProfileService/ChangePassword',
            app_dot_grpc_dot_generated_dot_profile__pb2.ChangePasswordRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecordLoginTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.ProfileService/RecordLoginTime',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
