from aiogram import types
from keyboards.default import start_menu
from keyboards.default import main_menu
from states import User, Func
from loader import dp
from loader import listBD


@dp.message_handler(commands=["start"])
async def welcome_key(message: types.Message):
    user_id, f_name = message.from_user.id, message.from_user.first_name
    if Func.get_id(user_id) is None:
        await message.answer("Вы подтверждатете, что ознакомились и согласны с условиями предоставления услуг?",
                             reply_markup=start_menu)
    else:
        await message.answer(f"С возвращением {f_name}!", reply_markup=main_menu)


@dp.message_handler(text=["Подтверждаю✅"])
async def accept_key(message: types.Message):
    user_id = message.from_user.id
    if Func.get_id(user_id) is None:
        listBD.append(User(user_id))
        user = Func.get_object(user_id)
        Func.save_to_bd(user_id, objects=user)
        await message.answer(f"Приятной игры!", reply_markup=main_menu)
