from develop.core.Route import Route
from rest_framework.views import APIView


class BotDetail(Route, APIView):
    def __init__(self):
        super().__init__()
        self.id = ""

    def get(self, request, id=None):
        self.id = id
        return super().get(request)

    def get_method(self):
        return "GET"

    def get_patch(self):
        return f"/bots/{self.id}"
