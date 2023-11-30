from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class BotList(CustomRoute, APIView):

    def get_method(self):
        return "GET"

    def get_patch(self):
        return "/bots"
