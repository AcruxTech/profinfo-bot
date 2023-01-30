import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config.config import load_config 
from app.handlers.common import register_common_handlers
from app.handlers.callbacks import register_callback_handlers


logger = logging.getLogger(__name__)


async def main():
    # Удаляем старые логи, если они есть
    if(os.path.isfile('profinfo.log')):
        os.remove('profinfo.log')

    # Настройка логирования в stdout
    logging.basicConfig(
        filename="profinfo.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=load_config().tg_bot.token)
    print((await bot.get_me()).username)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Регистрация хэндлеров
    register_common_handlers(dp)   
    register_callback_handlers(dp)  

    # Запуск поллинга                    
    await dp.start_polling(allowed_updates=['message', 'callback_query'])                    


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass