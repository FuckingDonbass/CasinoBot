from aiogram import types
from loader import dp
from states import State, Func
from aiogram.types import DiceEmoji, Dice
import asyncio


@dp.message_handler(content_types="dice")
async def dice(message: types.Message):
    user = Func.get_object(message.from_user.id)
    if message.dice.emoji == "🎲":
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
                user.state = State.Null
                bot_value = await message.answer_dice("🎲")
                await asyncio.sleep(3)
                user.state = State.Dice
                if bot_value.dice.value > message.dice.value:
                    user.balance -= user.bet
                    await message.answer(f"К сожалению, вы проиграли {user.bet} ₽\nВаш баланс: {user.balance} ₽")
                elif bot_value.dice.value < message.dice.value:
                    user.balance += user.bet
                    await message.answer(f"Поздравялем, вы выиграли {user.bet} ₽\nВаш баланс: {user.balance} ₽")
                else:
                    await message.answer(f"Ничья\nВаш баланс: {user.balance} ₽")
        user.state = State.Play
