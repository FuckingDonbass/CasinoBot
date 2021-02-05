from aiogram import types
from keyboards.default import slot_menu, dice_menu
from states import Func, State
from loader import dp


@dp.message_handler(text="Слот")
async def _slot(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Slot
    await message.answer(
        f"Приветсвуем вас в режиме \"Слот\", \nТекущий баланс: {user.balance} ₽\nТекущая ставка: {user.bet} ₽",
        reply_markup=slot_menu)


@dp.message_handler(text="Кости")
async def _dice(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Dice
    await message.answer(
        f"Приветсвуем вас в режиме \"Кости\", \nТекущий баланс: {user.balance} ₽\nТекущая ставка: {user.bet} ₽",
        reply_markup=dice_menu)


@dp.message_handler(text="Дартс")
async def _darts(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play


@dp.message_handler(text="Сапёр")
async def _sapper(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play


@dp.message_handler(text="Какая-то хуйня")
async def _rename(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.Play
