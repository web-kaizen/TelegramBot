from typing import Any

from requests import Response, Request

from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class BotDetail(CustomRoute, APIView):
    def __init__(self):
        super().__init__()
        self.bot_id: Any = None

    def get(self, request: Request, bot_id=None) -> Response:
        self.bot_id = bot_id
        return super().get(request)

    def get_method(self) -> str:
        return "GET"

    def get_patch(self) -> str:
        return f"/bots/{self.bot_id}"
