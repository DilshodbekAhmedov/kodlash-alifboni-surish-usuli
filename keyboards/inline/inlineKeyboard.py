from aiogram.types import InlineKeyboardButton ,InlineKeyboardMarkup
# from keyboards.inline.callback_data import course_callback
# i-usul


async def category_btn(pk):
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Javob yozish", callback_data=f"javob|{pk}")
            ]
        ]
    )
    return btn
