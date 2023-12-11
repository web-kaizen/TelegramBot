from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class EmailVerificationCheck(CustomRoute, APIView):

    def get_method(self) -> str:
        return "GET"

    def get_patch(self) -> str:
        return f"/users/email-verification/check"

