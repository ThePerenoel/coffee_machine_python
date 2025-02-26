from abc import ABC, abstractmethod

class ReportPrinter(ABC):

    @abstractmethod
    def print(self, result: str):
        pass