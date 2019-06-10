import os
clear = lambda: os.system('cls')
clear()
data = input('type a string:\n>> ')
data_inverted = data[::-1]
print('The inverted string is\n>>',data_inverted)

def stringcases(string):
    upper = string.upper()
    lower = string.lower()
    title = string.title()
    lista = list(string)
    lista.reverse()
    reverse_out = ''.join(lista)
    return tuple([upper,lower,title,reverse_out])

print(stringcases('stratocaster'))
