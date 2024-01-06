from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


citykey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent")
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ],
        
    ],
    resize_keyboard=True
)


filialkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sergile"),
            KeyboardButton(text="Qoratosh")
        ],
                [
            KeyboardButton(text="Beruniy"),
            KeyboardButton(text="Yunusobod")
        ],
                [
            KeyboardButton(text="Index"),
            KeyboardButton(text="Qorasuv")
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ],
        
    ],
    resize_keyboard=True
)

positionkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sotuvchi"),
            KeyboardButton(text="Kasser")
        ],
        
        [
            KeyboardButton(text="Qorovul"),
            KeyboardButton(text="Ish boshqaruvchi")
        ],

        [
            KeyboardButton(text="Bekor qilish")
        ],
    ],
    resize_keyboard=True
)

studentkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q"),
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ],
                
    ],
    resize_keyboard=True
)

salarykey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.5 mln - 2 mln"),
            KeyboardButton(text="2.5 mln - 3.5 mln")
        ],
        [
            KeyboardButton(text="4 mln - 5 mln"),
            KeyboardButton(text="5 mln - 6 mln"),
        ],

        [
            KeyboardButton(text="Bekor qilish")
        ],
                
    ],
    resize_keyboard=True
)

phonkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon nomer",request_contact=True),
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ],
          
    ],
    resize_keyboard=True
)


yuborishkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yuborish"),
            KeyboardButton(text="Rad etish")
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ],
          
    ],
    resize_keyboard=True
)