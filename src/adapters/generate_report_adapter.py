from src.usecases.generate_report import GenerateReport

class GenerateReportAdapter(GenerateReport):

    def act(self):
        print("Here is your report:")
        return super().act()
