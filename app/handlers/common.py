import asyncio
import logging

from aiogram import Dispatcher, types

from app.utils.keyboards import get_welcome_keyboard
from app.utils.functions import get_welcome_text
from app.shared.constants import GROUP_ID, DELETE_AFTER, ADMIN_USERNAME
from app.shared.variables import is_enabled


logger = logging.getLogger(__name__)


async def switch_state(message: types.Message):
    global is_enabled
    is_enabled = not is_enabled
    logger.info(
        f'bot is {"enabled" if is_enabled else "disabled"}\t' + \
        f'change status from user {message.from_user.id}'
    )
    await message.answer(
        f'Бот сейчас: <b>{"включен" if is_enabled else "выключен"}</b>\n' + \
        f'Для <b>{"выключения" if is_enabled else "включения"}</b> отправьте команду еще раз',
        parse_mode='HTML'
    )


async def welcome_group(message: types.Message):
    if not is_enabled:
        logger.info(f"new user {message.from_user.id} but bot disabled now")
        return

    ans = await message.answer(
        get_welcome_text(message.from_user.first_name), 
        reply_markup=get_welcome_keyboard()
    )
    logger.info(
        f'new user {message.from_user.id} join group'
    )
    await message.bot.restrict_chat_member(
        GROUP_ID,
        message.from_user.id,
        types.ChatPermissions(can_send_messages=False)
    )
    await asyncio.sleep(DELETE_AFTER)
    try:
        await ans.delete()
    except:
        pass


def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(
        switch_state,
        lambda message: message.from_user.username == ADMIN_USERNAME,
        commands=['switch_state']
    )
    dp.register_message_handler(
        welcome_group,
        lambda message: message.chat.id == GROUP_ID,
        content_types=types.ContentTypes.NEW_CHAT_MEMBERS
    )