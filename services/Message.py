from typing import Any

from requests import Request

from core.Route import Route
from rest_framework.views import APIView


class MessageList(Route, APIView):

    def get_method(self) -> str:
        return 'GET'


class MessageCreate(Route, APIView):

    def get_method(self) -> str:
        return 'POST'


class Message(MessageList, MessageCreate, APIView):

    def __init__(self):
        super().__init__()
        self.dialogue_id: Any = None

    def dispatch(self, request: Request, *args, **kwargs):
        self.dialogue_id = kwargs.get("dialogue_id")
        return super().dispatch(request=request)

    def get_method(self) -> str:
        return MessageCreate.get_method(self) if self.request.method == 'POST' else MessageList.get_method(self)

    def get_path(self) -> str:
        return f"/dialogues/{self.dialogue_id}/messages"


