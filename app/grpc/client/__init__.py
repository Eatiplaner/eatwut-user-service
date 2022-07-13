import os
import grpc


def grpc_channel():
    domain = os.getenv('GRPC_CLIENT_DOMAIN')
    port = os.getenv('GRPC_CLIENT_PORT')

    return grpc.insecure_channel(f'{domain}:{port}')
