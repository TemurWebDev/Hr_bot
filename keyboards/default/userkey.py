from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


boshmenuUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏢 Kompaniya haqida"),
        ],
        [
            KeyboardButton(text="🖋 Vakansiya"),
        ],
        [
            KeyboardButton(text="🇷🇺/🇺🇿/🇺🇸 Til")
        ],
    ],
    resize_keyboard=True
)



boshmenuUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏢 About the company"),
        ],
        [
            KeyboardButton(text="🖋 Job vacancy"),
        ],
        [
            KeyboardButton(text="🇷🇺/🇺🇿/🇺🇸 Language")
        ],
    ],
    resize_keyboard=True
)


boshmenuRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏢 О компании"),
        ],
        [
            KeyboardButton(text="🖋 Вакансия"),
        ],
        [
            KeyboardButton(text="🇷🇺/🇺🇿/🇺🇸 Язык")
        ],
    ],
    resize_keyboard=True
)


bekorUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bekor qilish"),
        ],
    ],
    resize_keyboard=True
)

bekorUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cancellation"),
        ],
    ],
    resize_keyboard=True
)


bekorRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отмена"),
        ],
    ],
    resize_keyboard=True
)