import copy

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
messy_list.insert(0,messy_list.pop(3))
messy_list1 = copy.copy(messy_list)
for item in messy_list1:
    # isinstance() verifica o tipo de variavel
    if isinstance(item,str):
        messy_list.remove(item)