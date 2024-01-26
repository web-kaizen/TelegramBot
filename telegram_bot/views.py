import random, string, os, django
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from django.core.cache import cache

''' django setup '''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from services import Register, Login
from telegram_bot.models import User

router = Router()


@router.message(Command("start"))
async def start(clb: CallbackQuery):
    email, password = f"{clb.from_user.id}@telegram.org", str(round(datetime.now().timestamp()))
    user = User.objects.get_or_create(
        email=email,
        defaults={
            "user_id": clb.from_user.id,
            "email": email,
            "password": generate_password_hash(password)
        })[0]

    cache_key = f"telegram_bot_{user.email}"
    authorized = cache.get(key=cache_key)

    if not authorized:
        Register.Register(data={"email": user.email, "password": user.password}, need_execute_local=True)
        login = Login.Login(data={"email": user.email, "password": user.password}, need_execute_local=True).get_response()
        expires_in, token = login["result"]["expires_in"], login["result"]["access_token"]

        cache.set(key=cache_key, value={"email": user.email, "token": token, "expires_in": expires_in}, timeout=expires_in)

    await main_menu(clb)
