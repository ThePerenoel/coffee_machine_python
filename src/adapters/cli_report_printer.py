from dataclasses import dataclass
from src.providers.report_printer import ReportPrinter

@dataclass
class CliReportPrinter(ReportPrinter):

    def print(self, result):
        print(result)
