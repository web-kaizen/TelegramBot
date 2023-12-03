from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class EmailVerificationCheck(CustomRoute, APIView):

    def get_method(self):
        return "GET"

    def get_patch(self):
        return f"/users/email-verification/check"

