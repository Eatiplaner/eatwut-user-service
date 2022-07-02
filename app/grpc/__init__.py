import grpc
from concurrent import futures

from app.grpc.rpc_pb import login_signup_pb2, login_signup_pb2_grpc
from app.grpc.services.login_signup_service import LoginSignupService

from grpc_reflection.v1alpha import reflection


def grpc_serve(grpc_port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    login_signup_pb2_grpc.add_LoginSignupServiceServicer_to_server(LoginSignupService(), server)

    SERVICE_NAMES = (
        login_signup_pb2.DESCRIPTOR.services_by_name["LoginSignupService"].full_name,
        reflection.SERVICE_NAME
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:" + str(grpc_port))
    server.start()
    print("Grpc running on port: " + grpc_port)

    server.wait_for_termination()
