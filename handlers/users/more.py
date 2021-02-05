from aiogram import types
from keyboards.default import game_menu, slot_menu
from states import State, Func
from loader import dp


@dp.message_handler(text="Изменить ставку")
async def change_bet(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    user.state = State.ChangeBet
    await message.answer("Укажите желаемый размер ставки в рублях!", reply_markup=None)


@dp.message_handler(text="Назад")
async def change_bet(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user.state == State.Play:
        await message.answer("Вы вернулись в меню игровых режимов", reply_markup=game_menu)


@dp.message_handler()
async def set_bet(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user.state == State.ChangeBet:
        try:
            bet = int(message.text)
            if bet > user.balance:
                await message.answer("Размер ставки превышает кол-во денег на балансе")
            elif bet < 1:
                await message.answer("Ставка не может быть меньше 1 ₽")
            else:
                user.bet = bet
                await message.answer("Ставка принятя", reply_markup=slot_menu)
        except ValueError:
            await message.answer("Введите число!")
