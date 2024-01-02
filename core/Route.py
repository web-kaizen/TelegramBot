import inspect
from django.core.management.commands.runserver import Command
import requests
from .Logger import Logger
from .settings import APP_ID, THIRD_PARTY_APP_URL, LOCALHOST, BASE_URI
from .Methods import Methods


class Route(Methods):
    def __init__(self, need_execute_local=False, *args, **kwargs):
        self._APP_ID = APP_ID
        self._THIRD_PARTY_APP_URL = THIRD_PARTY_APP_URL
        self._method: str | None = None
        self._parameters: dict | None = None
        self._response: dict | None = None
        self._headers: dict | None = None
        self._url: str | None = None
        self._status_code: int | None = None
        self._not_allowed_headers = ('Connection', 'Keep-Alive', "Content-Length", "Transfer-Encoding", "Content-Encoding")

        self._logger = Logger()
        if need_execute_local:
            request = requests.Request(
                method=self.get_method(),
                url=f"{self._THIRD_PARTY_APP_URL}{self._APP_ID}{self.get_path()}",
            )
            other_params: list = ["data", "query_params", "json", "headers"]
            for param in other_params:
                if param in inspect.signature(self.__init__).parameters:
                    setattr(request, param, getattr(self, param))
                else:
                    setattr(request, param, {})

            getattr(self, self.get_method().lower())(request)

    def request_setter(self, request):
        self._logger.set_proxy_method(request.method)
        try:
            self._logger.set_proxy_url(request.build_absolute_uri())
        except Exception as ex:
            self._logger.set_proxy_url(f"{LOCALHOST}{BASE_URI}{self.get_path()}")
        self._logger.set_proxy_request_headers(dict(request.headers))
        if self.get_method() == "GET":
            self._logger.set_proxy_request_body(dict(request.query_params))
        else:
            self._logger.set_proxy_request_body(request.data)
        super().request_setter(request)

    def set_method(self, method: str) -> None:
        self._method = method
        self._logger.set_core_method(method)

    def get_method(self) -> str:
        return self._method

    def set_url(self, url: str) -> None:
        self._url = url
        self._logger.set_core_url(url)

    def get_url(self) -> str:
        return self._url

    def set_headers(self, headers: dict) -> None:
        if "Host" in headers.keys():
            headers.pop("Host")
        self._headers = headers
        self._logger.set_core_request_headers(headers)

    def get_headers(self) -> dict:
        return self._headers

    def set_parameters(self, data: dict) -> None:
        self._parameters = data
        self._logger.set_core_request_body(data)

    def get_parameters(self) -> dict:
        return self._parameters

    def set_response(self, response: dict | None, status=None) -> None:
        self._logger.set_proxy_response_body(response)
        self._logger.set_proxy_response_status_code(status)
        if response is not None and status is not None:
            if 200 <= status < 300:
                response = self.on_success(response)
            if 400 <= status <= 500:
                response = self.on_error(response)
        self._response = response

    def get_response(self) -> dict | None:
        return self._response

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

        content_type = response.headers.get("Content-Type", "")

        response_body = response.text if response.text else None

        if 'application/json' in content_type:
            response_body = response.json()

        self._logger.set_core_response_headers(dict(response.headers))
        self._logger.set_core_response_body(response_body.copy() if response_body else response_body)
        self._logger.set_core_response_status_code(response.status_code)

        filtered_headers = {k: v for k, v in response.headers.items() if k not in self._not_allowed_headers}
        response.headers = filtered_headers

        response.headers.update({
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        })

        self.set_response(response_body, response.status_code)
        self._logger.set_proxy_response_headers(response.headers)

        self._logger.write()

        return self.get_response(), response.headers, response.status_code

