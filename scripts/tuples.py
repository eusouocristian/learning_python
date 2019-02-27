import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# função que soma todos os items inseridos como argumento
# versão 1:
def summ(*args):
    total = 0
    for item in args:
        total += item
    return total

def summ2(base, *args):
    total = base
    for item in args:
        total += item
    return total

clear_screen()
print("Metodo de soma 1: ")
soma1 = summ(1,2,3,4)
print(soma1)

print("\nMetodo de soma 2: ")
soma1 = summ2(1,2,3,4,5)
print(soma1)

for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz",start = 1):
    print("{}. {}".format(index , letter))

    