
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "\nWelcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("\n------------------- Challenge 1 -------------------\n")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether the user is legally allowed to drive in your city. 

print('Hello, this is a driving right check. Please enter your age')

UserInput = input()

if UserInput > '16':
  print('You are of age to drive') 
else :
  print('You are not of age to drive', '\n\ndo not drive'.upper())





# -------------------------------------------- 

print("\n------------------- Challenge 2 -------------------\n") 

# Who placed first?
   # Create three variables and assign them random scores. 
   # Write conditional statements that check which is the highest score and prints it.

import random

Score1 = random.randint(1,9)
Score2 = random.randint(1,9)
Score3 = random.randint(1,9)

print('Game Test - You are player One\n\n')

if Score1 > Score2 and Score1 > Score3:
   print('Player One is the winner'.upper())
elif Score2 > Score1 and Score2 > Score3:
   print('Player Two is the winner'.upper())
elif Score3 > Score1 and Score3 > Score2:
   print('Player Three is the winner'.upper())
elif Score1 == Score2 and Score1 > Score3 or Score1 == Score3 and Score1 > Score2:
   print('Draw')
elif Score2 == Score1 and Score2 > Score3 or Score2 == Score3 and Score2 > Score1:
   print('Draw')
elif Score3 == Score2 and Score3 > Score1 or Score3 == Score1 and Score3 > Score2:
   print('Draw')
elif Score1 == Score2 == Score3:
   print('Total Draw'.upper())




# -------------------------------------------- 

print("\n------------------- Challenge 3 -------------------\n")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "rainy"













# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.












# -------------------------------------------- 

print("\n------------------- Challenge 4 -------------------\n")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 











# -------------------------------------------- 

print("\n------------------- Challenge 5 -------------------\n")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.






