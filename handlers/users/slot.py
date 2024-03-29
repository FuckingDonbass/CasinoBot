from aiogram import types
from states import Func, State
from loader import dp
import asyncio


@dp.message_handler(text="Крутить")
async def slot(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user.state == State.Null:
        return None
    else:
        if user.balance == 0:
            await message.answer("Перед началом игры необходимо пополнить баланс")
        elif user.bet < 1:
            await message.answer("Ставка не может быть меньше 1₽")
        elif user.bet > user.balance:
            await message.answer("Ставка не может быть больше чем кол-во денег на счету!")
        else:
            dice = await message.answer_dice("🎰")
            slot_value = dice.dice.value
            user.state = State.Null
            await asyncio.sleep(2)
            if slot_value == 22 or slot_value == 43 or slot_value == 64 or slot_value == 1:
                win = user.bet * 10
                user.balance += win
                await message.answer(f"Поздравялем, вы выиграли {win} ₽\nВаш баланс: {user.balance} ₽")
            else:
                user.balance -= user.bet
                await message.answer(f"К сожалению, вы проиграли {user.bet} ₽\nВаш баланс: {user.balance} ₽")
            user.state = State.Slot
