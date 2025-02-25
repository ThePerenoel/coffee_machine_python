import unittest

from src.domain.drink_command import DrinkCommand
from src.domain.drink_type import DrinkType
from src.usecases.generate_report import GenerateReport
from tests.domain.in_memory_command_repository import InMemoryCommandRepository
from tests.domain.in_memory_report_printer import InMemoryReportPrinter

class TestGenerateReport(unittest.TestCase):

    def test1(self):
        commands = [
            DrinkCommand(DrinkType.COFFEE, 1),
            DrinkCommand(DrinkType.TEA, 1),
            DrinkCommand(DrinkType.CHOCOLATE, 4),
            DrinkCommand(DrinkType.COFFEE, 1),
            DrinkCommand(DrinkType.ORANGE, 0),
            DrinkCommand(DrinkType.COFFEE, 0),
            DrinkCommand(DrinkType.TEA, 3),
        ]
        commandRepository = InMemoryCommandRepository()
        reportPrinter = InMemoryReportPrinter()
        generateReport = GenerateReport(commandRepository, reportPrinter)
        for command in commands:
            commandRepository.save(command) 
        exepectedPrint = "[CHOCOLATE: 1, TEA: 2, COFFEE: 3, ORANGE: 1]"

        generateReport.act()
        self.assertTrue(reportPrinter.contains(exepectedPrint))

    def test2(self):
        commands = [
            DrinkCommand(DrinkType.COFFEE, 1),
            DrinkCommand(DrinkType.COFFEE, 1),
            DrinkCommand(DrinkType.CHOCOLATE, 4),
            DrinkCommand(DrinkType.COFFEE, 1),
            DrinkCommand(DrinkType.COFFEE, 0),
            DrinkCommand(DrinkType.COFFEE, 0),
            DrinkCommand(DrinkType.TEA, 3),
        ]
        commandRepository = InMemoryCommandRepository()
        reportPrinter = InMemoryReportPrinter()
        generateReport = GenerateReport(commandRepository, reportPrinter)
        for command in commands:
            commandRepository.save(command) 
        exepectedPrint = "[CHOCOLATE: 1, TEA: 1, COFFEE: 5, ORANGE: 0]"

        generateReport.act()
        self.assertTrue(reportPrinter.contains(exepectedPrint))
