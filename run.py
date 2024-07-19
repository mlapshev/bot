import asyncio
import logging

from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Наша команда делает все удобно для тебя")


@dp.message(Command("get_id"))
async def get_id(message: Message):
    await message.reply(f"Привет!\nТвой ID: {message.from_user.id}\nТвой Ник: {message.from_user.first_name} "
                      f"{message.from_user.last_name}\nГруппа ID: {message.chat.id}\n")

@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer("Это команда /help")

@dp.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("ок")

@dp.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMuZppVMv27MC78HRyKNv4bOsWSnUsAAgLeMRtQR9FIWJXT06PqVCwBAAMCAANtAAM1BA",
                        caption="Это я")

@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


async  def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  #логирование в консоль
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')