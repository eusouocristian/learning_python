import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

shopping_list = []

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to sholl the entire list.
Enter 'REMOVE' to delete an item from you list.
""")


def add_to_list(item):
    show_list()
    # se shopping list is not empty, it ask the user to choose the position to insert the item
    if len(shopping_list):
        position = input("Where should I add {}?\n"
        "press ENTER to add the item to the end of the list\n"
        "> ".format(item))
    else:
        # Otherwise it set the position to the index zero
        position = 0
    
    try:
        position = abs(int(position))
    except ValueError:
        position = None

    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(item)
    
    show_list()



def show_list():
    clear_screen()
    print("{} Itens Added:".format(len(shopping_list)))
    print("-"*10)
    for index, item in enumerate(shopping_list, start = 1):
        print("{}. {}".format(index,item))
    print("-"*10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
        show_list()
    except ValueError:
        pass


show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    else:
        add_to_list(new_item)
show_list()
