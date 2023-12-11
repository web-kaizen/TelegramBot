from requests import Request
from .CustomRoute import CustomRoute
from rest_framework.views import APIView


class DialogueList(CustomRoute, APIView):

    def get_method(self) -> str:
        return self.request.method

    def get_patch(self) -> str:
        return "/dialogues"
