from rest_framework.views import APIView
from core.Route import Route
from services.CustomRoute import CustomRoute


class BotList(Route, APIView):

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return "/bots"

    # def set_headers(self, headers: dict) -> None:
    #     headers["New_HEADER"] = "VALUE"
    #     super().set_headers(headers)

    # def get_headers(self) -> dict:
    #     self._headers["OLD_HEADER"] = "OLD_VALUE"
    #     return super().get_headers()

    # def set_response(self, response: dict | None, status=None) -> None: # c proxy_response
    #     if response:
    #         response = "OLD_VALUE"
    #     super().set_response(response, status)

    # def get_response(self) -> dict | None:
    #     self._response["NEW_RESULT"] = "NEW_VALUE"
    #     return super().get_response()


