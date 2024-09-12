import random 
import time
import os
import sys

# The reason to disapper game. Inspired by my sister
# Main reason to use class I guess farther widespread capabilites and just to show what I recently learned

class Person():
    def __init__(self, name, age, factors, relation):
        self.name = name
        self.age = age
        self.factors = factors 
        self.relation = relation

    def key_factor(self, rand_2):
        
        if rand_2 == 1:
            print("Up first the first reason you should be gone", self.factors[0])
        elif rand_2 == 2 and len(self.factors) >= 2:
            print("Now to of the best reasons to be gone", self.factors[0], self.factors[1])
        elif rand_2 == 3 and len(self.factors) >=3:
            print("Now for some suspense this is a big reason why you must be gone")
            time.sleep(5)
            print(self.factors[3])
        else:
            print("Heh, we will let the main reasons slide this time")
    
    def secondary_factor(self, rand_1):
        if rand_1 == 1:
            print("By the way have you seen your name", self.name)
        elif rand_1 == 2:
            print(f"How can you be {self.age} and still be like that!?")
        elif rand_1 == 3:
            print("Honestly how could can we ever be", self.relation, "It's unbareable")
        else:
            print("Heh, we will let the main reasons slide this time")

def user_promts():
    try:
        user_input_1 = input("\nWell let's start the reasons, whats the offenders name? Example >> Mujtaba\n")
        user_input_2 = int(input("Also what's his age? Example >> 10\n"))
        user_input_3 = input("What are some reasons you want this person gone? We will take up to 5 reasons. Example >> Cause he bothers me, Cause his a bum\n").split(", ")
        user_input_4 = input("Now finally whats your two relation? Example 'Brother and Sister'\n")

        offender = Person(user_input_1, user_input_2, user_input_3, user_input_4)

        rand_1 = random.randint(1,4)
        rand_2 = random.randint(1,4)

        offender.key_factor(rand_2)
        offender.secondary_factor(rand_1)
    except:
        print("Well we don't aceapt that is a valid answer. Let's roll it back")
        user_promts()

user_promts()