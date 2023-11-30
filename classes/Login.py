from rest_framework.views import APIView
from .CustomRoute import CustomRoute


class Login(CustomRoute, APIView):

    def get_method(self):
        return "POST"

    def get_patch(self):
        return "/users/login"
