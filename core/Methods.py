from rest_framework.response import Response
from rest_framework.views import APIView

from .settings import APP_ID, THIRD_PARTY_APP_URL


class Methods:

    def request_setter(self, request):
        self.set_method(self.get_method())
        self.set_url(f'{self._BASE_URL}{self._APP_ID}{self.get_path()}')
        self.set_headers(dict(request.headers))

        if self.get_method() == "GET":
            self.set_parameters(request.query_params.dict())
        else:
            self.set_parameters(request.data)

    def get(self, request):
        self.request_setter(request)
        response, headers, status_code = self.send()
        return Response(status=status_code, data=response, headers=headers)

    def post(self, request):
        self.request_setter(request)
        response, headers, status_code = self.send()
        return Response(status=status_code, data=response, headers=headers)

    def put(self, request):
        self.request_setter(request)
        response, headers, status_code = self.send()
        return Response(status=status_code, data=response, headers=headers)

    def patch(self, request):
        self.request_setter(request)
        response, headers, status_code = self.send()
        return Response(status=status_code, data=response, headers=headers)

    def delete(self, request):
        self.request_setter(request)
        response, headers, status_code = self.send()
        return Response(status=status_code, data=response, headers=headers)

    def options(self, request):
        self.request_setter(request)
        headers: dict | None = {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        }
        return Response(status=200, data=None, headers=headers)