from develop.core.Route import Route


class CustomRoute(Route):
    def set_response(self, response, status=None):
        if 'result' in response:
            super().set_response(response['result'], status)
            response['result'] = super().get_response()
        if 'error' in response:
            super().set_response(response['error'], status)
            response['error'] = super().get_response()
        self.response = response
