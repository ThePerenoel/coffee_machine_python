from abc import ABC, abstractmethod
from typing import List
from src.domain.drink_command import DrinkCommand

class CommandRepository(ABC):

    @abstractmethod
    def save(self, drinkCommand: DrinkCommand):
        pass

    @abstractmethod
    def getAll(self) -> List[DrinkCommand]:
        pass