from .CustomRoute import CustomRoute, Route
from rest_framework.views import APIView


class Register(CustomRoute, APIView):

    def get_method(self) -> str:
        return "POST"

    def get_patch(self) -> str:
        return "/users"
