from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="Список игр")
        ],
        [
            KeyboardButton(text="Настройки"),
            KeyboardButton(text="Кошелёк")
        ],
        [
            KeyboardButton(text="О сервисе"),
            KeyboardButton(text="Обратная свзяь")
        ]
    ],
    resize_keyboard=True
)
