import random 
import os
import sys

finsh_flag = False
player_items = []
player_time = 30

class Location:
    def __init__(self, location, moves, actions, atmosphere):
        self.location = location
        self.moves = moves
        self.actions = actions
        self.atmosphere = atmosphere

    def locate(self, user_input):
        dict_1 = {"game lounge":lab_game_lounge, "orange Room":lab_orange_room, "blue Room":lab_blue_room, "food bar":lab_food_bar, "hallway":lab_hallway, "lounge":lab_lounge, "entrance":lab_entrance}
        req_dict = dict_1.get(user_input)

        if user_input in dict_1.keys():
            return req_dict
        # else:
        #     print("Well you can't do that")

    def special_actions(self, user_input):
        global player_items
        global finsh_flag
        player_tries = 0
        player_tries_requirement = random.randint(2,4)

        if user_input in self.actions:
            if user_input == "coach stephaine":
                player_items.append("key1")
                print("Hey remember what you missed before was classes. Remember to use them there key")
            elif user_input == "coach jullian":
                player_items.append("Key2")
                print("Good moring. If you think your nearly there, but not quite you probaly forgeting dictonaries")
            elif user_input == "coach jeremy":
                player_items.append("key3")
                print("Hey! nerd, just joking. Remember to indent your code it key for it to function properly")
            elif user_input == "coach paul":
                print("Well I'm not sure how to help. But remember trying again never hurts.")
            elif user_input == "eat food":
                print("You ate amazing food and a couple of snacks")
                player_time += 15
            elif user_input == "red room":
                print("Room is locked")
            elif user_input == "closet" or user_input == "play games" or user_input == "printers and etc.":
                print("You wonder and tinker around. You realize you lost 10 energy")
                player_time -= 10
            elif user_input == "your working commputer" or user_input == "working computer":
                player_tries += 1
                if "key1" in player_items and "key2" in player_items and "key3" in player_items and player_tries_requirement <=0:
                    print("\n\nYou yell in celebration. You finished your task and your done!!")
                    finsh_flag = False
                else:
                    print("You failed to finish. Maybe you need some help?")
        # else:
        #     print("Well you can't do that")
    
    def on_enter(self):
        global player_time

        if player_time <= 0:
            print("You ran out of time. You are defeated by your coding challange") 
            os.execv(sys.executable, ['python'] + sys.argv)

        print(f"\n Your in {self.location} \n")
        print(f" {self.atmosphere} ")
        print(f"\nYou look around for what you can do you can {self.moves}, {self.actions}")
        print(f"You have {player_time} minutes of energy left")

lab_game_lounge = Location("Game Lounge", [], ["coach Jeremy", "play games"], "You now rest in a great area. One full of games to play to your hearts content.")
lab_orange_room = Location("Orange Room", [], ["coach Julian"], "Your in a perfect learning room for far as you can see. Some neat things of note is Launches project. Their plan for there companys")
lab_blue_room = Location("Blue Room", [], ["closet", "coach paul", "your work commputer"], "You come across the work you got to do on your laptop, the atmosphere here is nice. It's very homey")
lab_food_bar = Location("Food bar", [], [ "closet", "eat food"], "First thing when entering the space you smell the mouth water aroma of the food. It yerns you to eat it." )
lab_hallway = Location("Hallway", [lab_blue_room, lab_orange_room, lab_game_lounge], [], "You arrive at a lifted hallway overlooking the lounge. And it greatly attracts your attenion with all the wonderes things on the wall")
lab_lounge = Location("Lounge", [lab_hallway], ["printers and etc.", "coach Stephaine"], "You enter a comfrotable and large room, filled to the brim with working space, and many other intresting things")
lab_entrance = Location("Entrance", [lab_lounge], [], "It's a calm monday afternoon. Nice and bright. Your back at code next. Here to make up work you missed. Well now you better go in and get you coding challenge done")
lab_food_bar.moves = [lab_lounge]
lab_hallway.moves = [lab_lounge]
lab_food_bar.moves = [lab_lounge]
lab_blue_room.moves = [lab_hallway]
lab_orange_room.moves = [lab_hallway]
lab_game_lounge.moves = [lab_hallway]

current_location = lab_entrance

def user_promts():
    # try:
        global player_time
        global current_location
        dict_1 = {"game Lounge":lab_game_lounge, "orange Room":lab_orange_room, "blue Room":lab_blue_room, "food bar":lab_food_bar, "hallway":lab_hallway, "lounge":lab_lounge, "entrance":lab_entrance}

        current_location.on_enter()
        user_input = input("\nWell let's pick what you will do.\n" ).lower()
        player_time -= 1 
        
        if user_input in dict_1:
            current_location = current_location.locate(user_input)
        else:
            current_location.special_actions(user_input)
    # except:
    #     print("Well you can't do that")    

while finsh_flag == False:
    user_promts()