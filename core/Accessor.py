from .Methods import Methods


class Accessor(Methods):
    def __init__(self):
        self.__method: str = None
        self.__parameters: dict = {}
        self.__response: dict = {}
        self.__headers: dict = {}
        self.__request: dict = {}
        self.__url: str = None
        self.__status_code: int = None

    def set_url(self, url: str) -> None:
        self.__url = url

    def get_url(self) -> str:
        return self.__url

    def set_proxy_method(self, method: str) -> None:
        self.__method = method

    def get_proxy_method(self) -> str:
        return self.__method

    def allowed_client_headers(self, headers: dict) -> dict:
        allowed_headers = ["Authorization", "Content-Type"]
        headers_res = {}
        for key, value in headers.items():
            if key in allowed_headers:
                headers_res[key] = value
        return headers_res

    def set_headers(self, headers: dict) -> None:
        self.__headers = headers

    def get_headers(self) -> dict:
        return self.__headers

    def set_parameters(self, data: dict) -> None:
        self.__parameters = data

    def get_parameters(self) -> dict:
        return self.__parameters

    def set_request(self, data: dict) -> None:
        self.__request = data

    def get_request(self) -> dict:
        return self.__request

    def set_response(self, response: dict, status=None) -> None:
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

