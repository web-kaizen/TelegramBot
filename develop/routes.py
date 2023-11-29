import requests
from rest_framework.response import Response


class Methods:

    def get(self, request):
        self.set_parameters(request.query_params.dict())
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())

    def post(self, request):
        self.set_parameters(request.data)
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())

    def put(self, request):
        self.set_parameters(request.data)
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())

    def patch(self, request):
        self.set_parameters(request.data)
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())

    def delete(self, request):
        self.set_parameters(request.query_params.dict())
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response())


class Route(Methods):
    def __init__(self):
        self.parameters = []
        self.response = []
        self.APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'
        self.BASE_URL = 'http://core.webstktw.beget.tech/api/v0/apps/'

    def set_parameters(self, data):
        self.parameters = data

    def get_parameters(self):
        return self.parameters

    def set_response(self, response, status=None):
        if status is not None:
            if 200 <= status < 300:
                response = self.success(response)
            if 400 <= status <= 500:
                response = self.error(response)
        self.response = response

    def get_response(self):
        return self.response

    def send(self):
        url = f'{self.BASE_URL}{self.APP_ID}'
        response = requests.request(
            self.get_method(),
            f"{url}{self.get_patch()}",
            json=self.get_parameters()
        )
        return response.json(), response.status_code

    def success(self, response):
        return response

    def error(self, response):
        return response
