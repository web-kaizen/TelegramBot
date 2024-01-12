from core.Route import Route
from rest_framework.views import APIView

from services.CustomRoute import CustomRoute

class DialogueDetail(Route, APIView):
    def __init__(self, method=None, body: dict = None, headers: dict = {}, token=None, need_execute_local=False):
        self.method: str = method
        self._body: dict = body
        self.headers: dict = headers
        self.headers["Authorization"] = f"Bearer {token}"
        super().__init__(need_execute_local)

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return f"/dialogues/{self._dialogue_id}"
