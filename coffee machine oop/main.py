from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# A coffee machine using an object-oriented programming method

def main():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while True:
        # Display the available menu items
        print("Welcome to the Coffee Machine!")
        options = menu.get_items()
        print(f"Menu: {options}")

        # Take user input for drink selection
        user_choice = input(
            "What would you like to order? (Type the drink name or 'off' to turn off the machine): ").lower()

        if user_choice == "off":
            # Turn off the machine
            print("Turning off the machine. Have a great day!")
            break

        drink = menu.find_drink(user_choice)

        if drink:
            # Check if there are sufficient resources for the selected drink
            if coffee_maker.is_resource_sufficient(drink):
                # Process payment
                if money_machine.make_payment(drink.cost):
                    # Make the coffee
                    coffee_maker.make_coffee(drink)
        else:
            print("Invalid choice. Please select a valid drink from the menu.")


if __name__ == "__main__":
    main()
