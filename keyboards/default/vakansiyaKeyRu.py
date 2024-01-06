from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


citykeyRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ташкент")
        ],
        [
            KeyboardButton(text="Отмена")
        ],
        
    ],
    resize_keyboard=True
)


filialkeyRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сергиле"),
            KeyboardButton(text="Коратош")
        ],
                [
            KeyboardButton(text="Беруний"),
            KeyboardButton(text="Юнусобод")
        ],
                [
            KeyboardButton(text="Индех"),
            KeyboardButton(text="Корасув")
        ],

        [
            KeyboardButton(text="Отмена")
        ],
        
    ],
    resize_keyboard=True
)

positionkeyRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Продавец"),
            KeyboardButton(text="Кассер")
        ],
        
        [
            KeyboardButton(text="Сторожить"),
            KeyboardButton(text="менеджер")
        ],

        [
            KeyboardButton(text="Отмена")
        ],
        
    ],
    resize_keyboard=True
)

studentkeyRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],

        [
            KeyboardButton(text="Отмена")
        ],
                
    ],
    resize_keyboard=True
)

salarykeyRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.5 Млн - 2 Млн"),
            KeyboardButton(text="2.5 Млн - 3.5 Млн")
        ],
        [
            KeyboardButton(text="4 Млн - 5 Млн"),
            KeyboardButton(text="5 Млн - 6 Млн")
        ],

        [
            KeyboardButton(text="Отмена")
        ],
                
    ],
    resize_keyboard=True
)

phonkeyRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Номер телефона",request_contact=True),
        ],

        [
            KeyboardButton(text="Отмена")
        ],
          
    ],
    resize_keyboard=True
)


yuborishkeyRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправка"),
            KeyboardButton(text="Отказ")
        ],
          
        [
            KeyboardButton(text="Отмена")
        ],
    ],
    resize_keyboard=True
)