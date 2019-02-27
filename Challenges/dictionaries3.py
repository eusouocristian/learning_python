# Chalenge!!

# Alright, this one might be a bit challenging but you've been doing great so far, so I'm sure 
# you can manage it.
# I need you to make a function named word_count. It should accept a single argument which will 
# be a string. The function needs to return a dictionary. The keys in the dictionary will be each
# of the words in the string, lowercased. The values will be how many times that particular word 
# appears in the string.
# Check the comments below for an example.

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.


def word_count(string):
    dictionary = {}
    string_list = string.lower().split(" ")
    for word in string_list:
        dictionary[word] = string_list.count(word)
    return dictionary

print(word_count(input("> ")))
        
