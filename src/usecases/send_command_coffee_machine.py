from dataclasses import dataclass

from src.domain.client_input import ClientInput
from src.domain.coffee_machine_provider import CoffeeMachineProvider
from src.domain.command_repository import CommandRepository
from src.domain.drink_command import DrinkCommand
from src.domain.drink_type import DrinkType
from src.domain.message_command import MessageCommand


@dataclass(frozen=True)
class SendCommandToCoffeeMachine:
    commandRepository: CommandRepository
    coffeeMachineProvider: CoffeeMachineProvider
    
    def act(self, clientInput: ClientInput):
        command = clientInput.validate()
        if(type(command) is DrinkCommand):
            self.commandRepository.save(command)
        self.coffeeMachineProvider.send(command.translate())