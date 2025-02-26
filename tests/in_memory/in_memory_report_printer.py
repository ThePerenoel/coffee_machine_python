from dataclasses import dataclass, field
from typing import List

from src.providers.report_printer import ReportPrinter


@dataclass
class InMemoryReportPrinter(ReportPrinter):

    history: List[str] = field(default_factory = list)

    def print(self, result):
        self.history.append(result)

    def contains(self, printedReport: str):
        return printedReport in self.history