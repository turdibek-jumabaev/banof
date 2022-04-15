from loader import dp

from aiogram import types
from time import sleep


@dp.message_handler(commands=['ban', 'banof', 'kick', 'kickof', 'banofuz'])
async def ban_handler(message: types.Message):
    if message.reply_to_message:
        matn = f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a></b> guruhimiz azosi bo'lgan <b> <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a></b> foydalanuvchi ban qilmoqchi. \n\n<b>Rozimisiz?</b>\n\n<b>"
        await message.answer(matn)
    else:
        msg = message.answer("xabarga javob bering")
        await message.delete()
        await sleep(5)
        await msg.delete()
