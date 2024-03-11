from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telegram_bot.models import UserStatistic, User

router = Router()


@router.callback_query(F.data == "account")
async def account(callback: CallbackQuery):
    user_id = callback.from_user.id
    select_option_message = callback.message
    user = User.objects.filter(user_id=user_id).first()
    user_statistic = UserStatistic.objects.filter(user=user).order_by('model_id')

    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='Выбрать модель', callback_data=f"select_model"))
    builder.row(InlineKeyboardButton(text="<- BACK", callback_data='main_menu'))

    # user info
    text = \
        f''' 👨‍💻 Добро пожаловать, BotXchat
├ Ваш юзернейм: BotXchatBot
├ Ваш ID: {user.user_id}
├ Ваш баланс: {user.balance}
└ Язык бота: Русский '''

    # dialogues info
    text += '''\n💳 Кол-во Диалогов'''

    for user_model_info in user_statistic:
        text += f'''\n├ {user_model_info.name}: {user_model_info.current_dialogues}/{user_model_info.max_dialogues}'''

    await callback.message.answer(
        text=text,
        reply_markup=builder.as_markup()
    )
    await select_option_message.delete()
