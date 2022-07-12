# -------------------------------------------- 

	# You've just learned about functions.
	# Functions are reusable pieces of code that make your code more modular.
	
	# If you are writing the same bit of code over and over, you are doing more work that you have to.
	# Use functions xto simplify your code and decrease the amount of work you're doing. 

	# Any time you start thinking 'this is tedious', you can probably write a function for that task.

# -------------------------------------------- 


# -------------------------------------------- 
  # Challenge 1: Let's try to write some basic functions.
# -------------------------------------------- 

print("\n------------------- Challenge 1 -------------------\n")

# **** Challenge 1: Problem 1 ****
# Write a function called print_message() that prints any message you want.

def print_message(x):
	print(x)

print_message('Hi\n')

# **** Challenge 1: Problem 2 ****
# Write a function called print_five_messages() that calls print_message() five times.

def print_message5x(x):
	print(x, x, x, x, x)

print_message('Hi')



# **** Challenge 1: Problem 3 ****
# Write a function called get_user_input() that asks the user if they'd like to print your message
# once or five times. Then call one of the two functions above based on what the user decides.

Result = input('Print 1 or 5 times?')

def print_message5x(x):
	print(x, x, x, x, x)

def print_message(x):
	print(x)

if Result.lower() == '5 times':
	print_message5x('Hi')
elif Result.lower() == '1 time':
	print_message('Hi')
	

# **** Challenge 1: Problem 4 ****
# Write a function called print_greeting() that prints a greeting message to the user.

def print_greeting():
	print('Hello, thank you for using functions program')


# **** Challenge 1: Problem 5 ****
# Write a function called print_closing() that prints a goodbye message to the user.

def print_closing(x):
	print(f'Goodbye, thank you {x} for using functions program')


# **** Challenge 1: Problem 6 ****
# Write a function called run() that greets the user, asks them for input, and sends a goodbye message.
# Remember! Use the functions that you've already made. Don't hardcode anything!

def run():
	print_greeting()
	name = input('Please input your name')
	print_closing(name)
run()

# -------------------------------------------- 

# Challenge 2: Functions are also able to take input and return output. 
				# The value(s) you pass to it are called parameters.

# -------------------------------------------- 

print("\n------------------- Challenge 2 -------------------\n")

# **** Challenge 2: Problem 1 ****

# Write a function called sum_double that takes two number paramters and returns their sum.
# However, if the two values are the same, the funciton will return double their sum.

	# Examples:
		# sum_double(1, 2) → 3
		# sum_double(3, 2) → 5
		# sum_double(2, 2) → 8


def sum_double(x, y):
	addition = x+y
	Multiplyer = addition*2
	print(Multiplyer)

sum_double(5, 10)

# -------------------------------------------- 







# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 2 ****

# Write a function called makes_10 that takes two numbers, a and b, and returns true if one of them is 10 or if their sum is 10.

	# Examples:
		# makes_10(9, 10) → True
		# makes_10(9, 9) → False
		# makes_10(1, 9) → True

# -------------------------------------------- 

def makes_10(a, b):
	
	if a == 10 or b == 10:
		print('True')
	elif a+b==10:	
		print('True')
	else:
		print('false')

makes_10(5, 5)





# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 3 ****

# Write a function that will return the time our alarm is set to go off.

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string in the form "7:00" indicating
# when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
# the weekend it should be "10:00". However, if we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".
	# Examples:
		# alarm_clock(1, False) → "7:00"
		# alarm_clock(6, True) → "off"
		# alarm_clock(0, False) → "10:00"

# -------------------------------------------- 

def alarm_clock(x, y):
	
	vaccation = y
	
	if vaccation == False:
		if x == 0 or x == 6:
			time = '10:00'
		else:
			time = '7:00'
	else:
		time = 'off'

	print(time)	

alarm_clock(6, True)






# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 4 ****

# Write a function that will tell you if you received a speeding ticket.
# You are driving a little too fast, and a police officer stops you. 

# To compute the result, encoded as a number value: 
	# 0=no ticket
	# 1=small ticket
	# 2=big ticket
# If speed is 60 or less, the result is 0. 
# If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2.

# -------------------------------------------- 

def speeding_ticket(x):

	if x < 60:
		print('Result 0, No ticket')
	elif x < 80 and x > 60:
		print('Result 1, Small ticket')
	else:
		print('Result 2, Big ticket')

speeding_ticket(170)






# Make sure to test your code! Write a few function calls to make sure your code works!
