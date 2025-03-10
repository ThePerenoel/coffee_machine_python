from enum import Enum

class DrinkType(Enum):
    CHOCOLATE = "H", 0.5
    TEA = "T", 0.4
    COFFEE = "C", 0.6
    ORANGE = "O", 0.6

    def getStringValue(self) -> str:
        return self.value[0]

    def calculateMissingMoney(self, givenMoney: float) -> float:
        return round(self.value[1] - givenMoney, 2)
    