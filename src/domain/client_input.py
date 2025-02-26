from dataclasses import dataclass

from src.domain.command import Command
from src.domain.drink_command import DrinkCommand
from src.domain.drink_type import DrinkType
from src.domain.message_command import MessageCommand


@dataclass(frozen=True)
class ClientInput:
    drinkCommand: DrinkCommand
    _money: float
    
    def validate(self) -> Command:
        missingMoney = self.drinkCommand.calculateChange(self._money)
        if(missingMoney > 0):
            return MessageCommand(f"Cannot make command. {missingMoney} euro missing.")
        return self.drinkCommand
        
    def translate(self) -> str:
        return self.drinkCommand.translate()