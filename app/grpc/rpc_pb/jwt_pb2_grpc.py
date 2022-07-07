# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import jwt_pb2 as jwt__pb2


class JwtServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ValidToken = channel.unary_unary(
                '/auth.JwtService/ValidToken',
                request_serializer=jwt__pb2.ValidRequest.SerializeToString,
                response_deserializer=jwt__pb2.ValidResponse.FromString,
                )


class JwtServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ValidToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JwtServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ValidToken': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidToken,
                    request_deserializer=jwt__pb2.ValidRequest.FromString,
                    response_serializer=jwt__pb2.ValidResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.JwtService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JwtService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ValidToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.JwtService/ValidToken',
            jwt__pb2.ValidRequest.SerializeToString,
            jwt__pb2.ValidResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
