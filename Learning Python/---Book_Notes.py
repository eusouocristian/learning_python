import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

# Data structures

# Lists:
# mutable, iterable, have an order
list1 = [1,2,3]

# Dictionaries:
# mutable, iterable, doesn't have an order
dict1 = {'Name': 'Cristian', 'Age': 32, 'Skill': 'Engineer'}

#Tuples:
# Immutable
# you can transform a list into a tuple
tuple1 = 5, 6, 7
tuple2 = (2,3,4)
tuple3 = tuple(list1)
print('tuple1: {}'.format(tuple1),
      'tuple2: {}'.format(tuple2),
      'tuple3: {}'.format(tuple3))






