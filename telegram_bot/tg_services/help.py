from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from itertools import groupby
from operator import itemgetter
from telegram_bot.tg_services.assets import HELP_MESSAGE

from services import BotList

router = Router()


@router.callback_query(F.data == "help")
async def help(callback: CallbackQuery):
    select_option_message = callback.message

    bot_list_response = BotList.BotList(need_execute_local=True).get_response()

    # Группируем данные по авторам
    bot_list_result = {key: [item["model_name"] for item in group] for key, group in
                    groupby(bot_list_response, key=itemgetter("author"))}

    bot_list_text = str()

    for developer, models in bot_list_result.items():
        bot_list_text += f"Разработчик {developer}:\n"
        for model in models:
            bot_list_text += f"- {model}\n"
        bot_list_text += "\n"

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Выбрать модель', callback_data=f"select_model"))
    builder.row(InlineKeyboardButton(text="<- BACK", callback_data='main_menu'))

    await callback.message.answer(
        text=f"{HELP_MESSAGE}\n{bot_list_text}",
        reply_markup=builder.as_markup()
    )
    await select_option_message.delete()
