from requests import Request
from core.Route import Route
from rest_framework.views import APIView


class DialogueList(Route, APIView):

    def get_method(self) -> str:
        return self.request.method

    def get_path(self) -> str:
        return "/dialogues"
