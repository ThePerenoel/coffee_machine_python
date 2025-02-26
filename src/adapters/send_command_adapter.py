from dataclasses import dataclass
from src.domain.client_input import ClientInput
from src.domain.drink_command import DrinkCommand
from src.domain.drink_type import DrinkType
from src.usecases.send_command_coffee_machine import SendCommandToCoffeeMachine

class SendCommandAdapter(SendCommandToCoffeeMachine):

    def act(self, choice: str, givenMoney: str, sugars: str):
        drinkType = DrinkType.ORANGE if(choice == "ORANGE_JUICE") else DrinkType[choice]
        drinkCommand = DrinkCommand(drinkType, int(sugars))
        clientInput = ClientInput(drinkCommand, float(givenMoney))
        return super().act(clientInput)
