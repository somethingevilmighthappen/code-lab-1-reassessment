
money = 10.00 #this is the starting balance
vending_machine = {"Chips":"0A", "Soda":"0B", "Chocolate":"0C", "Fruits":"0D"} #this is the dictionary
prices = {"Chips":"2 AED", "Soda":"1 AED", "Chocolate":"1.50 AED", "Fruit Snacks":"0.25 AED"} #these are the price values


#==Debug Functions==================================
def set_money(amount): #used this function to set the money
	global money0d
	money = amount
	
	
def purchase(needed_money): #this one keeps track of money after checking to see if you can buy said item
	global money
	if money >= needed_money:
		money -= needed_money
		print("Item purchased.")
	else:
		print("Insufficient funds.")

def transaction(user_input): #made this function to take care of choosing said item, it then calls the "purchase" function
	global money
	if user_input == "0A":
		purchase(2)
	elif user_input == "0B":
		purchase(1)
	elif user_input == "0C":
		purchase(1.5)
	elif user_input == "0D":
		purchase(0.25)
	else:
		print("error, invalid code.")
	
			
#==============================================================	
		

def main(): #main program 
	item_list = []
	switch = 1 
	while switch == 1:
		print("Welcome to the Vending Machine program.") #greetings
		print("Here are your selections!")
		for item, selection in vending_machine.items(): #this for loop appends items to the item_list
			item_list.append((item, selection))
		
		print(item_list[::-1]) #print backwards so that it goes from top to the bottom
		
		print()
		print("Here are the prices")
		for item, price in prices.items(): #prints the items and their prices on separate lines
			print(item, price)
		print()	
		
		user_switch = 1 #User Proof loop
		while user_switch == 1:
			print("You currently have AED" + str(money))
			user_input = input("Write down the codes listed above to select an item: ").upper()
			transaction(user_input)
			print()
			choice = 1
			while choice == 1: #User proof loop
				user_input = input("Are you finished with the vending?(y/n): ").lower()
				if user_input == "y":
					user_switch = 0
					choice = 0
					switch = 0
				elif user_input == "n":
					user_switch = 1
					choice = 0
				else:
					print("Invalid command")
					choice = 1
					
		
main()