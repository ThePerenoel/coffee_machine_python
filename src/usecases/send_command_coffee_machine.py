from dataclasses import dataclass

from src.domain.client_input import ClientInput
from src.providers.coffee_machine_provider import CoffeeMachineProvider
from src.domain.command import Command
from src.repositories.command_repository import CommandRepository
from src.domain.drink_command import DrinkCommand
from src.domain.drink_type import DrinkType
from src.domain.message_command import MessageCommand


@dataclass(frozen=True)
class SendCommandToCoffeeMachine:
    _commandRepository: CommandRepository
    _coffeeMachineProvider: CoffeeMachineProvider
    
    def act(self, clientInput: ClientInput):
        command = clientInput.validate()
        self._saveCommand(command)
        self._coffeeMachineProvider.send(command.translate())
    
    def _saveCommand(self, command: Command):
        if(type(command) is DrinkCommand):
            self._commandRepository.save(command)
