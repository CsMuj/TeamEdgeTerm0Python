import random 
import time
import os
import sys
from PIL import Image

finsh_flag = False
player_items = []
player_time = 25
player_tries_requirement = random.randint(2,4)

class Location:
    def __init__(self, location, moves, actions, atmosphere, image):
        self.location = location
        self.moves = moves
        self.actions = actions
        self.atmosphere = atmosphere
        self.image = image 

    def locate(self, user_input):
        global player_time
        
        dict_1 = {"game lounge":lab_game_lounge, "orange room":lab_orange_room, "blue room":lab_blue_room, "food bar":lab_food_bar, "hallway":lab_hallway, "lounge":lab_lounge, "entrance":lab_entrance}
        req_dict = dict_1.get(user_input)
        
        if user_input in dict_1:
            print("\nSucessfully moved to the", user_input)
            player_time -= 1
            return req_dict
        else:
            print("Well you can't do that")

    def special_actions(self, user_input):
        global player_items
        global finsh_flag
        global player_time 
        global player_tries_requirement

        if user_input in self.actions:
            player_time -= 1
            if user_input == "coach stephanie":
                player_items.append("key1")
                print("\nHey remember what you missed? It was classes and dictionaries. These should be useful in your code")
            elif user_input == "coach julian":
                player_items.append("key2")
                print("\nGood moring. If you think your nearly there, but not quite you probaly forgeting capitalization")
            elif user_input == "coach jeremy":
                player_items.append("key3")
                print("\nHey! nerd, just joking. Remember to indent your code it key for it to function properly")
            elif user_input == "coach paul":
                print("\nWell I'm not sure how to help. But remember trying again never hurts.")
            elif user_input == "eat food":
                print("\nYou ate amazing food and a couple of snacks")
                player_time += 10
            elif user_input == "red room":
                print("\nRoom is locked")
                player_time -= 1
            elif user_input == "closet" or user_input == "play games" or user_input == "printers and etc" or user_input == "red room":
                print("\nYou wonder and tinker around. You realize you lost 10 energy")
                player_time -= 10
            elif user_input == "work computer":
                player_tries_requirement -= 1
                if "key1" in player_items and "key2" in player_items and "key3" in player_items and player_tries_requirement <=0:
                    print("\n\n\n\n\n\n\nYou yell in celebration. You finished your task and your done!!".upper())
                    finsh_flag = True
                else:
                    print("You failed to finish. Maybe you need some help..")
        else:
            print("Well you can't do that")
    
    def on_enter(self):
        global player_time

        if player_time > 40:
            player_time = 40
        elif player_time <= 0:
            print("\nYou ran out of time. You are defeated by your coding challange") 
            time.sleep(2.5)
            os.execv(sys.executable, ['python'] + sys.argv)

        self.image.show()
        print(f"\n\n\n\n--You're in the {self.location}-- \n {self.atmosphere} \n\n\nYou're looking around for what you can do... < {', '.join(self.moves)}, {', '.join(self.actions)} >\n<< You have enough energy for {player_time} actions >>")

lab_game_lounge = Location("Game Lounge", ["hallway"], ["coach jeremy", "play games"], "You now rest in a great area. One full of games to play to your hearts content.", Image.open("./picture4.jpg"))
lab_orange_room = Location("Orange Room", ["hallway"], ["coach julian"], "You're in a perfect learning room for far as you can see. Some neat things of note are Launch's project. Their plan for their companies", Image.open("./picture2.jpg"))
lab_blue_room = Location("Blue Room", ["hallway"], ["closet", "coach paul", "work computer"], "You come across the work you got to do on your laptop, the atmosphere here is nice. It's very homey", Image.open("./picture5.jpg"))
lab_food_bar = Location("Food bar", ["lounge"], [ "closet", "eat food"], "First thing when entering the space you smell the mouth water aroma of the food. It yerns you to eat it.", Image.open("./picture6.jpeg"))
lab_hallway = Location("Hallway", ["lounge", "blue room", "orange room", "game lounge"], ["red room "], "You arrive at a lifted hallway overlooking the lounge. And it greatly attracts your attenion with all the wonderes things on the wall", Image.open("./picture1.jpeg"))
lab_lounge = Location("Lounge", ["hallway", "food bar"], ["printers and etc", "coach stephanie"], "You enter a comfortable and large room, filled to the brim with working space, and many other interesting things", Image.open("./picture1.jpeg"))
lab_entrance = Location("Entrance", ["lounge"], [], "It's a calm monday afternoon. Nice and bright. Your back at code next. Here to make up work you misssed. Well now you better go in and get you coding challenge done. Hmm.. You should go ask a coach for help", Image.open("./picture0.jpg"))

current_location = lab_entrance

def user_promts():
    try:
        global current_location

        dict_1 = {"game lounge":lab_game_lounge, "orange room":lab_orange_room, "blue room":lab_blue_room, "food bar":lab_food_bar, "hallway":lab_hallway, "lounge":lab_lounge, "entrance":lab_entrance}

        current_location.on_enter()
        user_input = input("\nWell let's pick what you will do. Who knows maybe you need help or need to eat. Well it can't hurt trying.\n\n" ).lower().strip() 
        
        if user_input in dict_1:
            current_location = current_location.locate(user_input)
        else:
            current_location.special_actions(user_input)
    except:
        print("Well you can't do that")    

print("\nWell here's the deal for this game to do any actions you must type like say if you were given a option to lounge to go there just type lounge. Or to talk to someome type there title like Coach stephanie. Remember your goal is to finish your coding challange. Get much help as you can and remember theres a limit to your actions. Lastly don't worry you don't got to worry about coding")

while finsh_flag == False:
    user_promts()     