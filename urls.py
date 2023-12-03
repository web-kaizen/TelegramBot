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
from django.urls import path

from classes.BotList import BotList
from classes.BotDetail import BotDetail
from classes.Register import Register
from classes.Login import Login
from classes.Logout import Logout

from classes.EmailVerificationCheck import EmailVerificationCheck
from classes.EmailVerificationResend import EmailVerificationResend
from classes.EmailVerificationVerify import EmailVerificationVerify

urlpatterns = [
    path("api/v0/users", Register().as_view()),
    path("api/v0/users/login", Login().as_view()),
    path("api/v0/users/logout", Logout().as_view()),
    path("api/v0/users/email-verification/check", EmailVerificationCheck().as_view()),
    path("api/v0/users/email-verification/resend", EmailVerificationResend().as_view()),
    path("api/v0/users/email-verification/verify", EmailVerificationVerify().as_view()),
    path("api/v0/bots", BotList().as_view()),
    path("api/v0/bots/<int:id>", BotDetail().as_view()),
]
