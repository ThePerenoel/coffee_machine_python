import unittest
from src.domain.client_input import ClientInput
from src.domain.drink_command import DrinkCommand
from src.domain.message_command import MessageCommand
from src.usecases.send_command_coffee_machine import SendCommandToCoffeeMachine
from src.domain.drink_type import DrinkType
from tests.in_memory.in_memory_coffee_machine_provider import InMemoryCoffeeMachineProvider
from tests.in_memory.in_memory_command_repository import InMemoryCommandRepository

class TestDrinkMaker(unittest.TestCase):

    def test1(self):
        """
        GIVEN ClientInput with DrinkCommand for coffee with one sugar AND 0.6 euros
        THEN SendCommandToCoffeeMachine should save the command and send the translation to coffeeMachine
        """
        commandRepository = InMemoryCommandRepository()
        coffeeMachineProvider = InMemoryCoffeeMachineProvider()
        drinkCommand = DrinkCommand(DrinkType.COFFEE, 1)
        clientInput = ClientInput(drinkCommand, 0.6)
        sendCommandToCoffeeMachine = SendCommandToCoffeeMachine(commandRepository, coffeeMachineProvider)
        sendCommandToCoffeeMachine.act(clientInput)
        self.assertTrue(commandRepository.contains(drinkCommand))
        self.assertTrue(coffeeMachineProvider.hasSent("C:1:0"))

    def test2(self):
        """
        GIVEN ClientInput with DrinkCommand for coffee with one sugar AND 0.5 euros
        THEN SendCommandToCoffeeMachine should not save the command and send an error message
        """
        commandRepository = InMemoryCommandRepository()
        coffeeMachineProvider = InMemoryCoffeeMachineProvider()
        drinkCommand = DrinkCommand(DrinkType.COFFEE, 1)
        clientInput = ClientInput(drinkCommand, 0.5)
        sendCommandToCoffeeMachine = SendCommandToCoffeeMachine(commandRepository, coffeeMachineProvider)
        sendCommandToCoffeeMachine.act(clientInput)
        self.assertFalse(commandRepository.contains(drinkCommand))
        self.assertTrue(coffeeMachineProvider.hasSent("M:Cannot make command. 0.1 euro missing."))


if __name__ == '__main__':
    unittest.main()
