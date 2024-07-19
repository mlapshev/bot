
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Меню',reply_markup=await kb.inline_cars())

@router.message(Command("get_id"))
async def get_id(message: Message):
    await message.reply(f"Привет!\nТвой ID: {message.from_user.id}\nТвой Ник: {message.from_user.first_name} "
                      f"{message.from_user.last_name}\nГруппа ID: {message.chat.id}\n")

@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Это команда /help")

@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("ок")

@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMuZppVMv27MC78HRyKNv4bOsWSnUsAAgLeMRtQR9FIWJXT06PqVCwBAAMCAANtAAM1BA",
                        caption="Это я")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')