from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from itertools import groupby
from operator import itemgetter
from services import BotList

router = Router()


def add_buttons(builder, models, key_prefix, back_prefix):
    for model_id, name in models:
        print(f"{key_prefix}:{model_id}")
        builder.add(InlineKeyboardButton(text=name, callback_data=f"{key_prefix}:{model_id}"))
    builder.row(InlineKeyboardButton(text='<- BACK', callback_data=f'{back_prefix}'))


@router.callback_query(F.data.startswith("select_model"))
async def select_model(callback: CallbackQuery):

    bot_list_response = BotList.BotList(need_execute_local=True).get_response()

    # Группируем данные по авторам ({Автор: [модели]})
    bot_list_result = {key: [[item["id"], item["model_name"]] for item in group if item['status_code'] == "active"] for key, group in
                    groupby(bot_list_response, key=itemgetter("author"))}

    builder = InlineKeyboardBuilder()

    if callback.data == 'select_model':
        if len(bot_list_result) > 1:
            models = list(bot_list_result)
            add_buttons(builder, models, 'select_model', 'main_menu')

        else:
            key, models = bot_list_result.popitem()
            add_buttons(builder, models, 'start_dialogue', 'main_menu')

    else:
        key = callback.data.split(":")[1]
        models = bot_list_result[key]
        add_buttons(builder, models, 'start_dialogue', 'select_model')

    await callback.bot.answer_callback_query(callback.id)
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=builder.as_markup()
    )
