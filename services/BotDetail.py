from typing import Any
from django.http import HttpResponse
from requests import Response, Request
from core.Route import Route
from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class BotDetail(Route, APIView):
    def __init__(self):
        super().__init__()
        self.bot_id: Any = None

    def dispatch(self, request: Request, **kwargs) -> HttpResponse:
        self.bot_id = kwargs.get("bot_id")
        return super().dispatch(request)

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return f"/bots/{self.bot_id}"
