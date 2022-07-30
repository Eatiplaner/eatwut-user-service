import grpc
from concurrent import futures

from app.grpc.generated import login_signup_pb2, login_signup_pb2_grpc
from app.grpc.generated import profile_pb2_grpc, profile_pb2
from app.grpc.generated import confirmation_pb2_grpc, confirmation_pb2

from .services.login_signup import LoginSignupService
from .services.profile import ProfileService
from .services.confirmation import ConfirmationService

from grpc_reflection.v1alpha import reflection


def grpc_serve(grpc_port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    login_signup_pb2_grpc.add_LoginSignupServiceServicer_to_server(LoginSignupService(), server)
    profile_pb2_grpc.add_ProfileServiceServicer_to_server(ProfileService(), server)
    confirmation_pb2_grpc.add_ConfirmationServiceServicer_to_server(ConfirmationService(), server)

    SERVICE_NAMES = (
        login_signup_pb2.DESCRIPTOR.services_by_name["LoginSignupService"].full_name,
        profile_pb2.DESCRIPTOR.services_by_name["ProfileService"].full_name,
        confirmation_pb2.DESCRIPTOR.services_by_name["ConfirmationService"].full_name,
        reflection.SERVICE_NAME
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:" + str(grpc_port))
    server.start()
    print("Grpc running on port: " + grpc_port)

    server.wait_for_termination()
