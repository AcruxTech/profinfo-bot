import logging

from aiogram import Dispatcher, types

from app.shared.constants import CHANNEL_USERNAME, GROUP_ID


logger = logging.getLogger(__name__)


async def call_check_subscription(call: types.CallbackQuery):
    member = await call.bot.get_chat_member(CHANNEL_USERNAME, call.from_user.id) 
    if member.status not in ['member', 'creator']: 
        logger.info(
            f'new user {call.from_user.id} unsuccessful attempt to restrict self'
        )
        await call.answer('Подпишитесь на канал, чтобы писать сообщения!')
        return

    logger.info(
        f'new user {call.from_user.id} successfully restricted self'
    )
    await call.answer('Ура! Теперь Вы можете писать сообщения!')
    await call.message.delete()
    await call.bot.restrict_chat_member(
        GROUP_ID,
        call.from_user.id,
        types.ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_invite_users=True
        )
    )
    await call.answer()


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(call_check_subscription, text='check_subscription')