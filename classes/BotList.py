from .CustomRoute import CustomRoute
from rest_framework.views import APIView
from core.Route import Route


class BotList(Route, APIView):

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return "/bots"

    def set_url(self, url: str) -> None:
        super().set_url(url + "/new_bots")

    def set_headers(self, headers: dict) -> None:
        headers["Cache-Hash"] = "skdhgadjaskdad"
        super().set_headers(headers)

    def set_parameters(self, data: dict) -> None:
        data["query"] = 123
        super().set_parameters(data)

    def set_response(self, response: dict, status=None) -> None:
        response["error_2"] = "NEW ERROR"
        super().set_response(response)


