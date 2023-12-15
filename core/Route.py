import requests
from .Logger import Logger
from .settings import APP_ID, THIRD_PARTY_APP_URL
from .Methods import Methods
import json


class Route(Methods):
    def __init__(self):
        self._APP_ID = APP_ID
        self._BASE_URL = THIRD_PARTY_APP_URL
        self.__method: str = None
        self.__parameters: dict = {}
        self.__response: dict = {}
        self.__headers: dict = {}
        self.__url: str = None
        self.__status_code: int = None
        self._not_allowed_headers = ('Connection', 'Keep-Alive', "Content-Length")
        self._logger = Logger()

    def request_setter(self, request):
        self._logger.set_proxy_method(request.method)
        self._logger.set_proxy_url(request.build_absolute_uri())
        self._logger.set_proxy_request_headers(dict(request.headers))
        self._logger.set_proxy_request_body(request.data)
        super().request_setter(request)

    def set_method(self, method: str) -> None:
        self.__method = method
        self._logger.set_core_method(method)

    def get_method(self) -> str:
        return self.__method

    def set_url(self, url: str) -> None:
        self.__url = url
        self._logger.set_core_url(url)

    def get_url(self) -> str:
        return self.__url

    def set_headers(self, headers: dict) -> None:
        self.__headers = headers
        self._logger.set_core_request_headers(headers)

    def get_headers(self) -> dict:
        return self.__headers

    def set_parameters(self, data: dict) -> None:
        self.__parameters = data
        self._logger.set_core_request_body(data)

    def get_parameters(self) -> dict:
        return self.__parameters

    def set_response(self, response: dict, status=None) -> None:
        self._logger.set_proxy_response_body(response)
        self._logger.set_proxy_response_status_code(status)

        if status is not None:
            if 200 <= status < 300:
                response = self.on_success(response)
            if 400 <= status <= 500:
                response = self.on_error(response)
        self.__response = response

    def get_response(self) -> dict:
        return self.__response

    def on_success(self, response: dict) -> dict:
        return response

    def on_error(self, response: dict) -> dict:
        return response

    def send(self) -> tuple:
        response = requests.request(
            method=self.get_method(),
            url=self.get_url(),
            json=self.get_parameters(),
            headers=self.get_headers()
        )
        filtered_headers = {k: v for k, v in response.headers.items() if k not in self._not_allowed_headers}
        response.headers = filtered_headers

        self._logger.set_core_response_body(response.json())
        self._logger.set_core_response_status_code(response.status_code)

        self.set_response(response.json(), response.status_code)

        self._logger.write()

        return self.get_response(), response.headers, response.status_code

