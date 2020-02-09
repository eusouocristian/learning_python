def stringcases(string):
    upper = string.upper()
    lower = string.lower()
    title = string.title()
    lista = list(string)
    lista.reverse()
    reverse_out = ''.join(lista)
    return tuple([upper,lower,title,reverse_out])

print(stringcases('stratocaster'))