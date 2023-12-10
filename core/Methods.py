from rest_framework.response import Response


class Methods:

    def request_setter(self, request):
        self.set_url(request.build_absolute_uri())
        self.set_method(request.method)
        self.set_request(request.data)
        self.set_headers(dict(request.headers))
        if request.method == "GET":
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
