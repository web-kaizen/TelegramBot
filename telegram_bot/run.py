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
    log_dir = os.path.join(os.path.dirname(__file__), 'TelegramLogs')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    file_handler = logging.FileHandler(os.path.join(log_dir, 'logs_tg.log'))
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(module)s - %(funcName)s  - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        print("Error: ", ex)
