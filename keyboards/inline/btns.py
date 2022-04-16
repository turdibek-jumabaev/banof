from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def btns(a, b):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➕", callback_data=f"{a}_{b}"),
                InlineKeyboardButton(text="➖", callback_data=f"{b}_{a}"),
            ]
        ]
    )
    return markup
