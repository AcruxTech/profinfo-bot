import os
import dotenv

from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config():
    dotenv.load_dotenv()

    return Config(
        tg_bot=TgBot(
            token=os.getenv('BOT_TOKEN')
        )
    )
