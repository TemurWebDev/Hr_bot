from aiogram import types
import logging
from data.config import ADMINS
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.userkey import boshmenuUz,boshmenuRu,boshmenuUs





@dp.message_handler(text=["Bekor qilish","Cancellation","Отмена"],state='*')
async def stateend(message: types.Message, state: FSMContext):
    user = db.select_user(chat_id=message.from_user.id)
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)

    await state.finish()
    if user[4] == 'uz':
        await message.answer("Kerakli bo'limni tanlang!",reply_markup=boshmenuUz)
    if user[4] == 'ru':
        await message.answer("Выберите нужный раздел!",reply_markup=boshmenuRu)
    if user[4] == 'en':
        await message.answer("Select the desired section!",reply_markup=boshmenuUs)
    