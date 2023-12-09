from rest_framework.response import Response


class Methods:

    def get(self, request):
        self.set_headers(dict(request.headers))
        self.set_parameters(request.query_params.dict())

        options = {
            "proxy_method": self.get_patch(),
            "proxy_url": f"{self.__BASE_URL}{self.__APP_ID}",
            "proxy_request_headers": self.get_headers(),
            "proxy_request_body": self.get_response(),
            "proxy_response_headers": self.get_headers(),
            "proxy_response_body": self.get_response(),
            "proxy_response_status_code": self.get_response()
        }

        response = self.send()
        self.set_response(response[0], response[1])

        return Response(status=response[1], data=self.get_response())

    def post(self, request):
        self.set_headers(dict(request.headers))
        self.set_parameters(request.data)
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())

    def put(self, request):
        self.set_headers(dict(request.headers))
        self.set_parameters(request.data)
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())

    def patch(self, request):
        self.set_headers(dict(request.headers))
        self.set_parameters(request.data)
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())

    def delete(self, request):
        self.set_headers(dict(request.headers))
        self.set_parameters(request.query_params.dict())
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())
