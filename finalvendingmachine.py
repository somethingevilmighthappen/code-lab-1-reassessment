"""
Vending Machine Program - Utility App Assessment
Module: CODELAB I

This is my vending machine program for the assignment.
It lets users buy drinks and snacks, handles money and change,
and has some extra features like categories, stock tracking,
and suggestions.

The user has a wallet that holds their money.
They insert money from their wallet into the machine.
Change gets returned to their wallet.
"""

# ==============================
# VENDING MACHINE DATA
# ==============================

# I organised items by category to make it nicer for users
# Each item has a code, name, price, category, and stock count

vending_machine = {
    # Cold drinks
    "A1": {"name": "Coca Cola", "price": 1.50, "category": "Drinks", "stock": 5},
    "A2": {"name": "Sprite", "price": 1.50, "category": "Drinks", "stock": 3},
    "A3": {"name": "Water", "price": 1.00, "category": "Drinks", "stock": 8},
    "A4": {"name": "Orange Juice", "price": 2.00, "category": "Drinks", "stock": 4},
    
    # Snacks
    "B1": {"name": "Potato Chips", "price": 1.25, "category": "Snacks", "stock": 6},
    "B2": {"name": "Pretzels", "price": 1.00, "category": "Snacks", "stock": 0},  # sold out
    "B3": {"name": "Popcorn", "price": 1.50, "category": "Snacks", "stock": 4},
    
    # Chocolate bars
    "C1": {"name": "Snickers", "price": 1.25, "category": "Chocolate", "stock": 7},
    "C2": {"name": "KitKat", "price": 1.25, "category": "Chocolate", "stock": 5},
    "C3": {"name": "M&Ms", "price": 1.50, "category": "Chocolate", "stock": 3},
    
    # Hot drinks
    "D1": {"name": "Black Coffee", "price": 1.75, "category": "Hot Drinks", "stock": 4},
    "D2": {"name": "Hot Chocolate", "price": 1.75, "category": "Hot Drinks", "stock": 2},
}

# These are for the suggestion feature
# If you buy something, the machine recommends something that goes well with it
suggestions = {
    "Coca Cola": "Pretzels",
    "Black Coffee": "KitKat",
    "Hot Chocolate": "M&Ms",
    "Potato Chips": "Sprite",
}


# ==============================
# HELPER FUNCTIONS
# ==============================

def show_menu():
    """Displays all items with categories."""
    print("\n" + "=" * 50)
    print("           VENDING MACHINE MENU")
    print("=" * 50)
    
    # Group by category to make it easier to read
    categories = ["Drinks", "Snacks", "Chocolate", "Hot Drinks"]
    
    for category in categories:
        print(f"\n--- {category} ---")
        for code, item in vending_machine.items():
            if item["category"] == category:
                if item["stock"] > 0:
                    stock_text = f"[{item['stock']} left]"
                else:
                    stock_text = "[OUT OF STOCK]"
                print(f"  {code}: {item['name']:15} AED {item['price']:.2f}  {stock_text}")
    
    print("\n" + "=" * 50)


def show_wallet(wallet):
    """Shows how much money the user has in their wallet."""
    print(f"Your wallet balance: AED {wallet:.2f}")


def insert_money(wallet):
    """
    User puts money into the vending machine from their wallet.
    Money comes out of wallet and goes into the machine.
    Returns the new wallet balance and how much was inserted.
    """
    print(f"\nYour wallet has AED {wallet:.2f}")
    
    while True:
        try:
            amount = float(input("How much to insert into the machine? AED "))
            
            if amount <= 0:
                print("You need to insert some money.")
                continue
                
            if amount > wallet:
                print(f"You only have AED {wallet:.2f} in your wallet. Try a smaller amount.")
                continue
                
            if amount > 20:
                print("Machine only accepts AED 20 max at a time.")
                continue
                
            # Take money from wallet
            new_wallet = wallet - amount
            print(f"Inserted AED {amount:.2f} into the machine")
            print(f"Remaining in wallet: AED {new_wallet:.2f}")
            
            return new_wallet, amount
            
        except ValueError:
            print("Please enter a valid number like 5.00")


def dispense_item(code, inserted_amount, cost):
    """
    Dispenses the item and returns change.
    Updates stock levels.
    """
    item = vending_machine[code]
    change = round(inserted_amount - cost, 2)
    
    # Reduce stock by one
    vending_machine[code]["stock"] -= 1
    
    # Dispense message required by brief
    print(f"\n[DISPENSING]")
    print(f"   {item['name']} has been dispensed.")
    print(f"   Cost: AED {cost:.2f}")
    print(f"   You inserted: AED {inserted_amount:.2f}")
    
    # Change message required by brief
    if change > 0:
        print(f"   Change returned: AED {change:.2f}")
    else:
        print(f"   Exact change. No change returned.")
    
    return change


