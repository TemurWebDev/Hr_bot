from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


citykeyUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tashkent")
        ],
        [
            KeyboardButton(text="Cancellation")
        ],
        
    ],
    resize_keyboard=True
)


filialkeyUs = ReplyKeyboardMarkup(
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
            KeyboardButton(text="Cancellation")
        ],
        
    ],
    resize_keyboard=True
)

positionkeyUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Vendor"),
            KeyboardButton(text="cashier")
        ],
        
        [
            KeyboardButton(text="Guard"),
            KeyboardButton(text="Manager")
        ],
        
        [
            KeyboardButton(text="Cancellation")
        ],
    ],
    resize_keyboard=True
)

studentkeyUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yes"),
            KeyboardButton(text="No")
        ],
        
        [
            KeyboardButton(text="Cancellation")
        ],
    ],
    resize_keyboard=True
)

salarykeyUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.5 mln - 2 mln"),
            KeyboardButton(text="2.5 mln - 3.5 mln")
        ],
        [
            KeyboardButton(text="4 mln - 5 mln"),
            KeyboardButton(text="5 mln - 6 mln")
        ],

        [
            KeyboardButton(text="Cancellation")
        ],
                
    ],
    resize_keyboard=True
)

phonkeyUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Phone number",request_contact=True),
        ],

        [
            KeyboardButton(text="Cancellation")
        ],
          
    ],
    resize_keyboard=True
)


yuborishkeyUs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sending"),
            KeyboardButton(text="Refusal")
        ],
          
        [
            KeyboardButton(text="Cancellation")
        ],
    ],
    resize_keyboard=True
)