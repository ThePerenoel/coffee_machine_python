import unittest
from parameterized import parameterized
from src.domain.drink_type import DrinkType

class TestDrinkType(unittest.TestCase):

    @parameterized.expand([
        [DrinkType.CHOCOLATE, 0.3, 0.2],
        [DrinkType.CHOCOLATE, 0.5, 0],
        [DrinkType.CHOCOLATE, 0.6, -0.1],
        [DrinkType.TEA, 0.1, 0.3],
        [DrinkType.TEA, 0.4, 0],
        [DrinkType.TEA, 0.5, -0.1],
        [DrinkType.COFFEE, 0.6, 0],
        [DrinkType.COFFEE, 0.4, 0.2],
        [DrinkType.COFFEE,  1, -0.4],
        [DrinkType.ORANGE, 0.6, 0],
        [DrinkType.ORANGE, 0.4, 0.2],
        [DrinkType.ORANGE,  1, -0.4],
    ])
    def test_calculate_change(self, drinkType: DrinkType, givenMoney: float, expectedMissingMoney: float):
        missingMoney = drinkType.calculateMissingMoney(givenMoney)
        self.assertEqual(missingMoney, expectedMissingMoney)
