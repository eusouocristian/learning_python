import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()

favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']
slice1 = favorite_things[2:5]
slice2 = favorite_things[5:]
sorted_things = favorite_things[:]
sorted_things.sort()
print(slice2)
print(sorted_things)

# Criar uma lista - funcao range()
numbers = list(range(20))
print("numbers: ",numbers)
# Copiar a lista com passos de 2 em 2
# : (toda a lista), : (com passos de), 2 => (::2)
# 2:20 (item 2 a 20), com passos de 2 => (2:20:2)
print("numbers[::2]: ",numbers[::2])
# os passos podem ser negativos
print("numbers[-5:-8:-1]: ", numbers[-5:-8:-1])
# inverte a sequencia da lista
print("numbers[::-1]: ", numbers[::-1])

def first_and_last_4(thing):
    first_four = thing[:4]
    last_four = thing[-4:]
    print(first_four+last_four)

first_and_last_4(input("digite a coisa:/n> "))
