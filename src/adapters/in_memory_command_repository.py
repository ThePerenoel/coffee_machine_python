from dataclasses import dataclass, field
from typing import List

from src.domain.drink_command import DrinkCommand
from src.repositories.command_repository import CommandRepository

@dataclass
class InMemoryCommandRepository(CommandRepository):
    _database:List[DrinkCommand] = field(default_factory=list)

    def save(self, drinkCommand):
        self._database.append(drinkCommand)
        return
    
    def getAll(self):
        return self._database

    def contains(self, drinkCommand) -> bool:
        return drinkCommand in self._database
