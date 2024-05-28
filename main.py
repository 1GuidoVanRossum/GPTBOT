import asyncio
import logging
from aiogram import Bot, Dispatcher
import os

from app.database_4RA import create_db
from app.handlers import router

token = '6775089578:AAG5mKlJjNkcwh5Sipge0iZrq5EpuB1Y8HM'

async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await create_db()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
