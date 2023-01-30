from aiogram import types

from app.shared.constants import CHANNEL_USERNAME


def get_welcome_keyboard() -> types.InlineKeyboardMarkup:
    buttons = [
        types.InlineKeyboardButton(text='Шаг 1: подписаться на канал', url='https://t.me/' + CHANNEL_USERNAME[1:]),
        types.InlineKeyboardButton(text='Шаг 2: нажать эту кнопку', callback_data='check_subscription')
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(*buttons)
    return keyboard