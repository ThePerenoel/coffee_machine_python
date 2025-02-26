from dataclasses import dataclass, field
from src.domain.command import Command
from src.domain.drink_type import DrinkType

@dataclass(frozen=True)
class DrinkCommand(Command):
    type: DrinkType
    _quantity: int
    _isExtraHot: bool = field(default=False)

    def translate(self) -> str:
        return self.type.getStringValue() + self._determineExtraHot()  + self._translateSuffix()
    
    def _determineExtraHot(self) -> str:
        return "h" if self._isExtraHot else ""
    
    def _translateSuffix(self) -> str:
        if(self._quantity == 0):
            return "::"
        return f":{str(self._quantity)}:0"

    def calculateMissingMoney(self, givenMoney) -> float:
        return self.type.calculateMissingMoney(givenMoney)