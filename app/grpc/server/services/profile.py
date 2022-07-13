from app.grpc.client.decorators.auth import authenticated


class ProfileService():
    @authenticated
    def UpdateProfile(self, request, context):
        # TODO: Implement GRPC Update Profile
        return None
