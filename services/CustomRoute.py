from core.Route import Route


class CustomRoute(Route):
    def set_response(self, response: dict | None, status=None) -> None:
        self._logger.set_proxy_response_body(response)
        self._logger.set_proxy_response_status_code(status)
        if response:
            if 'result' in response:
                super().set_response(response['result'], status)
                response['result'] = super().get_response()
            if 'error' in response:
                super().set_response(response['error'], status)
                response['error'] = super().get_response()
        self.__response = response
