import os, django, asyncio, logging
from aiogram import Dispatcher, Bot, F, Router
from tg_services import start, main_menu

''' django setup '''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

router = Router()


async def main() -> None:
    token: str = os.environ.get('API_TOKEN')
    bot = Bot(token=token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router=router)
    dp.message.register(start.start)
    dp.message.register(main_menu.main_menu)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        print("Error: ", ex)