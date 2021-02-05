from aiogram import types
from keyboards.default import game_menu
from states import Func, State
from loader import dp


@dp.message_handler(text=["Профиль"])
async def profile_key(message: types.Message):
    print()


@dp.message_handler(text=["Список игр"])
async def game_list_key(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.GameMenu
    await message.answer("Выберите интересующий вас режим, сюда нужно добавить краткую инструкцию",
                         reply_markup=game_menu)


@dp.message_handler(text=["Настройки"])
async def profile_key(message: types.Message):
    print()


@dp.message_handler(text=["Кошелёк"])
async def profile_key(message: types.Message):
    print()


@dp.message_handler(text=["О сервсисе"])
async def profile_key(message: types.Message):
    print()


@dp.message_handler(text=["Обратная связь"])
async def profile_key(message: types.Message):
    print()
