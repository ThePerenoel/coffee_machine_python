from dataclasses import dataclass, field
from src.domain.command import Command


@dataclass
class MessageCommand(Command):
    __message: str = field(default="")

    def translate(self) -> str:
        return f"M:{self.__message}"