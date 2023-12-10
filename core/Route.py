import os
import requests

from logger.Logger import Logger
from .Accessor import Accessor
from .settings import APP_ID, THIRD_PARTY_APP_URL


class Route(Accessor):
    def __init__(self):
        self.__APP_ID = APP_ID
        self.__BASE_URL = THIRD_PARTY_APP_URL

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
            headers=self.get_headers()
        )

        options_core = {
            "core_method": self.get_method(),
            "core_url": f"{url}{self.get_patch()}",
            "core_request_headers": self.get_headers(),
            "core_request_body": self.get_request(),
            "core_response_headers": dict(response.headers),
            "core_response_body": response.json(),
            "core_response_status_code": response.status_code
        }

        logger = Logger(options=options_proxy | options_core)
        logger.write()
        print(True)

        self.set_response(response.json(), response.status_code)

        return self.get_response(), response.status_code



