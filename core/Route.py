import requests
from .Logger import Logger
from .settings import APP_ID, THIRD_PARTY_APP_URL
from .Methods import Methods


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

    def allowed_client_headers(self, headers: dict) -> dict:
        allowed_headers = ["Authorization", "Content-Type"]
        headers_res = {}
        for key, value in headers.items():
            if key in allowed_headers:
                headers_res[key] = value
        return headers_res

    # def check_response(self, response: Response) -> dict | None:
    #     """Проверка response не содержание body используя headers["Content-Type"] (e.g. logout)"""
    #     if response.status_code != 204:
    #         return response.json()
    #     else:
    #         return None

    def send(self) -> tuple:
        print(self.get_method())
        print(self.get_url())
        response = requests.request(
            method=self.get_method(),
            url=self.get_url(),
            # headers=self.allowed_client_headers(self.get_headers()),
            json=self.get_parameters(),
        )
        print(response)

        # response_body = self.check_response(response)

        # response.headers.pop('Connection')
        # response.headers.pop('Keep-Alive')
        self._logger.set_core_response_body(response.json())
        self._logger.set_core_response_status_code(response.status_code)

        self.set_response(response.json(), response.status_code)

        self._logger.write()

        return self.get_response(), {}, response.status_code

