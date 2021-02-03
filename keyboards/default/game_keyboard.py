from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

game_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Слот"),
            KeyboardButton(text="Кости")
        ],
        [
            KeyboardButton(text="Дартс"),
            KeyboardButton(text="Угадай число")
        ],
        [
            KeyboardButton(text="Сапер"),
            KeyboardButton(text="Какая-то хуйня")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)


slot_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Крутить")
        ],
        [
            KeyboardButton(text="Изменить баланс")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)