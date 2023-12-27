import requests
from requests import Request


class HandMadeRequest:
    def __init__(
            self,
            method: str = None,
            uri: str = None,
            params: dict = None,
            data: dict = None
    ):
        self._method = method
        self._uri = uri
        self._params = params
        self._data = data

    def create_request(self) -> Request:
        request = requests.request(method=self._method, url=f"http://127.0.0.1:8000/api/v0{self._uri}", params=self._params, json=self._data)
        return request.json()

