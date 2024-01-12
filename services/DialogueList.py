from requests import Request
from core.Route import Route
from rest_framework.views import APIView


class DialogueList(Route, APIView):
    def __init__(self):
        super().__init__()
        self.__request_headers: dict = None

    def request_setter(self, request):
        self.__request_headers = dict(request.headers)
        self.__request_headers["Content-Type"] = "application/json"
        request.headers = self.__request_headers
        super().request_setter(request)

    def get_method(self) -> str:
        return self.request.method

    def get_path(self) -> str:
        return "/dialogues"
