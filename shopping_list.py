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

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type add to begin adding to your shopping list. \n or you can type remove to begin removing items. \n Also note you may only take one of any item. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list

shopping_list = []

def prompt_user():
 
    reply = input("What do you want to add or remove? Example: add Bacon  >>  ").lower()
    
    list_1 = reply.split(" ")

    return list_1

def check_answer(ans):
    
    if len(ans) == 2:
        if ans[0] == "add":
            add_item(ans)
        elif ans[0] == "remove":
            remove_item(ans)
        else:
            print("That is not a valid answer")
    else:
        print("That is not a valid answer")
    
def add_item(ans):
   
    if ans[1] in shopping_list:
        print("\nOne of each item only\n")
    elif ans[1] == "" or ans[1].isspace():
        print("\nThat is not a valid answer.\n")
    else:
        shopping_list.append(ans[1])
        print("\nSucessfully added\n\n", ans[1])
        print("Your current items >> ", shopping_list)

def remove_item(ans):

    if ans[1] not in shopping_list:
        print("\nNo such item in cart\n")       
    else:
        shopping_list.remove(ans[1])
        print("\nSucessfully removed\n\n", ans[1])
        print("Your current items >> ", shopping_list)

while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True

