from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types import CallbackQuery
from .start_dialogue import get_cached_data
from services import DialogueList
from aiogram.utils import markdown
router = Router()


@router.callback_query(F.data == "account")
async def account(clb: CallbackQuery):
    tg_user_id = clb.from_user.id
    select_option_message = clb.message
    builder = InlineKeyboardBuilder().row(InlineKeyboardButton(text="<- BACK", callback_data='main_menu'))
    token, _, _ = await get_cached_data(user_id=tg_user_id)
    total_dialogues = len(DialogueList.DialogueList(need_execute_local=True, token=token).get_response()['result'])
    gpt_3_5__16k = total_dialogues // 5
    gpt_3_5__4k = total_dialogues - gpt_3_5__16k
    await clb.message.answer(
        text=f"""
    👨‍💻  Добро пожаловать, {markdown.text(f"|| {clb.from_user.first_name} ||")}
        ├ Ваш юзернейм: {markdown.text(f"|| @{clb.from_user.username} ||")}
        ├ Ваш ID: {markdown.text(f"|| {tg_user_id} ||")}
        ├ Ваш баланс: 0
        └ Ваш тариф: {"Premium" if clb.from_user.is_premium else "General"}

💳  Кол\-во диалогов: {total_dialogues} 
        ├ GPT\-3\.5 4k: {gpt_3_5__4k}
        ├ GPT\-3\.5 16k: {gpt_3_5__16k}
        ├ GPT\-4 8k: 0 
        ├ GPT\-4 32k: 0
        """,
        reply_markup=builder.as_markup(),
        parse_mode="MarkdownV2"
    )
    await select_option_message.delete()
