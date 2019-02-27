import os
clear = lambda: os.system('cls')
clear()
data = input('type a string:\n>> ')
data_inverted = data[::-1]
print('The inverted string is\n>>',data_inverted)
