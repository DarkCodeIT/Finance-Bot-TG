import asyncio
from aiogram import Bot, Dispatcher
from icecream import ic
from dotenv import load_dotenv
import os

from bot.handler import (command_handler,
                     admin_handler,
                     callback_query_handler)


async def start_bot() -> None:

    load_dotenv()

    bot = Bot(os.getenv("TOKEN"))
    dp = Dispatcher()

    dp.include_routers(
        command_handler.router,
        admin_handler.router,
        callback_query_handler.router
    )

    try:
        ic("Bot is Started...")
        await dp.start_polling(bot)

    except Exception as ex:
        ic(ex)

asyncio.run(start_bot())