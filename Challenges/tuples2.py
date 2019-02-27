# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]


def combo(iterable1, iterable2):
    lista = []

    for index1, letter1 in enumerate(iterable1):
        for index2, letter2 in enumerate(iterable2):
            if index1 == index2:
                lista.append(tuple([letter1, letter2]))
    return lista
    

print(combo([1, 2, 3], 'abc'))