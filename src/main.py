from src.adapters.generate_report_adapter import GenerateReportAdapter
from src.adapters.send_command_adapter import SendCommandAdapter
from src.adapters.cli_report_printer import CliReportPrinter
from src.adapters.cli_coffee_machine_provider import CliCoffeeMachineProvider
from src.adapters.in_memory_command_repository import InMemoryCommandRepository

def main():

    reportPrinter = CliReportPrinter()
    coffeeMachineProvider = CliCoffeeMachineProvider()
    commandRepository = InMemoryCommandRepository()
    generateReport = GenerateReportAdapter(commandRepository, reportPrinter)
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
    print("**********************************************************")

    while True:
        choice = input("What can I do for you? > ").strip().upper()
        if choice in {"TEA", "COFFEE", "CHOCOLATE", "ORANGE_JUICE"}:
            sendCommandToCoffeeMachine.act(choice)
        elif choice == "REPORT":
            generateReport.act()
        elif choice == "EXIT":
            print("Ok Bye!")
            break
        else:
            print("Sorry, I don't recognize that command. Please enter a valid command.")

if __name__ == "__main__":
    main()