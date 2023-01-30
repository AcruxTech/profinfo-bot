import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from app.utils.keyboards import get_welcome_keyboard
from app.utils.functions import get_welcome_text
from app.shared.constants import GROUP_ID, DELETE_AFTER


async def welcome_group(message: types.Message, state: FSMContext):
    ans = await message.answer(
        get_welcome_text(message.from_user.first_name), 
        reply_markup=get_welcome_keyboard()
    )
    await message.bot.restrict_chat_member(
        GROUP_ID,
        message.from_user.id,
        types.ChatPermissions(can_send_messages=False)
    )
    await asyncio.sleep(DELETE_AFTER)
    await ans.delete()


def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(
        welcome_group,
        lambda message: message.chat.id == GROUP_ID,
        content_types=types.ContentTypes.NEW_CHAT_MEMBERS
    )