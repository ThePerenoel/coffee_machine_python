from dataclasses import dataclass, field
from src.domain.command import Command
from src.domain.drink_type import DrinkType

@dataclass(frozen=True)
class DrinkCommand(Command):
    type: DrinkType
    __quantity: int
    __extraHot: bool = field(default=False)

    def translate(self) -> str:
        return self.type.value[0] + self.__determineExtraHot()  + self.__translateSuffix()
    
    def __determineExtraHot(self) -> str:
        if(self.__extraHot):
            return "h"
        return ""
    
    def __translateSuffix(self) -> str:
        if(self.__quantity == 0):
            return "::"
        return f":{str(self.__quantity)}:0"

    def calculateChange(self, money) -> float:
        return self.type.value[1] - money