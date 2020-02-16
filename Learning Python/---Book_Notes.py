import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

# Data structures

# Lists:
# mutable, iterable, have an order
list1 = [1,2,3]

## Dictionaries:
# mutable, iterable, doesn't have an order
dict1 = {'Name': 'Cristian', 'Age': '32', 'Skill': 'Engineer'}
#print all the keys:
print(f'All the keys of dict1: {dict1.keys()}')
#print all the values:
print(f'All the Values of dict1: {dict1.values()}')
#Sort the dictionaries values and keys:
print(f'Sorted keys: {sorted(dict1.keys())}')
print(f'Sorted Values: {sorted(dict1.values())}')
#Changing values:
dict1['Name'] = 'Figueiredo'
print(f'dict1 novo: {dict1}')
#Add a new key:
dict1['Estatura'] = 'Alto' 
print(f'dict1 com key nova{dict1}')
#Delete a key
del(dict1['Age'])
print(f'dic1 com Age deletado: {dict1}\n')

# unpacking using items()
for key, value in dict1.items():
      print(key)
      print(value)
print(f'\n')

# To pack a Dictionarie, we have to use duble '**'
def packer(**kwargs):
      for key, value in kwargs.items():
            print(f'{key}: {value}')
packer(name = "Cristian", Idade = 32, Religiao = False, Status = "Married")
print(f'\n')

##Tuples:
# Preferable to use, we can acess the data quickly
# Immutable <<<----
# you can transform a list into a tuple
tuple1 = 5, 6, 7
tuple2 = (2,3,4)
tuple3 = tuple(list1)
print('tuple1: {}'.format(tuple1))
print('tuple2: {}'.format(tuple2))  
print('tuple3: {}'.format(tuple3))   
# To pack a Tuple, we have to use simple '*'
def tuple_packer(*args):
      print(args)
tuple_packer('cristian',27,[1,2,3,4]) #It creates a tuple with  a 'str', 'int' and a 'list'     

# Enumerate in for loop
# f' inside print() to format the content
letter_list = ['a','b','c','d','e','f','g','h','i']
for index, letter in enumerate(letter_list, start=1):
      print(f'{index}. {letter}')


fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')
'eggplant' in fruits # False
'eggplant' not in fruits # True
'eggplant' in vegetables # True
'eggplant' not in vegetables # False


my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')
my_pets.index('dog') # 0
my_pets.index('chicken') # 3

my_pets = ['dog', 'cat', 'cat', 'chicken', 'dog']
my_pets.count('cat') # 2
my_pets.count('lizard') # 0

nums = range(1, 10, 2) # start, stop, step
0 in nums # False
6 in nums # False
4 not in nums # True
8 not in nums # True

nums = range(1, 10, 2)
nums.index(5) # 2
nums.index(1) # 0