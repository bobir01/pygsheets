from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

freshman_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ICT Systems & Tools"),
            KeyboardButton(text="Linear Algebra")
        ],
        [
            KeyboardButton(text="Precalculus/Tutorial"),
            KeyboardButton(text="Precalculus")
        ],
        [
            KeyboardButton(text="Computer Programming"),
            KeyboardButton(text="English Reading-Prof.Uralova")
            
        ],
        [
            KeyboardButton(text="Eng. Writ.1-Prof.Abdullaeva"),
            KeyboardButton(text="Eng. Writ.1-Prof.Akhmedjanov")
        ]
    ],resize_keyboard=True
)