def check_stock(code):
    """Checks if item exists and has stock."""
    if code not in vending_machine:
        return False, "That code is not valid. Check the menu."
    
    if vending_machine[code]["stock"] <= 0:
        return False, f"Sorry, {vending_machine[code]['name']} is sold out."
    
    return True, "Available"


def make_suggestion(bought_item, wallet, items):
    """
    Suggests a complementary item based on what the user bought.
    This was an advanced feature I added for higher marks.
    """
    if bought_item in suggestions:
        suggested = suggestions[bought_item]
        for code, item in items.items():
            if item["name"] == suggested and item["stock"] > 0:
                print(f"\nSuggestion: Since you bought {bought_item},")
                print(f"   would you like to add {suggested}? Only AED {item['price']:.2f}")
                print(f"   Enter code: {code}")
                return True
    return False


def ask_continue():
    """Asks if user wants to buy another item."""
    while True:
        answer = input("\nBuy another item? (yes/no): ").lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please type yes or no.")


def return_change_to_wallet(wallet, change):
    """Change from the machine goes back into the user's wallet."""
    new_wallet = wallet + change
    print(f"Change added to your wallet. Wallet now has: AED {new_wallet:.2f}")
    return new_wallet


# ==============================
# MAIN PROGRAM
# ==============================

def run_vending_machine():
    """
    Main loop that runs the vending machine.
    User starts with money in their wallet.
    They insert money from wallet -> machine takes it
    Machine returns change -> change goes back to wallet
    """
    print("\n" + "=" * 50)
    print("   WELCOME TO THE VENDING MACHINE")
    print("=" * 50)
    
    # User starts with money in their wallet/purse
    user_wallet = 20.00
    
    total_spent = 0.0
    items_bought = 0
    last_item = None
    
    print(f"\nYou start with AED {user_wallet:.2f} in your wallet.")
    
    while True:
        # Show menu
        show_menu()
        
        # Show user their wallet balance
        show_wallet(user_wallet)
        
        # Check if user has any money left
        if user_wallet <= 0:
            print("\nYour wallet is empty. You cannot buy anything else.")
            print("Thank you for shopping.")
            break
        
        # Get user's choice
        code = input("\nEnter item code (or type 'exit' to quit): ").upper()
        
        if code == "EXIT":
            break
        
        # Validate code
        if code not in vending_machine:
            print(f"'{code}' is not a valid code. Look at the menu and try again.")
            continue
        
        # Check stock
        available, message = check_stock(code)
        if not available:
            print(f"{message}")
            continue
        
        item = vending_machine[code]
        price = item["price"]
        
        print(f"\nYou selected: {item['name']} - AED {price:.2f}")
        
        # User inserts money from their wallet into the machine
        user_wallet, inserted_amount = insert_money(user_wallet)
        
        # Check if enough money was inserted
        if inserted_amount < price:
            print(f"\nNot enough money inserted.")
            print(f"   {item['name']} costs AED {price:.2f}")
            print(f"   You only inserted AED {inserted_amount:.2f}")
            print(f"   Returning AED {inserted_amount:.2f} to your wallet...")
            user_wallet = return_change_to_wallet(user_wallet, inserted_amount)
            continue
        
        # Dispense the item
        change_from_machine = dispense_item(code, inserted_amount, price)
        
        # Change goes back to user's wallet
        if change_from_machine > 0:
            user_wallet = return_change_to_wallet(user_wallet, change_from_machine)
        
        # Calculate actual money spent
        actual_cost = inserted_amount - change_from_machine
        total_spent = total_spent + actual_cost
        items_bought += 1
        last_item = item["name"]
        
        # Show updated wallet
        print(f"\nAfter this purchase:")
        print(f"   Spent: AED {actual_cost:.2f}")
        print(f"   Wallet now has: AED {user_wallet:.2f}")
        
        # Smart suggestion feature
        make_suggestion(last_item, user_wallet, vending_machine)
        
        # Ask if they want to continue shopping
        if not ask_continue():
            break
        
        print("\n--- Continuing shopping ---")
        print(f"Your wallet still has AED {user_wallet:.2f}")
    
    # Goodbye message with summary
    print("\n" + "=" * 50)
    print("   THANK YOU FOR USING THE VENDING MACHINE")
    print("=" * 50)
    print(f"Purchase summary:")
    print(f"   Items bought: {items_bought}")
    print(f"   Total spent: AED {total_spent:.2f}")
    print(f"   Money left in wallet: AED {user_wallet:.2f}")
    
    if last_item:
        print(f"   Last item purchased: {last_item}")
    
    print("\n   See you next time")
    print("=" * 50)


# ==============================
# RUN THE PROGRAM
# ==============================

if __name__ == "__main__":
    run_vending_machine()
