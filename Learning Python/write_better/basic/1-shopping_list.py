shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to sholl the entire list
""")
    

def add_to_list(item):
    shopping_list.append(item) 
    print("Added item #{}:".format(len(shopping_list)),"{}".format(item))


def show_list():
    print("{} Itens Added:".format(len(shopping_list)))
    item_number = 1
    for item in shopping_list:
        print("#{} {} ".format(item_number,item))
        item_number += 1
    
show_help()

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)
show_list()