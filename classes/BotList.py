from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class BotList(CustomRoute, APIView):

    def get_method(self) -> str:
        return "GET"

    def get_patch(self) -> str:
        return "/bots"
