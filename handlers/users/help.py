from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Buyruqlar:</b> ",
            "/start - Botni qayta ishga tushirish",
            "",
            "Botdan foydalanish uchun guruhga admin qiling va quyidagi kalit so'rlardan foydalaning:",
            "<i>+ banof</i>",
            "<i>+ banofuz</i>",
            "<i>+ ban</i>",)

    await message.answer("\n".join(text))
