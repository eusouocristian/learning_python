# A function that takes a string and must return a tuple with:
# All Upercases
# All Lowercase
# Titlecased
# Reversed

def stringcases(string):
    upper = string.upper()
    lower = string.lower()
    titled = string.title()

    reverse = list(string)[::-1]
    reverse = "".join(reverse)
    
    return (upper,lower,titled, reverse)

tuple_result = stringcases("CrisTIan FigueIREdo DOs SanTos")
print(tuple_result)
# print de somente um dos items do tuple
print(tuple_result[1])


