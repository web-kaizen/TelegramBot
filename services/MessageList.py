from typing import Any
from django.http import HttpResponse
from requests import Request
from core.Route import Route
from rest_framework.views import APIView


class MessageList(Route, APIView):

    def __init__(self):
        super().__init__()
        self.dialogue_id: Any = None

    def dispatch(self, request: Request, **kwargs) -> HttpResponse:
        self.dialogue_id = kwargs.get("dialogue_id")
        return super().dispatch(request=request)

    def get_method(self) -> str:
        return self.request.method

    def get_path(self) -> str:
        return f"/dialogues/{self.dialogue_id}/messages"
