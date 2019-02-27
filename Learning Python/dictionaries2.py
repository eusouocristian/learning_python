import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)

dict = {"name": "Cristian", "food": "shrimps"}
print(favorite_food(dict),"\n")