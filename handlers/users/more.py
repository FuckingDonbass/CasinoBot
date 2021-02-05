from aiogram import types
from keyboards.default import game_menu, slot_menu, main_menu, dice_menu
from states import State, Func
from loader import dp


@dp.message_handler(text="Изменить ставку")
async def change_bet(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user.state == State.Slot:
        user.state = State.ChangeBetSlot
        await message.answer("Укажите желаемый размер ставки в рублях!", reply_markup=None)
    elif user.state == State.Dice:
        user.state = State.ChangeBetDice
        await message.answer("Укажите желаемый размер ставки в рублях!", reply_markup=None)
    else:
        await message.answer("Дождитесь окончания игры перед тем как изменить ставку!", reply_markup=None)


@dp.message_handler(text="Назад")
async def change_bet(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user.state == State.Slot or State.Dice:
        user.state = State.GameMenu
        await message.answer("Вы вернулись в меню игровых режимов", reply_markup=game_menu)


@dp.message_handler(text=["Вернуться в главное меню"])
async def back_to_main_menu(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user.state == State.GameMenu:
        await message.answer("Вы вернулись в главное меню", reply_markup=main_menu)


@dp.message_handler()  # Принимаем изменение ставки
async def set_bet(message: types.Message):
    user_id = message.from_user.id
    user = Func.get_object(user_id)
    if user.state == State.ChangeBetSlot:
        try:
            bet = int(message.text)
            if bet > user.balance:
                await message.answer("Размер ставки превышает кол-во денег на балансе")
            elif bet < 1:
                await message.answer("Ставка не может быть меньше 1 ₽")
            else:
                user.bet = bet
                await message.answer(
                    "Ставка принятя!\n"
                    f"Текущий баланс: {user.balance} ₽"
                    f"\nТекущая ставка: {user.bet} ₽",
                    reply_markup=slot_menu)
                user.state = State.Slot
        except ValueError:
            await message.answer("Введите число!")
    elif user.state == State.ChangeBetDice:
        try:
            bet = int(message.text)
            if bet > user.balance:
                await message.answer("Размер ставки превышает кол-во денег на балансе")
            elif bet < 1:
                await message.answer("Ставка не может быть меньше 1 ₽")
            else:
                user.bet = bet
                await message.answer(
                    "Ставка принятя!\n"
                    f"Текущий баланс: {user.balance} ₽"
                    f"\nТекущая ставка: {user.bet} ₽",
                    reply_markup=dice_menu)
                user.state = State.Dice
        except ValueError:
            await message.answer("Введите число!")
