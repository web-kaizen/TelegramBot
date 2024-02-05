from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from .assets import router
from django.core.cache import cache
from .start import start
from services import DialogueCreate, DialogueList, MessageCreate, MessageList


async def get_user_token(user_id, clb=None) -> str:
    # valid_token = DialogueList.DialogueList(
    #         need_execute_local=True,
    #         token=cache.get(key=f"telegram_bot_{user_id}")).get_response()
    # if "error" in valid_token and valid_token["error"]["code"] == "invalid_access_token":
    #     cache.delete(key=f"telegram_bot_{user_id}")
    #     await start(clb=clb)

    token = cache.get(key=f"telegram_bot_{user_id}")["token"]

    return token


@router.callback_query(F.data.startswith('start_dialogue'))
async def start_dialogue(clb: CallbackQuery, new_dialogue=False):
    selected_model = int(clb.data.split(":")[1]) + 1
    token: str = await get_user_token(user_id=clb.from_user.id, clb=clb)
    print(token)
    data = {
        "name": "New dialogue 1",
        "bot_id": selected_model
    }
    created_dialogue = DialogueCreate.DialogueCreate(need_execute_local=True, token=token, data=data).get_response()

    await free_mode(clb.message, selected_model)
    # builder = InlineKeyboardBuilder().add(InlineKeyboardButton(text="New dialogue", callback_data="new_dialogue"))
    # await clb.bot.edit_message_reply_markup(
    #     chat_id=clb.message.chat.id,
    #     message_id=clb.message.message_id,
    #     reply_markup=builder.as_markup()
    # )


@router.callback_query(F.data == "new_dialogue")
async def new_dialogue(clb: CallbackQuery):
    pass




@router.message()
async def free_mode(msg: Message = None, selected_model: int = None):
    token = await get_user_token(msg.from_user.id)
    data = {
        "text": msg.text,
        "bot_id": selected_model
    }
    replied_message = MessageList.MessageList(need_execute_local=True, data=data).get_response()
    answer_text = replied_message["result"][1]["text"]
    await msg.answer(text=f"{answer_text}")
    # answer = await start_dialogue(msg.text)
    # await msg.answer(text=f"Start_use: {answer}, Token: {token}")