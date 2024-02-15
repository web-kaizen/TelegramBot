from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .assets import WELCOME_MESSAGE


router = Router()


@router.callback_query(F.data == "main_menu")
async def main_menu(clb: CallbackQuery):
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='Модели', callback_data='select_model'))
    builder.row(InlineKeyboardButton(text='Профиль', callback_data='account'))
    builder.row(InlineKeyboardButton(text='Помощь', callback_data='help'))

    try:
        await clb.bot.edit_message_reply_markup(
            chat_id=clb.message.chat.id,
            message_id=clb.message.message_id,
            reply_markup=builder.as_markup()
        )
    except Exception as ex:
        await clb.answer(
            text=WELCOME_MESSAGE,
            reply_markup=builder.as_markup()
        )
