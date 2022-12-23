import asyncio
from random import randint
from pyrogram import Client, filters, types
from pyrogram.errors import FloodWait

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.me & filters.command("spam", prefixes="!"))
async def spam(client, message: types.Message):
    command_text: str = message.text.split("!spam", maxsplit=1)[1].strip()
    await message.delete()
    if not command_text:
        m = await message.reply("Example: !spam 10 Text to spam")
        await asyncio.sleep(10)
        await m.delete()
    else:
        try:
            repeats = command_text.split()[0]
            text_to_spam = command_text.replace(repeats, "").strip()
            repeats = int(repeats)
            for _ in range(repeats):
                try:
                    await message.reply(text_to_spam)
                    await asyncio.sleep(0.2)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
        except (ValueError, IndexError):
            m = await message.reply("Example: !spam 10 Text to spam")
            await asyncio.sleep(10)
            await m.delete()


@app.on_message(filters.me & filters.command("type", prefixes="!"))
async def typing(client, message: types.Message):
    # sourcery skip: use-assigned-variable
    orig_text: str = message.text.split("!type", maxsplit=1)[1].strip()
    text = orig_text
    to_be_printed = ""
    typing_symbol = "|"
    while to_be_printed != orig_text:
        try:
            await message.edit(to_be_printed + typing_symbol)
            await asyncio.sleep(0.5)

            to_be_printed += text[0]
            text = text[1:]

            await message.edit(to_be_printed)
            await asyncio.sleep(0.5)

        except FloodWait as e:
            await asyncio.sleep(e.x)


@app.on_message(filters.me & filters.command("hack_pentagon", prefixes="!"))
async def hack_pentagon(client, message: types.Message):
    perc = 0
    while perc < 100:
        try:
            text = f"👮🏽‍♂️ Взлом Пентагона... {perc}%"
            await message.edit(text)
            perc += randint(1, 3)
            await asyncio.sleep(0.3)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    await message.edit("👮🏽‍♂️ Взлом произведён успешно...")
    await asyncio.sleep(2)
    await message.edit("👮🏽‍♂️ Поиск секретных данных...")
    await asyncio.sleep(2)
    await message.edit("👮🏽‍♂️ Найдены данные об НЛО 🛸")


@app.on_message(filters.me & filters.command("hack_user", prefixes="!"))
async def hack_user(client, message: types.Message):
    user = message.chat
    perc = 0
    while perc < 100:
        try:
            text = (f"🕵️ Получение данных об пользователе {user.first_name} "
                    f"{user.last_name}... {perc}%")
            await message.edit(text)
            perc += randint(1, 3)
            await asyncio.sleep(0.3)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    await message.edit("🕵️ Данные получены успешно...")
    await asyncio.sleep(2)
    await message.edit("🕵️ Получение криптографического ключа шифрофки "
                       "данных telegram...")
    await asyncio.sleep(2)
    await message.edit("🕵️ Расшифровка данных...")
    await asyncio.sleep(2)
    await message.edit("🕵️ Данные пользователя:\n"
                       f"Username: {user.username}\n"
                       f"Уникальный ключ пользователя: {user.id}\n"
                       f"Имя пользователя: {user.first_name}\n"
                       f"Фамилия пользователя: {user.last_name}\n\n"
                       "*None - значение отсутствует")

app.run()
