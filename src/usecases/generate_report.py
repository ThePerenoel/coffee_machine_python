from dataclasses import dataclass
from functools import reduce
from typing import List, Type
from src.domain.command_repository import CommandRepository
from src.domain.drink_type import DrinkType
from src.domain.report_printer import ReportPrinter

@dataclass(frozen=True)
class GenerateReport:
    _commandRepository: CommandRepository
    _reportPrinter: ReportPrinter

    def act(self):
        drinkCommands = self._commandRepository.getAll()
        drinkTypes = [drinkCommand.type for drinkCommand in drinkCommands]
        output = "[" + self._formatDrinkReport(drinkTypes) + "]"
        self._reportPrinter.print(output)

    def _formatDrinkReport(self, drinkTypes: List[DrinkType]):
        return ", ".join(f"{data.name}: {drinkTypes.count(data)}" for data in DrinkType)