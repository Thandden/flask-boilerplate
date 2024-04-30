import os
from typing import Any

from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)


class ImmutableConfig:
    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.__dict__:
            raise AttributeError("Env cannot be changed")
        super().__setattr__(key, value)


class Config(ImmutableConfig):
    def __init__(self) -> None:
        self.SECRET = os.environ.get("SECRET")
        self.DB_URI = os.environ.get("DB_URI")


settings = Config()
