import os
import re    # import regular expressions (RE)

# clean the terminal screen
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

# to understand the difference between normal strings and raw strings:
print('This is a \n normal string')
print(r'This is a \n raw string') # it ignores the codes like \n used to format strings

# \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
# \W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
# \s - matches whitespace, so spaces, tabs, newlines, etc.
# \S - matches everything that isn't whitespace.
# \d - is how we match any number from 0 to 9
# \D - matches anything that isn't a number.
# \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
# \B - matches anything that isn't the edges of a word.


# Open a txt file:
#--------------------------------------------------------------
# names_file is a pointer to the names.txt file on the system
names_file = open('names.txt', encoding='utf-8') 
# data recieves all the content from names.txt file
data = names_file.read()
# then close the file to realease memory
names_file.close()

# use match to look for a string at the beginning of the text
print(re.match(r'Love', data))
# use search to look for a string in somewhere in the text
print(re.search(r'Kenneth', data))

# We have to put \ before () like that -> \( <content> \) because parenthesis have a different meaning in raw strings
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))




