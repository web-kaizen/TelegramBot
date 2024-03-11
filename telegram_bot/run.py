import os, django, asyncio, logging
from aiogram import Dispatcher, Bot
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

''' django setup '''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from tg_services import start, main_menu, start_dialogue, select_model, help, quit_dialogue, free_mode, continue_dialog, account

token: str = os.environ.get('API_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()


async def main() -> None:
    dp.include_routers(
        start.router,
        main_menu.router,
        start_dialogue.router,
        select_model.router,
        help.router,
        account.router,
        quit_dialogue.router,
        continue_dialog.router,
        free_mode.router,
    )
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        print("Error: ", ex)
