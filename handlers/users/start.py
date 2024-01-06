import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.inlinekey import til
from keyboards.default.userkey import boshmenuUz,boshmenuUs,boshmenuRu



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.from_user.id
    username = message.from_user.username
    fulname = message.from_user.first_name
    date = str(message.date)
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(chat_id=chat_id,first_name=fulname,username=username,date=date)
        for admin in ADMINS:
            await bot.send_message(chat_id=admin,text=f" {message.from_user.first_name} bazaga qoshildi")
    except sqlite3.IntegrityError as err:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=err)

    user = db.select_user(chat_id=chat_id)

    if user[4] == None:
        await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык", reply_markup=til)
    elif user[4] == "uz":
        await message.answer(f"Kerakli bo'limni tanlang {message.from_user.first_name}",reply_markup=boshmenuUz)
    elif user[4] == "ru":
        await message.answer(f"Выберите нужный раздел {message.from_user.first_name}",reply_markup=boshmenuRu)
    elif user[4] == "en":
        await message.answer(f"Select the desired section {message.from_user.first_name}",reply_markup=boshmenuUs)
        
        
@dp.message_handler(text="🏢 Kompaniya haqida")
async def kopUz(message: types.Message):
    photo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Headquarter_of_InBazar.jpg/800px-Headquarter_of_InBazar.jpg?20210320084526"
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption="Inbazar internet magazin",
    )


@dp.message_handler(text="🏢 О компании")
async def kopRu(message: types.Message):
    photo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Headquarter_of_InBazar.jpg/800px-Headquarter_of_InBazar.jpg?20210320084526"
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption="Интернет-магазин Инбазар",
    )


@dp.message_handler(text="🏢 About the company")
async def kopUs(message: types.Message):
    photo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Headquarter_of_InBazar.jpg/800px-Headquarter_of_InBazar.jpg?20210320084526"
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo_url,
        caption="Inbazar online store",
    )