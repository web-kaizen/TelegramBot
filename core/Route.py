import os
import requests
from requests import Response

from logger.Logger import Logger
from .Accessor import Accessor
from .settings import APP_ID, THIRD_PARTY_APP_URL


class Route(Accessor):
    def __init__(self):
        self.__APP_ID = APP_ID
        self.__BASE_URL = THIRD_PARTY_APP_URL

    def check_response(self, response: Response) -> dict | None:
        """Проверка response не содержание body используя headers["Content-Type"] (e.g. login)"""
        if 'Content-Type' in response.headers.keys():
            return response.json()
        else:
            return None

    def send(self):
        options_proxy = {
            "proxy_method": self.get_method(),
            "proxy_url": self.get_url(),
            "proxy_request_headers": self.get_headers(),
            "proxy_request_body": self.get_request(),
            "proxy_response_headers": self.get_headers(),
            "proxy_response_body": self.get_request(),
        }

        url = f'{self.__BASE_URL}{self.__APP_ID}'
        response = requests.request(
            method=self.get_method(),
            url=f"{url}{self.get_patch()}",
            json=self.get_parameters(),
            headers=self.allowed_client_headers(self.get_headers())
        )

        response_body = self.check_response(response)

        options_core = {
            "core_method": self.get_method(),
            "core_url": f"{url}{self.get_patch()}",
            "core_request_headers": self.get_headers(),
            "core_request_body": self.get_request(),
            "core_response_headers": dict(response.headers),
            "core_response_body": response_body,
            "core_response_status_code": response.status_code
        }

        logger = Logger(options=options_proxy | options_core)
        logger.write()

        response.headers.pop('Connection')
        response.headers.pop('Keep-Alive')
        return response_body, response.headers, response.status_code




