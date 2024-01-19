from rest_framework.views import APIView
from core.Route import Route
from services.CustomRoute import CustomRoute
from django.core.cache import cache
from core.settings import CACHE_DEFAULT_TTL


class BotList(CustomRoute, APIView):

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return "/bots"

    def send(self) -> tuple:
        body = cache.get("body")
        headers = cache.get("headers")
        status_code = cache.get("status_code")

        if not body or not headers or not status_code:
            response_body, response_headers, response_status_code = super().send()
            cache.set_many(data={
                "body": response_body,
                "headers": response_headers,
                "status_code": response_status_code
            }, timeout=CACHE_DEFAULT_TTL)

            return response_body, response_headers, response_status_code
        else:
            return body, headers, status_code


