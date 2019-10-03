import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

# Criar um set com dados
set1 = {"Dado 1","Dado 2","Dado 3"}
set2 = set(["Dado 4","Dado 5", "Dado 6"])
print(type(set1))
print(type(set2))
print(set1)
print(set2)
print("\n")

set_a = set([1,2,3,4])
print("set_a: ", set_a)
set_a.add(5)
print("set_a.add(5): ",set_a)
set_a.update({6,7}, {8,9}) #uptade can add a group of sets at once
print("set_a.update({6,7}, {8,9}): ",set_a)
set_a.remove(1) # returns an error when the item doesn't exist in the set
print("set_a.remove(1): ",set_a)
set_a.discard(2) #Doesn't return an error if the item is not in the set
print("set_a.discard(2): ",set_a)
item_pop = set_a.pop() # .pop() takes a item off the set, the first one, and returns it
print("item_pop = set_a.pop(): ", item_pop)



print("\n\n")

# Union (cria um novo set com a união dos items em ambos os sets)
set3 = set([1,3,4,5,6,7,8])
set4 = set([6,7,8,9,10])
print("set3: ",set3)
print("set4: ",set4)
print("set3.union(set4): ",set3.union(set4))
print("\n")


# Difference (Itens que estão no primeiro set E NAO estão no segundo set)
# Pode ser escrito de duas formas conforme abaixo
print("set3.difference(set4): ",set3.difference(set4))
print("set3.difference(set4): ",set3 - set4)
print("set4.difference(set3): ",set4 - set3)
print("\n")



# operador ^ (symmetric_difference)
# Union entre set3.difference(set4) e set4.difference(set3)
print("set3 ^ set4: ", set3 ^ set4)
print("set3.symmetric_difference(set4): ", set3.symmetric_difference(set4))
print("\n")

# operador & (intersection)
# Itens que estão em ambos os sets
print("set3 & set4: ", set3 & set4)
print("set3.intersection(set4): ", set3.intersection(set4))
print("\n")







