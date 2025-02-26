from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from src.domain.drink_type import DrinkType

class Command(ABC):

    @abstractmethod
    def translate(self) -> str:
        """Translate the command to a string representation"""
        pass
