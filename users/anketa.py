# import re
# import asyncpg.exceptions
from aiogram.types import InlineKeyboardMarkup
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menuKeyboard import mainmenu
from keyboards.inline.inlineKeyboard import category_btn


from loader import dp, bot
from states.personalData import PersonalData

@dp.message_handler(text="📞 Zamdekan bilan aloqa")
async def enter_test(message: types.Message):
    await message.answer("Marhamat quyidagi raqamga qung'iroq qilishingiz mumkin")
    await message.answer('+998979238448', reply_markup=mainmenu)

@dp.message_handler(text="Dasturchi")
async def enter_test(message: types.Message):
    await message.answer("Marhamat quyidagi usernamega yozishingiz mumkun")
    await message.answer('@hyperman0011', reply_markup=mainmenu)

@dp.message_handler(text="Zamdekanga murojat")
async def enter_test(message: types.Message):
    await message.answer("Murojatingizni yozib qoldiring!!!")
    await PersonalData.murojat.set()

@dp.message_handler(state=PersonalData.murojat)
async def answer_phone(message: types.Message, state: FSMContext):
    murojat = message.text
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    category_markup = await category_btn(user_id)
    await bot.send_message(chat_id=1610668492, text=f"Ism : {full_name}\nUsername : @{username}\nMurojat : {murojat}", reply_markup=category_markup)
    await message.answer(
        "Murojatingiz uchun raxmat\ntez orada murojatingiz ko'rib chiqiladi va murojatingizga javob olasiz",
        reply_markup=mainmenu)
    await state.finish()



@dp.callback_query_handler(lambda c: 'javob' in c.data, state='*')
async def answer_input_step(callback_query: types.CallbackQuery, state: FSMContext):
    _, user_id = callback_query.data.split('|')
    async with state.proxy() as data:
        data['user_id'] = user_id
    await bot.send_message(callback_query.from_user.id, 'Javobingizni yozing')
    await PersonalData.answer.set()


@dp.message_handler(state=PersonalData.answer)
async def answer_send_step(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text

    await bot.send_message(data['user_id'], data['answer'])
    await state.finish()