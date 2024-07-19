from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                          InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
    ],
                resize_keyboard=True,
                input_field_placeholder='Выберите пункт меню.')
setings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Youtube', url='https://www.youtube.com/')]
    ])

cars = ['BMW','Mercedes','Audi','Volkswagen','To']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://yandex.ru'))
    return keyboard.adjust(2).as_markup()
