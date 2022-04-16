import io

from loader import dp, bot
from filters.is_group import IsGroup
from filters.admins import AdminFilter

from aiogram.types import Message, InputFile
from aiogram.dispatcher.filters import Command


# change gruop name
@dp.message_handler(IsGroup(), Command('set_title', prefixes='!/'), AdminFilter())
async def set_new_title(message: Message):
    source_message = message.reply_to_message
    title = source_message.text
    await bot.set_chat_title(message.chat.id, title=title)


# change group photo
@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = InputFile(photo)
    await message.chat.set_photo(photo=input_file)


# change group description
@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: Message):
    source_message = message.reply_to_message
    description = source_message.text
    await message.chat.set_description(description=description)
