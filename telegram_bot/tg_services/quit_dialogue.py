import asyncio
from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types import Message, ReplyKeyboardRemove
from .start_dialogue import get_cached_data

router = Router()


@router.message(F.text.lower() == "новый диалог")
async def quit_dialog(msg: Message, error=False):
    tg_user_id = msg.from_user.id
    _, _, model_id = await get_cached_data(user_id=tg_user_id)
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Другая модель🔄", callback_data="select_model"))

    if error:
        text = "Выбранная модель не отвечает 😞. Пожалуйста выберите другую модель"
    else:
        text = "Пожалуйста выберите модель, с которой хотите начать новый диалог🤖"
        builder.add(InlineKeyboardButton(text="Та же модель⏩", callback_data=f"start_dialogue:{model_id}"))

        ended_dialogue_message = await msg.answer(text="Диалог завершен!✅", reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(0.5)
        await ended_dialogue_message.delete()

    builder.row(InlineKeyboardButton(text='<- BACK', callback_data="main_menu"))

    await msg.answer(
        text=text,
        reply_markup=builder.as_markup(),
        )
