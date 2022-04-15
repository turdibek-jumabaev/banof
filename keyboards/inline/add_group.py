from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

addGroup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕", url="https://t.me/banofuzbot?startgroup=new")
        ]
    ]
)
