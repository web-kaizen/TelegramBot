import time

import django
import os
""" DJANGO SETUP """
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from services import BotList, BotDetail, DialogueList, DialogueDetail, EmailVerificationCheck, EmailVerificationResend, EmailVerificationVerify, Register, Login, Logout


bot_list = BotList.BotList(need_execute_local=True)
bot_list_response = bot_list.get_response()
print(f"BotList: {bot_list_response}")

time.sleep(1)

bot_details = BotDetail.BotDetail(bot_id=1, need_execute_local=True)
bot_details_response = bot_details.get_response()
print(f"BotDetail: {bot_details_response}")

time.sleep(1)

register = Register.Register(need_execute_local=True, data={"email": "telegram_admin@admin.ru", "password": "telegram12345"})
register_response = register.get_response()
print(f"Register: {register_response}")

time.sleep(1)

login = Login.Login(need_execute_local=True, data={"email": "telegram_admin@admin.ru", "password": "telegram12345"})
login_response = login.get_response()
print(f"Login: {login_response}")

time.sleep(1)

dialogue_list = DialogueList.DialogueList(method="GET", need_execute_local=True, token=login_response["access_token"])
dialogue_list_response = dialogue_list.get_response()
print(f"DialogueList: {dialogue_list_response}")

time.sleep(1)

dialogue_details = DialogueDetail.DialogueDetail(method="GET", dialogue_id=2, need_execute_local=True, token=login_response["access_token"])
dialogue_details_response = dialogue_details.get_response()
print(f"DialogueDetail: {dialogue_details_response}")

time.sleep(1)

email_check = EmailVerificationCheck.EmailVerificationCheck(need_execute_local=True, token=login_response["access_token"])
email_check_response = email_check.get_response()
print(f"EmailCheck: {email_check_response}")

time.sleep(1)

email_resend = EmailVerificationResend.EmailVerificationResend(need_execute_local=True, token=login_response["access_token"])
email_resend_response = email_resend.get_response()
print(f"EmailResend: {email_resend_response}")

time.sleep(1)

email_verify = EmailVerificationVerify.EmailVerificationVerify(need_execute_local=True, token=login_response["access_token"])
email_verify_response = email_verify.get_response()
print(f"EmailVerify: {email_verify_response}")

time.sleep(1)

logout = Logout.Logout(need_execute_local=True, token=login_response["access_token"])
logout_response = logout.get_response()
print(f"Logout: {logout_response}")


# @dp.callback_query(F.data == 'select_model')
# async def select_chat_model(callback: CallbackQuery) -> None:
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text='GPT',
#         callback_data='select_model_GPT')
#     )
#     builder.add(InlineKeyboardButton(
#         text='SBER',
#         callback_data='select_model_SBER')
#     )
#     builder.add(InlineKeyboardButton(
#         text='YANDEX',
#         callback_data='select_model_YANDEX')
#     )