from aiogram import types
# from keyboards.default import slot_menu
# from keyboards.default import main_menu
from states import Func
from loader import dp
import asyncio


@dp.message_handler(text="Крутить")
async def slot(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user is None:
        await message.answer("Вы не зарегестрированы в системе, используйте команду //start")
    else:
        balance, bet = user.balance, user.bet
        if bet < 1:
            await message.answer("Ставка не может быть меньше 1₽")
        elif bet > balance:
            await message.answer("Ставка не может быть большеб чем кол-во денег на счету!")
        else:
            dice = await message.answer_dice("🎰")
            slot_value = dice.dice.value
            if slot_value == 22 or slot_value == 43 or slot_value == 64 or slot_value == 1:
                win = bet * 15
                balance += win
                user.balance = balance
                await asyncio.sleep(2)
                await message.answer(f"Поздравялем, вы выиграли {win} ₽\nВаш баланс: {balance} ₽")
            else:
                balance -= bet
                user.balance = balance
                await asyncio.sleep(2)
                await message.answer(f"К сожалению, вы проиграли {bet} ₽\nВаш баланс: {balance} ₽")
