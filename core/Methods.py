from rest_framework.response import Response


class Methods:

    def request_setter(self, request):
        self.set_url(request.build_absolute_uri())
        self.set_proxy_method(request.method)
        self.set_request(request.data)
        self.set_headers(dict(request.headers))
        ''' Доделать логику условия При Get -> 
        {
            "status": 400,
            "code": "invalid_email",
            "message": "Invalid parameter: email"
        }'''
        if request.method == "GET":
            self.set_parameters(request.query_params.dict())
        else:
            print(request.method)
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
