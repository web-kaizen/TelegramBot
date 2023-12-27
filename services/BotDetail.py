from typing import Any
from django.http import HttpResponse
from requests import Response, Request
from core.Route import Route
from rest_framework.views import APIView

from services.CustomRoute import CustomRoute


class BotDetail(CustomRoute, APIView):
    def __init__(self, bot_id=None, data: dict | None = None, need_execute_local=False):
        self.bot_id: Any = bot_id
        self.data: dict = data
        super().__init__(need_execute_local)

    def dispatch(self, request: Request, **kwargs) -> HttpResponse:
        bot_id = kwargs.get('bot_id', None)
        if bot_id:
            self.bot_id = bot_id
        return super().dispatch(request)

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return f"/bots/{self.bot_id}"
