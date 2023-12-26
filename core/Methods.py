from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .settings import APP_ID, THIRD_PARTY_APP_URL


class Methods:

    def request_setter(self, request):
        self.set_method(self.get_method())
        self.set_url(f'{self._BASE_URL}{self.get_path()}')
        self.set_headers(dict(request.headers))

        if self.get_method() == "GET":
            self.set_parameters(dict(request.query_params))
        else:
            self.set_parameters(request.data)

    def get(self, request):
        self.request_setter(request)
        response, headers, status_code = self.send()
        if type(response) == str:
            return HttpResponse(status=status_code, content=response, headers=headers)
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
