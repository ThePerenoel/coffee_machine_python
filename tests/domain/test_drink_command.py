import unittest
from parameterized import parameterized
from src.domain.command import Command
from src.domain.drink_command import DrinkCommand
from src.domain.drink_type import DrinkType

class TestCommand(unittest.TestCase):

    @parameterized.expand([
        [DrinkCommand(DrinkType.CHOCOLATE, 0), "H::",],
        [DrinkCommand(DrinkType.CHOCOLATE, 9), "H:9:0"],
        [DrinkCommand(DrinkType.CHOCOLATE, 10), "H:10:0"],
        [DrinkCommand(DrinkType.TEA, 0), "T::"],
        [DrinkCommand(DrinkType.TEA, 1), "T:1:0"],
        [DrinkCommand(DrinkType.TEA, 3), "T:3:0"],
        [DrinkCommand(DrinkType.COFFEE, 0), "C::"],
        [DrinkCommand(DrinkType.COFFEE, 2), "C:2:0"],
        [DrinkCommand(DrinkType.COFFEE, 4),  "C:4:0"],
        [DrinkCommand(DrinkType.ORANGE, 0),  "O::"],
        [DrinkCommand(DrinkType.COFFEE, 0, True),  "Ch::"],
        [DrinkCommand(DrinkType.CHOCOLATE, 1, True),  "Hh:1:0"],
        [DrinkCommand(DrinkType.TEA, 2, True),  "Th:2:0"],
    ])
    def test_translation(self, drinkCommand: DrinkCommand, expectedTranslation: str):
        translation = drinkCommand.translate()
        self.assertEqual(translation, expectedTranslation)

    
if __name__ == '__main__':
    unittest.main()
