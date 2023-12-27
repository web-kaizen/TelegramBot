from typing import Any
from django.http import HttpResponse
from requests import Request
from core.Route import Route
from rest_framework.views import APIView

from services.CustomRoute import CustomRoute


class DialogueDetail(CustomRoute, APIView):
    def __init__(self, method=None, dialogue_id=None, body: dict = None, headers: dict = {}, token=None, need_execute_local=False):
        self.dialogue_id: Any = dialogue_id
        self.method: str = method
        self._body: dict = body
        self.headers: dict = headers
        self.headers["Authorization"] = f"Bearer {token}"
        super().__init__(need_execute_local)

    def dispatch(self, request: Request, **kwargs) -> HttpResponse:
        dialogue_id = kwargs.get('dialogue_id', None)
        if dialogue_id:
            self.dialogue_id = dialogue_id
        return super().dispatch(request=request)

    def get_method(self) -> str:
        if self.method:
            return f"{self.method}"
        return self.request.method

    def get_path(self) -> str:
        return f"/dialogues/{self.dialogue_id}"
