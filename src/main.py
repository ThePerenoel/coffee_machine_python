from src.adapters.send_command_adapter import SendCommandAdapter
from src.domain.drink_command import DrinkCommand
from src.domain.drink_type import DrinkType
from src.adapters.cli_report_printer import CliReportPrinter
from src.adapters.in_memory_coffee_machine_provider import InMemoryCoffeeMachineProvider
from src.adapters.in_memory_command_repository import InMemoryCommandRepository
from src.domain.client_input import ClientInput
from src.usecases.send_command_coffee_machine import SendCommandToCoffeeMachine
from src.usecases.generate_report import GenerateReport

def main():

    reportPrinter = CliReportPrinter()
    coffeeMachineProvider = InMemoryCoffeeMachineProvider()
    commandRepository = InMemoryCommandRepository()
    generateReport = GenerateReport(commandRepository, reportPrinter)
    sendCommandToCoffeeMachine = SendCommandAdapter(commandRepository, coffeeMachineProvider)

    print("Welcome to your coffee machine. Type the following command to use it :")
    print("- Type the name of your drink to order it (exemple: TEA)")
    print("- Type REPORT to get a full report of the coffee machine")
    print("- Type EXIT to exit the program")
    print("**********************************************************")
    print("Prices :")
    print("TEA - 0.40€")
    print("COFFEE - 0.60€")
    print("CHOCOLATE - 0.50€")
    print("ORANGE_JUICE - 0.60€")

    while True:
        choice = input("What can I do for you? ").strip().upper()
        
        if choice in {"TEA", "COFFEE", "CHOCOLATE", "ORANGE_JUICE"}:
            givenMoney = input("How much money do you have? ")
            sugars = input("How many sugars? ")
            sendCommandToCoffeeMachine.act(choice, givenMoney, sugars)
        elif choice == "REPORT":
            print("Here is your report:")
            generateReport.act()
        elif choice == "EXIT":
            print("Ok Bye!")
            break
        else:
            print("Sorry, I don't recognize that command. Please enter a valid command.")

if __name__ == "__main__":
    main()