import asyncio
from itertools import groupby
from operator import itemgetter
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from django.core.cache import cache
from .start import start
from services import DialogueOptionalUpdate, BotList
from .start_dialogue import get_cached_data

router = Router()

DIALOGUE_OPTIONAL_UPDATE_OPTIONS: dict = {
    200: object,
    204: object,
    400: "Переданы некорректные данные!⚠️",
    401: "Invalid access token!⚠️",
    403: "Dialogue access denied⚠️",
    404: "No data was found, please try again later!⚠️",
    409: "Bot version conflict!⚠️",
    422: "Bot error⚠️",
    500: "Internal server error, please try again later!⛔️"
}


@router.callback_query(F.data.startswith('continue_dialog'))
async def change_dialogue_options(clb):
    tg_user_id = clb.from_user.id
    select_option_message = clb.message
    selected_model = int(clb.data.split(":")[1])
    token, dialogue_id, model_id = await get_cached_data(user_id=tg_user_id)

    data = {
        "bot_id": selected_model
    }
    dialogue_update = DialogueOptionalUpdate.DialogueOptionalUpdate(dialogue_id=dialogue_id, data=data, token=token, need_execute_local=True)
    dialogue_update_data = dialogue_update.get_response()  # Возвращает {'bot_id': 2}

    dialogue_update_result = DIALOGUE_OPTIONAL_UPDATE_OPTIONS[dialogue_update._status_code]
    if dialogue_update_result is object:
        successful_data = await clb.message.answer("Модель успешно изменена!")
        await asyncio.sleep(0.5)
        await successful_data.delete()

        dialogue_update_data["id"] = dialogue_id
        dialogue_update_data["name"] = f"Dialogue No.{dialogue_id}"
        cache.set(
            key=f"dialogue_{tg_user_id}",
            value=dialogue_update_data,
            timeout=60 * 60 * 24 * 5  # 5 день
        )

        await clb.message.answer("Введите свой запрос!👨‍💻")
        await select_option_message.delete()

    elif type(dialogue_update_result) is str:
        await clb.message.answer(text=dialogue_update_result)
        return await start(clb=clb)


@router.message(F.text.lower() == "продолжить диалог")
async def continue_dialog(msg: Message):
    tg_user_id = msg.from_user.id
    token, dialogue_id, model_id = await get_cached_data(user_id=tg_user_id)
    bot_list_response = BotList.BotList(need_execute_local=True, use_cache=False).get_response()

    '''
    Группируем данные по авторам 
    ({Автор: [модели -> [id, name]]}) -> 
    {'OpenAI': [
        [2, 'Gpt-3.5 16K'],
        [3, 'Gpt-4 8K']
    ]}
    '''
    bot_list_result = {key: [[item["id"], item["model_name"]]
                             for item in group
                             if item['status_code'] == "active"
                             and
                             item["id"] != model_id]
                       for
                       key, group in
                       groupby(bot_list_response, key=itemgetter("author"))}

    builder = InlineKeyboardBuilder()

    for author, models in bot_list_result.items():
        for model_id, model_name in models:
            print(model_id, model_name)
            builder.add(InlineKeyboardButton(text=model_name, callback_data=f"continue_dialog:{model_id}"))

    builder.row(InlineKeyboardButton(text='Отменить', callback_data="cancel_changes"))

    ended_dialogue_message = await msg.answer(text="Понял! ✅", reply_markup=ReplyKeyboardRemove())  # удаляем кастомную клавиатуру
    await asyncio.sleep(0.5)
    await ended_dialogue_message.delete()

    await msg.answer(
        text="Выберите новую модель с которой хотите продолжить ваш диалог."
             "Все данные будут сохранены, поэтому выбранная модель будет 'помнить' весь диалог.",
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "cancel_changes")
async def cancel_changes(clb: CallbackQuery):
    select_option_message = clb.message
    await clb.message.answer("Можете продолжать общение! ✅")
    await select_option_message.delete()
