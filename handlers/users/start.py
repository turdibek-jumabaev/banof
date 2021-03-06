from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline import addGroup
from filters import IsPrivate


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Banof ishlashi uchun guruhga qo'shing.", reply_markup=addGroup)
