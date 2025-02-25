import unittest
from src.domain.client_input import ClientInput
from src.domain.drink_command import DrinkCommand
from src.domain.message_command import MessageCommand
from src.usecases.send_command_coffee_machine import SendCommandToCoffeeMachine
from src.domain.drink_type import DrinkType
from tests.domain.in_memory_command_repository import InMemoryCommandRepository

class TestClientInput(unittest.TestCase):

    def test1(self):
        """
        GIVEN DrinkCommand for coffee with one sugar AND 0.6 euros
        THEN ClientInput should validate the command and return it
        """
        drinkCommand = DrinkCommand(DrinkType.COFFEE, 1)
        clientInput = ClientInput(drinkCommand, 0.6)
        order = clientInput.validate()
        expectedOrder = drinkCommand
        self.assertEqual(order, expectedOrder)

    def test2(self):
        """
        GIVEN DrinkCommand for coffee with one sugar AND 0.4 euros
        THEN ClientInput should return a MessageCommand with 0.2 euros missing
        """
        drinkCommand = DrinkCommand(DrinkType.COFFEE, 1)
        clientInput = ClientInput(drinkCommand, 0.4)
        order = clientInput.validate()
        expectedOrder = MessageCommand("Cannot make command. 0.2 euro missing.")
        self.assertEqual(order, expectedOrder)

    def test1(self):
        """
        GIVEN DrinkCommand for coffee with two sugars AND 1 euro
        THEN ClientInput should validate the command and return it
        """
        drinkCommand = DrinkCommand(DrinkType.COFFEE, 1)
        clientInput = ClientInput(drinkCommand, 1)
        order = clientInput.validate()
        expectedOrder = drinkCommand
        self.assertEqual(order, expectedOrder)

if __name__ == '__main__':
    unittest.main()
