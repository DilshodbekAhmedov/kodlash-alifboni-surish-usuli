from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import mainmenu
from loader import dp

@dp.message_handler(text="menyular")
async def show_menu(message: Message):
    await message.answer("Bo'limni tanlang", reply_markup=mainmenu)