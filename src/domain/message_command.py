from dataclasses import dataclass, field
from src.domain.command import Command


@dataclass
class MessageCommand(Command):
    _message: str = field(default="")

    def translate(self) -> str:
        return f"M:{self._message}"