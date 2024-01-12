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


@dp.message(Command('start'))
async def main_menu(msg: Message, registered=REGISTERED):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Model', callback_data='select_model'))
    builder.row(InlineKeyboardButton(text='Options', callback_data='options'))
    builder.row(InlineKeyboardButton(text='Start a dialogue', callback_data='dialogue'))
    builder.row(InlineKeyboardButton(text='Bots info', callback_data='get_bots_info'))
    if not registered:
        builder.row(InlineKeyboardButton(text='Register', callback_data='register'))

    await msg.answer(
        text='========  Выберите пункт меню:  =========',
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == 'dialogue')
async def start_use(callback: CallbackQuery):
    text = ('Тут мы делаем запрос к модели. \n'
            'Получаем какое-то приветствие и выдаем его пользователю.')
    await bot.answer_callback_query(callback.id)
    await callback.message.answer(text=text)


@dp.callback_query(F.data == 'select_model')
async def select_chat_model(callback: CallbackQuery) -> None:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='GPT', callback_data='select_model_GPT'))

    await bot.answer_callback_query(callback.id)
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == 'select_model_GPT')
async def select_model_gpt(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='GPT 3.5 4k', callback_data='select_model_GPT_3_5_4k'))
    builder.add(InlineKeyboardButton(text='GPT 4 16k', callback_data='select_model_GPT_4_0_16k'))
    builder.row(InlineKeyboardButton(text='<- BACK', callback_data='select_model'))

    await bot.answer_callback_query(callback.id)
    await bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == "select_model_GPT_3_5_4k")
async def select_model_gpt_3_5_4k(callback: CallbackQuery):
    text = ('Вы выбрали модель GPT 3.5 4k и мы это помним.\n'
            'Тут можно добавить описание.\n'
            'Или не добавить.')

    GPT_3_5_info = handler.bot_detail(bot_id=1)

    await bot.answer_callback_query(callback.id)
    await callback.message.answer(text=str(GPT_3_5_info))
    await main_menu(callback.message)


@dp.callback_query(F.data == "get_bots_info")
async def get_bots_info(callback: CallbackQuery):
    bots_info = handler.bot_list()

    await bot.answer_callback_query(callback.id)
    await callback.message.answer(text=str(bots_info))
    await main_menu(callback.message)


@dp.callback_query(F.data == "register")
def register_user(callback: CallbackQuery):
    userAuthorizationService = UserAuthorizationService()
    await callback.message.answer("Введите почту: ")
    await YourStateEnum.waiting_for_email.set()
    await userAuthorizationService.proceed_email(message=callback.message)
    await callback.message.answer("Введите пароль: ")
    await userAuthorizationService.proceed_password(message=callback.message)



@dp.message(F.text)
async def free_mode(msg: Message):
    text = ('Мы получили произвольный вопрос от пользователя.\n'
            f'Вот он: <b>{msg.text}</b>\n'
            'Обрабатываем, отвечаем: "бла-бла-бла"')
    await msg.answer(text=text)


async def main() -> None:
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
