from aiogram import executor
from handlers import dp
from loader import dp
# import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from states import Func
import asyncio

Func.select_all_to_bd()


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
