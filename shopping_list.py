#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type add to begin adding to your shopping list. \n or you can type remove to begin removing items. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list

shopping_list = []

def prompt_user():

    reply = input("What do you want to add or remove?  >>  ").lower()

    return reply

def check_answer(ans):
    

    if ans == "add":
        add_item()
    elif ans == "remove":
        remove_item()
    else:
        print("error")
        prompt_user()
   

def add_item():

    user_item = input("what item do you want")
   
    if user_item in shopping_list:
        print("One of each item only")
        prompt_user()
    else:
        shopping_list.append(user_item)
        print("Sucessfully added", user_item)
        print(shopping_list)


def remove_item():
    
    user_remove_item = input("What item do you want to remove")

    if user_remove_item not in shopping_list:
        print("No such item in cart")
        prompt_user()
    else:
        shopping_list.remove(user_remove_item)
        print("Sucessfully removed", user_remove_item)
        print(shopping_list)


while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True

intital = prompt_user()
check_answer(intital)
