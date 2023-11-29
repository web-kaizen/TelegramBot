from django.urls import path

from .classes.BotList import BotList
from .classes.BotDetail import BotDetail
from .classes.Register import Register
from .classes.Login import Login

urlpatterns = [
    path("api/v0/users", Register().as_view()),
    path("api/v0/users/login", Login().as_view()),
    path("api/v0/bots", BotList().as_view()),
    path("api/v0/bots/<int:id>", BotDetail().as_view()),
]