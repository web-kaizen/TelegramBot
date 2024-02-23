import requests
from typing import Any, Coroutine
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from datetime import datetime
from django.core.cache import cache
from .main_menu import main_menu
from services import Register, Login
from telegram_bot.models import User

router = Router()


async def log_user(clb: CallbackQuery, user: User, login_status_options: dict, tg_user_id: int) -> Any:
    login = Login.Login(data={"email": user.email, "password": user.password}, need_execute_local=True)
    login_response = login.get_response()

    log_status_res = login_status_options[login._status_code]
    if type(log_status_res) is str:
        return await clb.answer(text=log_status_res)

    elif log_status_res is object:
        expires_in = login_response.get("expires_in", 60)
        token = login_response.get("access_token", None)

        if not token:
            await clb.answer("Token was not provided...")
            raise requests.exceptions.ProxyError("Invalid token")

        cache.set(key=f"telegram_bot_{tg_user_id}", value={"email": user.email, "token": token},
                  timeout=expires_in)


@router.message(Command("start"))
async def start(clb: CallbackQuery) -> Coroutine[Any, Any, None]:
    tg_user_id = clb.from_user.id
    register_status_options = {
        200: Login.Login,
        404: "No data was found, please try again later",
        409: "User already exists",
        500: "Server error, please try again later"
    }

    login_status_options = {
        200: object,
        401: "Invalid email or password",
        404: "No data was found, please try again later",
        500: "Server error, please try again later"
    }
    email, password = f"{tg_user_id}@telegram.org", str(round(datetime.now().timestamp()))
    user = User.objects.filter(email=email).first()

    if user:
        cached_user = cache.get(key=f"telegram_bot_{tg_user_id}")
        if not cached_user:
            await log_user(clb=clb, user=user, login_status_options=login_status_options, tg_user_id=tg_user_id)
    elif not user:
        user = User.objects.create(user_id=tg_user_id, email=email, password=password)
        register = Register.Register(data={"email": user.email, "password": user.password}, need_execute_local=True)
        register_response = register.get_response()
        reg_status_res = register_status_options[register._status_code]
        if type(reg_status_res) is str:
            await clb.answer(text=reg_status_res)
        elif reg_status_res is Login.Login:
            user.user_core_id = register_response.get("user_id", None)
            user.save()
            await log_user(clb=clb, user=user, login_status_options=login_status_options, tg_user_id=tg_user_id)

    return await main_menu(clb)
