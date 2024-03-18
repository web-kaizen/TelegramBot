from aiogram import Router, F
from aiogram.types import CallbackQuery
from django.core.cache import cache
from django.db.models import Q

from .start import start
from services import DialogueCreate
from telegram_bot.models import UserStatistic

router = Router()

DIALOGUE_CREATE_OPTIONS: dict = {
    200: object,
    400: "Переданы некорректные данные!⚠️",
    401: "Invalid access token!⚠️",
    404: "No data was found, please try again later!⚠️",
    409: "Bot version conflict!⚠️",
    500: "Internal server error, please try again later!⛔️"
}


async def get_cached_data(user_id, clb=None) -> (str, int):
    cached_user = cache.get(key=f"telegram_bot_{user_id}")
    dialogue_cached = cache.get(key=f"dialogue_{user_id}", default={"id": 1, "bot_id": 1})
    if not cached_user:
        await start(clb=clb)
        cached_user = cache.get(key=f"telegram_bot_{user_id}")

    if not dialogue_cached:
        await start_dialogue()  # Пока бессмысленно, т.к. default в cache.get стоит

    token = cached_user['token']
    dialogue_id = dialogue_cached["id"]
    model_id = dialogue_cached["bot_id"]
    return token, dialogue_id, model_id


@router.callback_query(F.data.startswith('start_dialogue'))
async def start_dialogue(clb: CallbackQuery):
    tg_user_id = clb.from_user.id
    select_option_message = clb.message
    selected_model = int(clb.data.split(":")[1])
    token, dialogue_id, _ = await get_cached_data(user_id=tg_user_id, clb=clb)

    user_stats = UserStatistic.objects.filter(Q(user__user_id=tg_user_id) & Q(model_id=selected_model)).first()
    if user_stats.current_dialogues >= user_stats.max_dialogues:
        await clb.message.answer("Вы достигли максимального количества диалогов с этой моделью.")
        return

    data = {
        "name": f"Dialogue No.{dialogue_id + 1}",
        "bot_id": selected_model
    }

    dialogue = DialogueCreate.DialogueCreate(need_execute_local=True, token=token, data=data)
    dialogue_data = dialogue.get_response()

    await increment_dialogue_to_statistic(user_id=tg_user_id, selected_model=selected_model)

    dialogue_create_result = DIALOGUE_CREATE_OPTIONS[dialogue._status_code]
    if dialogue_create_result is object:
        cache.set(
            key=f"dialogue_{tg_user_id}",
            value=dialogue_data,
            timeout=60*60*24*5  # 5 дней
        )

        await clb.message.answer("Введите свой запрос!👨‍💻")
        await select_option_message.delete()

    elif type(dialogue_create_result) is str:
        await clb.message.answer(text=dialogue_create_result)
        if dialogue._status_code == 401:
            cache.delete(key=f"telegram_bot_{tg_user_id}")
        await start(clb=clb)
        await start_dialogue(clb=clb)


async def increment_dialogue_to_statistic(user_id: int, selected_model: int):
    userStats = UserStatistic.objects.filter(Q(user__user_id=user_id) & Q(model_id=selected_model)).first()
    userStats.current_dialogues += 1
    userStats.save()

