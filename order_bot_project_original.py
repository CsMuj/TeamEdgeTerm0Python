# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------
import time
import os
import sys

tax = 0.08875

scrambled_eggs = 3.49
chicken_apple_sausage = 4.99
roasted_sweet_potatoes = 2.49
country_grain_bread = 1.99
sliced_fruit = 2.99
cooled_Snapple = 2.99
cooled_tropicana = 1.00


# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------
def main_course(x):
	
	if x == 1:
		print(f"Scrambled eggs, {scrambled_eggs}")
	elif x == 2:
		print(f"Chicken apple sausage, {chicken_apple_sausage}")
	elif x == 3:
		print(f"Chicken apple sausage, {chicken_apple_sausage}")

def sub_course(x):

	if x == 1:
		print(f"Country Grain Bread, {country_grain_bread}")
	elif x == 2:
		print(f"Sliced fruit{sliced_fruit}")

def drinks(x):
	
	if x == 1:
		print(f"Cooled snapple, {cooled_Snapple}")
	elif x == 2:
		print(f"Cooled snapple, {cooled_tropicana}")
	elif x == 3:
		print("Water, Free")

def order_menu():

	print("\n--Menu--\n")
	print(f"\n --- Main Course ---\n1. Scrambled Eggs, ${format(scrambled_eggs, '.2f')}\n2. Chicken & Apple Sausage, ${format(chicken_apple_sausage, '.2f')}\n3. Roasted Sweet Potatoes, ${format(roasted_sweet_potatoes, '.2f')}")
	print(f"\n --- Sub Course ---\n4. Country Grain Bread, ${format(country_grain_bread, '.2f')}\n5. Sliced fruit, ${format(sliced_fruit, '0.2f') }")
	print(f"\n --- Drinks ---\n6. Cooled Snapple, ${format(cooled_Snapple, '.2f')}\n7. Cooled Tropicana, ${format(cooled_tropicana, '.2f')}\n8. Water, Free ")
	print("\n --- Extra ---\nCoach jeremy's Jokes, You pick your price\n\n")
	
	answer_2 = input("What Main Course shall you have? \n").lower()
	answer_3 = input("What Sub Course will you have?\n").lower()
	answer_4 = input("What Drink do you want?\n").lower()



	if answer_2 == "scrambled eggs":
		cost_1 = scrambled_eggs
		main = 1
	elif answer_2 == "chicken apple sausage":
		cost_1 = chicken_apple_sausage	
		main = 2
	elif answer_2 == roasted_sweet_potatoes == "roasted sweet potatoes":
		cost_1 = roasted_sweet_potatoes
		main = 3		
	else:
		print("I don't understand. Please repeat yourself.")
		time.sleep(2)
		order_menu()

	if answer_3 == "country grain bread":
		cost_2 = cost_1+country_grain_bread
		sub = 1
	elif answer_3 == "sliced fruit":
		cost_2 = cost_1+sliced_fruit
		sub = 2
	else:
		print("I don't understand. Please repeat yourself.")
		time.sleep(2)
		order_menu()
	
	if answer_4 == "cooled snapple":
		cost_3 = cost_2+cooled_Snapple
		juice = 1
	elif answer_4 == "cooled tropicana":
		cost_3 = cost_2+cooled_tropicana
		juice = 2
	elif answer_4 == "water":
		cost_3 = cost_2
		juice = 3
		water = True
	else:
		print("I don't understand. Please repeat yourself.")
		time.sleep(2)
		order_menu()
	
	cost_5 = float(input("How much do you want to pay for jeremy's jokes?"))

	sub_total = cost_3+cost_5
	
	taxed_price = format(round(sub_total*1+tax, 2), '.2f')

	print(f"\n -- Sub Total -- {format(round(sub_total, 2), '.2f')}")

	main_course(main)
	sub_course(sub)
	drinks(juice)
	print("Jeremy's jokes", format(cost_5, '.2f'))

	print("Tax", taxed_price)

	answer_5 = float(input('how much do want to tip? Enter decimal number only'))
	final = float(taxed_price)*(1+answer_5)

	print("Total", format(round(final, 2), '.2f'))

	answer_6 = float(input("how was your expirence out of 5. Whole numbers only "))
	
	if answer_6 <= 2:
		print("Oh really? Well then I'll give you a discount, your total is", format(round(final*.70, 2), '.2f'))
	elif answer_6 <= 3.5 and not answer_6 <= 2:
		print("Alright. You know what enjoy a small discount", format(round(final*.9, 2), '.2f'))
	elif answer_6 > 3.5:
		print("Great")
	else:
		print("okay")
	

answer_1 = input("\nHello, would you like to order food via CodeNext Lab food bar? Yes or No?\n Note you must order a Main Course, Sub Course and Drink\n\n").lower()

if answer_1 == "yes" or answer_1 == "y":
	print("\nHere is the menu")
	order_menu()
elif answer_1 == "no" or answer_1 == "n":
	print("\nAre you sure?")
	time.sleep(2)
	os.execl(sys.executable, sys.executable, *sys.argv)	
else:
	print("Sorry I don't understand.")
	os.execl(sys.executable, sys.executable, *sys.argv)





# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------












# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 












# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 




# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
