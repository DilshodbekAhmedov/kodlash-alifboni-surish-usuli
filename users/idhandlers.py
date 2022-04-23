from aiogram import types
from aiogram.dispatcher import filters
from keyboards.default.menuStart import menu
from loader import dp

SUPERUSER = [1610668492]
@dp.message_handler(chat_id='1610668492', commands='start')
async def id_filter_emample(msg:types.Message):
    await msg.answer("Xush kelibsiz SuperUSER!")
    await msg.answer("menularni bosing", reply_markup=menu)