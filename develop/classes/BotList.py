from develop.routes import Route
from rest_framework.views import APIView


class BotList(Route, APIView):

    def get_method(self):
        return "GET"

    def get_patch(self):
        return "/bots"
