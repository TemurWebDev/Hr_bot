import logging
from aiogram.types import CallbackQuery
from data.config import ADMINS

from loader import bot, dp, db
from aiogram import types

from keyboards.default.userkey import boshmenuUz,boshmenuUs,boshmenuRu


from keyboards.inline.inlinekey import til

@dp.callback_query_handler(text="uz")
async def til_uz(call: CallbackQuery):
    lang = call.data
    db.update_user_lang(lang=lang, chat_id=call.from_user.id)
    #user = db.select_user(chat_id=call.from_user.id)
    #await bot.send_message(chat_id=1363350178,text=f"{user[2]} ning tili {lang} bolib saqlandi")

    await call.message.delete()
    await call.message.answer(f"Salom {call.from_user.first_name}",reply_markup=boshmenuUz)



@dp.callback_query_handler(text="en")
async def til_en(call: CallbackQuery):
    lang = call.data
    db.update_user_lang(lang=lang, chat_id=call.from_user.id)
    #user = db.select_user(chat_id=call.from_user.id)
    #await bot.send_message(chat_id=1363350178,text=f"{user[2]} ning tili {lang} bolib saqlandi")

    await call.message.delete()
    await call.message.answer(f"Hello there {call.from_user.first_name}",reply_markup=boshmenuUs)


@dp.callback_query_handler(text="ru")
async def til_ru(call: CallbackQuery):
    lang = call.data
    db.update_user_lang(lang=lang, chat_id=call.from_user.id)
    #user = db.select_user(chat_id=call.from_user.id)
    #await bot.send_message(chat_id=1363350178,text=f"{user[2]} ning tili {lang} bolib saqlandi")

    await call.message.delete()
    await call.message.answer(f"Привет {call.from_user.first_name}",reply_markup=boshmenuRu)



@dp.message_handler(commands='language')
async def lang_update(message:types.Message):
    await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)

@dp.message_handler(text="🇷🇺/🇺🇿/🇺🇸 Til")
async def lang_updateUz(message:types.Message):
    await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)

@dp.message_handler(text="🇷🇺/🇺🇿/🇺🇸 Language")
async def lang_updateUs(message:types.Message):
    await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)

@dp.message_handler(text="🇷🇺/🇺🇿/🇺🇸 Язык")
async def lang_updateRu(message:types.Message):
    await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)