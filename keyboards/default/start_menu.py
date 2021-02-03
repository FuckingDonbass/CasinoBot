from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подтверждаю✅")
        ]
    ],
    resize_keyboard=True
)
