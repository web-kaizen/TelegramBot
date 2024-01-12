import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telegram_bot.handler import Handler
import os
import django

from telegram_bot.tg_services.Account import UserAuthorizationService
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
API_TOKEN = '6391076892:AAGwQHQMKEBAycF_GSrU_r0Zr3-kVCyZTA4'
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher()
handler = Handler()
REGISTERED = False


async def main_menu(msg: Message, registered=REGISTERED):
    ...


async def start_use(callback: CallbackQuery):
    ...


async def select_chat_model(callback: CallbackQuery) -> None:
    ...


async def select_model_gpt(callback: CallbackQuery):
    ...


async def register_user(callback: CallbackQuery):
    ...


async def free_mode(msg: Message):
    ...


async def main() -> None:
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())