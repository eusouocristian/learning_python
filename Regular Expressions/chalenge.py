import re

data = '1-Cristian Figueiredo dos Santos2'

def first_number(data):
    search = re.match(r'\d', data)
    return search

print(first_number(data))