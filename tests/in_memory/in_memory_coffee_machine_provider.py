from dataclasses import dataclass, field
from typing import List
from src.providers.coffee_machine_provider import CoffeeMachineProvider

@dataclass
class InMemoryCoffeeMachineProvider(CoffeeMachineProvider):

    _commandHistory: List[str] = field(default_factory=list)

    def send(self, command: str):
        self._commandHistory.append(command)
    
    def hasSent(self, command: str):
        return command in self._commandHistory
    
    def isEmpty(self):
        return not self._commandHistory