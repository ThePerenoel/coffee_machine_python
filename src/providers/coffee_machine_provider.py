from abc import ABC, abstractmethod


class CoffeeMachineProvider(ABC):

    @abstractmethod
    def send(self, command: str):
        pass