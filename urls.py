"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from services.BotList import BotList
from services.BotDetail import BotDetail
from services.Register import Register
from services.Login import Login
from services.Logout import Logout
from services.EmailVerificationCheck import EmailVerificationCheck
from services.EmailVerificationResend import EmailVerificationResend
from services.EmailVerificationVerify import EmailVerificationVerify
from services.DialogueList import DialogueList
from services.DialogueDetail import DialogueDetail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v0/users", Register().as_view()),
    path("api/v0/users/login", Login().as_view()),
    path("api/v0/users/logout", Logout().as_view()),
    path("api/v0/users/email-verification/check", EmailVerificationCheck().as_view()),
    path("api/v0/users/email-verification/resend", EmailVerificationResend().as_view()),
    path("api/v0/users/email-verification/verify", EmailVerificationVerify().as_view()),
    path("api/v0/bots", BotList().as_view()),
    path("api/v0/bots/<int:bot_id>", BotDetail().as_view()),
    path("api/v0/dialogues", DialogueList.as_view()),
    path("api/v0/dialogues/<int:dialogue_id>", DialogueDetail.as_view())
]
