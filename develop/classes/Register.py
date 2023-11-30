from develop.core.Route import Route
from rest_framework.views import APIView


class Register(Route, APIView):

    def get_method(self):
        return "POST"

    def get_patch(self):
        return "/users"
