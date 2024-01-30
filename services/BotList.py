from rest_framework.views import APIView
from services.CustomRoute import CustomRoute


class BotList(CustomRoute, APIView):
    def __init__(self):
        self.use_cache = True
        super().__init__(use_cache=self.use_cache)

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return "/bots"
