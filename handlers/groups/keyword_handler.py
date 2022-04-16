from cgitb import text
from loader import dp
from filters import IsGroup
from keyboards.inline import btns

from aiogram import types
from aiogram.dispatcher.filters import Text
from time import sleep


@dp.message_handler(IsGroup(), Text(equals="ban", ignore_case=True))
@dp.message_handler(IsGroup(), Text(contains="banof", ignore_case=True))
@dp.message_handler(IsGroup(), commands=['ban', 'banof', 'kick', 'kickof', 'banofuz'])
async def ban_handler(message: types.Message):
    if message.reply_to_message:
        check = await message.chat.get_member(message.from_user.id)
        if check.status == 'creator' or check.status == 'administrator':
            await message.chat.kick(message.reply_to_message.from_user.id, until_date=None)
            await message.answer(f"<a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a> kick qilindi.")
            await message.delete()
        else:
            matn = f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a></b> guruhimiz azosi bo'lgan <b> <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a></b> foydalanuvchi ban qilmoqchi. \n\n<b>Rozimisiz?</b>\n\n<b>"
            await message.answer(matn, reply_markup=btns(message.from_user.id, message.reply_to_message.from_user.id))
    else:
        msg = message.answer("xabarga javob bering")
        await message.delete()
        await sleep(5)
        await msg.delete()
