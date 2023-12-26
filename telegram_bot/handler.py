import django
import os
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from services import BotList, BotDetail, DialogueList, DialogueDetail, EmailVerificationCheck, EmailVerificationResend,EmailVerificationVerify, Register, Login, Logout
# from core.Route import Route

# botList = BotList()
# print(botList)
# new_request = requests.Request(method="GET", url="http://127.0.0.1:8000/api/v0/bots/")
# botList.get(new_request)

# botList.set_url("http://127.0.0.1:8000/api/v0/bots")
# data = botList.send()
response, headers, status_code = BotList.BotList(need_execute_local=True).send()
if status_code != 500 and status_code != 404:
    print(response)
else:
    print(status_code)

# response, headers, status_code = BotDetail.BotDetail(need_execute_local=True).send()
# if status_code != 500 and status_code != 404:
#     print(response)
# else:
#     print(status_code)


# response, headers, status_code = DialogueList.DialogueList(need_execute_local=True).send()
# if status_code != 500 and status_code != 404:
#     print(response)
# else:
#     print(status_code)

# response, headers, status_code = DialogueDetail.DialogueDetail(need_execute_local=True).send()
# if status_code != 500 and status_code != 404:
#     print(response)
# else:
#     print(status_code)

response, headers, status_code = EmailVerificationCheck.EmailVerificationCheck(need_execute_local=True).send()
if status_code != 500 and status_code != 404:
    print(response)
else:
    print(status_code)

response, headers, status_code = EmailVerificationResend.EmailVerificationResend(need_execute_local=True).send()
if status_code != 500 and status_code != 404:
    print(response)
else:
    print(status_code)


response, headers, status_code = EmailVerificationVerify.EmailVerificationVerify(need_execute_local=True).send()
if status_code != 500 and status_code != 404:
    print(response)
else:
    print(status_code)

response, headers, status_code = Register.Register(need_execute_local=True).send()
if status_code != 500 and status_code != 404:
    print(response)
else:
    print(status_code)

response, headers, status_code = Login.Login(need_execute_local=True).send()
if status_code != 500 and status_code != 404:
    print(response)
else:
    print(status_code)

response, headers, status_code = Logout.Logout(need_execute_local=True).send()
if status_code != 500 and status_code != 404:
    print(response)
else:
    print(status_code)

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