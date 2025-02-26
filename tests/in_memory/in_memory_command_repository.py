from dataclasses import dataclass, field
from typing import List
from src.repositories.command_repository import CommandRepository
from src.domain.drink_command import DrinkCommand

@dataclass
class InMemoryCommandRepository(CommandRepository):
    __database:List[DrinkCommand] = field(default_factory=list)

    def save(self, drinkCommand):
        self.__database.append(drinkCommand)
        return
    
    def getAll(self):
        return self.__database

    def contains(self, drinkCommand) -> bool:
        return drinkCommand in self.__database