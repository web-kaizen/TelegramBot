from rest_framework.response import Response


class Methods:

    def get(self, request):
        self.set_parameters(request.query_params.dict())
        response = self.send()
        self.set_response(response[0], response[1])
        return Response(status=response[1], data=self.get_response(), headers=self.get_headers())

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
