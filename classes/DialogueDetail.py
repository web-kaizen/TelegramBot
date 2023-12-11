from typing import Any
from django.http import HttpResponse
from requests import Request
from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class DialogueDetail(CustomRoute, APIView):

    def __init__(self):
        super().__init__()
        self.dialogue_id: Any = None

    ''' Вместо прописывания всех методов get/post... из-за dialogue_id,
     метод dispatch передает dialogue_id и вызывет определенный метод из request (request.method) '''
    def dispatch(self, request: Request, **kwargs) -> HttpResponse:
        self.dialogue_id = kwargs.get("dialogue_id")
        return super().dispatch(request=request)

    def get_method(self) -> str:
        return self.request.method

    def get_patch(self) -> str:
        return f"/dialogues/{self.dialogue_id}"
