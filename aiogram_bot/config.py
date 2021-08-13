from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class AiogramBot:
    token: str
    admin_id: int


def load_config(path: str) -> AiogramBot:
    config = ConfigParser()
    config.read(path)

    return AiogramBot(
        **config['aiogram_bot']
    )
