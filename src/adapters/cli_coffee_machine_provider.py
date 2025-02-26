from src.providers.coffee_machine_provider import CoffeeMachineProvider
class CliCoffeeMachineProvider(CoffeeMachineProvider):

    def send(self, command):
        drinkType = command[0]
        match drinkType:
            case "H":
                print("Here is your chocolate.")
            case "C":
                print("Here is your coffee.")
            case "O":
                print("Here is your orange juice.")
            case "T":
                print("Here is your tea.")
            case "M":
                print(command[2:])
            case _:
                print("An error occured.")

