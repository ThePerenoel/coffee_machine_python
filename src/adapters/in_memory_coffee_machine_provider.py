from dataclasses import dataclass, field
from typing import List
from src.providers.coffee_machine_provider import CoffeeMachineProvider

@dataclass
class InMemoryCoffeeMachineProvider(CoffeeMachineProvider):

    _database:List[str] = field(default_factory=list)

    def send(self, command):
        print(command)
        self._database.append(command)
