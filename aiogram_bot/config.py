from configparser import ConfigParser
from dataclasses import dataclass
from typing import Union


@dataclass
class AiogramBot:
    token: str
    admins_id: Union[list, int]


def load_config(path: str) -> AiogramBot:
    config = ConfigParser()
    config.read(path)

    return AiogramBot(
        **config['aiogram_bot']
    )
