from aiogram import types
from keyboards.default import slot_menu
from states import Func, State
from loader import dp


@dp.message_handler(text="Слот")
async def slot(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play
    await message.answer(
        f"Приветсвуем вас в режиме \"Слот\", \nТекущий баланс: {user.balance} ₽\nТекущая ставка: {user.bet} ₽",
        reply_markup=slot_menu)


@dp.message_handler(text="Кости")
async def dice(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play


@dp.message_handler(text="Дартс")
async def darts(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play


@dp.message_handler(text="Сапёр")
async def sapper(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play


@dp.message_handler(text="Какая-то хуйня")
async def rename(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play
