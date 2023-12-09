import os

import requests
from .Methods import Methods
from .settings import APP_ID, THIRD_PARTY_APP_URL


class Route(Methods):
    def __init__(self):
        self.__parameters = []
        self.__response = []
        self.__headers = []
        self.__APP_ID = APP_ID
        self.__BASE_URL = THIRD_PARTY_APP_URL

    ''' HEADERS '''

    def set_headers(self, headers: dict) -> None:
        self.__headers = headers

    def get_headers(self):
        return self.__headers

    """-----------"""

    def set_parameters(self, data):
        self.__parameters = data

    def get_parameters(self):
        return self.__parameters

    def set_response(self, response, status=None):
        if status is not None:
            if 200 <= status < 300:
                response = self.on_success(response)
            if 400 <= status <= 500:
                response = self.on_error(response)
        self.__response = response

    def get_response(self):
        return self.__response

    def send(self):
        url = f'{self.__BASE_URL}{self.__APP_ID}'
        response = requests.request(
            method=self.get_method(),
            url=f"{url}{self.get_patch()}",
            json=self.get_parameters(),
            headers=self.get_headers()
        )

        self.set_headers(dict(response.headers))

        return response.json(), response.status_code

    def on_success(self, response):
        return response

    def on_error(self, response):
        return response