import graphic

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 200,
}

coin_values = {
    "p": 0.01,
    "n": 0.05,
    "d": 0.1,
    "q": 0.25
}

password = "5975"

# Technician mode
def technician_mode():
    while True:
        your_password = input("Enter the technician password: ")
        if your_password == password:
            print("Your code is the correct code")
            print("Current coin inventory:")
            for coin, count in coin_values.items():
                print(f"{coin}: {count}")
            print("Current resource inventory:")
            for resource, amount in resources.items():
                print(f"{resource}: {amount}")
            question = input("Do you want to fill the missing inventory? (yes/no): ").casefold()
            if question[0] == "y":
                resources["water"] = 500
                resources["milk"] = 300
                resources["coffee"] = 200
                print("The tanks are full, see you again soon.")
            turn_off = input("Do you want to exit technician mode? yes or no?").casefold()
            if turn_off[0] == "y":
                print("Turning off...")
                exit()
        else:
            print("Invalid password. Try again.")
            break


# User mode
def Client_status():
    while True:
        choice = input("Choose a coffee - (l)atte, (e)espresso, (c)cappuccino, or (off) to turn off: ")

        if choice not in ["l", "e", "c"]:
            print("Invalid choice. Please select l, e, c, or off.")
        if choice == "off":
            print("Turning off...")
            break
        Choice_of_drink = {"l": "latte", "e": "espresso", "c": "cappuccino"}[choice]
        cost = menu[Choice_of_drink]["cost"]
        print(f"Cost of {Choice_of_drink}: ${cost}")

        while cost > 0:
            coin_input = input("Insert p for penny, n for nickel, d for dime, or q for quarter: ")
            if coin_input not in ["p", "n", "d", "q"]:
                print("Invalid coin. Please insert p, n, d, or q.")
                continue

            coin_value = {"p": 0.01, "n": 0.05, "d": 0.10, "q": 0.25}[coin_input]
            coin_values[coin_input] += 1
            cost -= coin_value

            if cost <= 0:
                change = abs(cost)
                print(f"Here is your change: ${change:.2f}")
                print(f"Enjoy your {Choice_of_drink}!")
                print(graphic.coffee)

                if choice == "l":
                    resources["water"] -= 200
                    resources["milk"] -= 150
                    resources["coffee"] -= 24
                elif choice == "c":
                    resources["water"] -= 250
                    resources["milk"] -= 100
                    resources["coffee"] -= 24
                elif choice == "e":
                    resources["water"] -= 50
                    resources["coffee"] -= 18
                break

            print(f"You have to pay: ${cost:.2f}")

            if resources["water"] < 50 or resources["milk"] < 30 or resources["coffee"] < 10:
                print("Resources depleted. Please call a technician.")
                break


while True:
    print(graphic.welcome)
    mode = input("Enter a mode (technician/user): ").casefold()
    if mode[0] == "t":
        technician_mode()
    elif mode[0] == "u":
        Client_status()
    else:
        print("Invalid mode. Please select technician or user.")
