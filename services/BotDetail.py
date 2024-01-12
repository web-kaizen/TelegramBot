from core.Route import Route
from rest_framework.views import APIView

from services.CustomRoute import CustomRoute

class BotDetail(Route, APIView):
    def __init__(self, data: dict | None = None, need_execute_local=False):
        self.data: dict = data
        super().__init__(need_execute_local)

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return f"/bots/{self._bot_id}"
