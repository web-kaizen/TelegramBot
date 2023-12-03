from .CustomRoute import CustomRoute, Route
from rest_framework.views import APIView


class Register(CustomRoute, APIView):

    def get_method(self):
        return "POST"

    def get_patch(self):
        return "/users"
