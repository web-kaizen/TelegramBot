from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from .start_dialogue import get_cached_data
from .quit_dialogue import quit_dialog
from string import punctuation
from services import MessageCreate

router = Router()

MESSAGE_CREATE_OPTIONS: dict = {
    200: object,
    400: "Переданы некорректные данные!⚠️",
    401: "Invalid access token!⚠️",
    403: "Dialogue access denied!⚠️",
    404: "No data was found, please try again later!⚠️",
    429: "Limit exceeded, please try again later!⚠️",
    500: "Internal server error, please try again later!⛔️"
}


async def reply_parse(replied_message: list) -> str:
    modified_text = ""
    for char in replied_message:
        if char in punctuation and char != "`":
            modified_text += "\\" + char
        else:
            modified_text += char

    return modified_text


@router.message(F.text)
async def free_mode(msg: Message):
    tg_user_id = msg.from_user.id
    token, dialogue_id, model_id = await get_cached_data(user_id=tg_user_id)

    print("MODEL:", model_id)
    print("DIALOGUE:", dialogue_id)

    data = {
        "text": msg.text,
        "bot_id": model_id
    }

    message_wait = await msg.answer(text="Печатаю... 👨‍💻")

    message = MessageCreate.MessageCreate(
        need_execute_local=True,
        data=data,
        token=token,
        dialogue_id=dialogue_id
    )
    await message_wait.delete()

    message_data = message.get_response()

    quit_button = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Новый диалог")]],
        resize_keyboard=True
    )

    message_create_result = MESSAGE_CREATE_OPTIONS[message._status_code]

    if message_create_result is object:
        replied_message = message_data[1]["text"]
        parsed_text: str = await reply_parse(replied_message=replied_message)
        return await msg.answer(text=parsed_text, parse_mode="MarkdownV2", reply_markup=quit_button)

    elif type(message_create_result) is str:
        return await quit_dialog(msg=msg, error=True)

