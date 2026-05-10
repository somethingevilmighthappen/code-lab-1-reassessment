# vending machine data

items = {
    # Chips - 4 AED
    11:("Cheetoes", 4), 12: ("Doritos", 4), 13: ("Lays", 4),

    # Candy - 2 AED
    21: ("Snickers", 2), 22: ("Skittles", 2),

    # Soda - 3 AED
    31: ("Coca-Cola", 3), 32: ("Pepsi", 3), 33: ("Sprite", 3),

    # Juice - 2 AED
    41: ("Orange Juice", 2), 42: ("Apple Juice", 2), 43: ("almost juice", 2)
}


# Display menu

def show_menu():
  print("\n============ Vending Machine Menu ============\n")


  print("Chips - 4 AED")
  for code in range(11, 21):
    print(f"{code} - {items[code][0]}")

    print("\nCandy - 2 AED")
    for code in range(21, 31):
      print(f"{code} - {items[code][0]}")

      print("\nSoda - 3 AED")
      for code in range(31, 41):
        print(f"{code} - {items[code][0]}")

        print("\nJuice - 2 AED")
        for code in range(41, 44):
          print(f"{code} - {items[code][0]}")

def process_purchase():
  money = int(input("\n Insert Cash or select payment type (AED): "))
  choice = int(input("\n Choose your order number:"))

  if choice not in items:
    print("\n error, cant do that pal.")
    return

    item_name, price = items[choice]

    print(f"\nYou chose: {item_name}")
    print(f"Price: {price} AED")

    # exact amount
    if money == price:
      print("you actually sent enough cash.")
      print("thanks lol")

      # More money -> return change