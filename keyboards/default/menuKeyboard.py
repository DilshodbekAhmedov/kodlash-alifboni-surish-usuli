from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mainmenu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Zamdekanga murojat'),
            KeyboardButton(text="📞 Zamdekan bilan aloqa"),
            KeyboardButton(text="Dasturchi"),
        ],
    ],
    resize_keyboard=True
)