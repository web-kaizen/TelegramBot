import os, django, asyncio, logging
from aiogram import Dispatcher, Bot, F, Router
from tg_services.assets import router
''' django setup '''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from tg_services import start, main_menu, start_dialogue, select_model, help


async def main() -> None:
    token: str = os.environ.get('API_TOKEN')
    bot = Bot(token=token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router=router)
    dp.message.register(start.start)
    dp.message.register(main_menu.main_menu)
    dp.message.register(select_model.select_model)
    dp.message.register(help.help)
    dp.message.register(start_dialogue.start_dialogue)
    dp.message.register(start_dialogue.new_dialogue)
    dp.message.register(start_dialogue.free_mode)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        print("Error: ", ex)