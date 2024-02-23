from core.Route import Route
from rest_framework.views import APIView
from services.CustomRoute import CustomRoute


class DialogueOptionalUpdate(CustomRoute, APIView):

    def __init__(self, dialogue_id, data: dict = None, headers: dict = {}, token=None, need_execute_local=False):
        self.data: dict = data
        self.headers: dict = headers
        self.headers["Authorization"] = f"Bearer {token}"
        self._dialogue_id = dialogue_id
        super().__init__(need_execute_local)

    def get_method(self) -> str:
        return "PATCH"

    def get_path(self) -> str:
        return f"/dialogues/{self._dialogue_id}"
