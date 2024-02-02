import random, string, os, django
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telegram_bot.run import router


@router.callback_query(F.data == "main_menu")
async def main_menu(clb: CallbackQuery):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='Модели', callback_data='select_model'))
    builder.row(InlineKeyboardButton(text='Профиль', callback_data='account'))
    builder.row(InlineKeyboardButton(text='Помощь', callback_data='help'))

    await clb.answer(
        text="""
        Добро пожаловать в Bot-X!\n
Я ваш личный телеграмм-помощник, который облегчит вам жизнь, отвечая на вопросы и поддерживая с вами общение.\n
Чтобы начать диалог, выберите одну из моделей ниже и задайте интересующий вас вопрос.
        """,
        reply_markup=builder.as_markup()
    )