from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class EmailVerificationCheck(CustomRoute, APIView):

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return f"/users/email-verification/check"

