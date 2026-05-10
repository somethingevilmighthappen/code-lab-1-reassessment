# ==============================
# Vending Machine Program
# ==============================

money = 10.00  # Starting balance

# Item database/dictionary
vending_machine = {
    "0A": {"item": "Chips", "price": 2.00},
    "0B": {"item": "Soda", "price": 1.00},
    "0C": {"item": "Chocolate", "price": 1.50},
    "0D": {"item": "Fruit Snacks", "price": 0.25}
}


def display_items():
    """Display all vending machine items."""
    print("\n===== VENDING MACHINE =====")

    for code, info in vending_machine.items():
        print(f"{code} | {info['item']} - AED {info['price']:.2f}")

    print("===========================\n")


def purchase(code):
    """Handle item purchases."""
    global money

    if code not in vending_machine:
        print("Invalid selection.")
        return

    item = vending_machine[code]["item"]
    price = vending_machine[code]["price"]

    if money >= price:
        money -= price
        print(f"You purchased {item} for AED {price:.2f}")
        print(f"Remaining balance: AED {money:.2f}")
    else:
        print("Insufficient funds.")


def main():
    """Main vending machine loop."""

    print("Welcome to the Vending Machine Program!")

    while True:
        display_items()

        print(f"Current balance: AED {money:.2f}")

        user_input = input(
            "Enter item code (or type 'exit' to quit): "
        ).upper()

        if user_input == "EXIT":
            break

        purchase(user_input)

        print()

    print(f"\nThank you for using the vending machine!")
    print(f"Your remaining balance is AED {money:.2f}")


# Run program
main()