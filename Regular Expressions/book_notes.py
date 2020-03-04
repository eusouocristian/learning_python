import os
import re    # import regular expressions (RE)

# clean the terminal screen
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

# to understand the difference between normal strings and raw strings:
#print('This is a \n normal string')
#print(r'This is a \n raw string') # it ignores the codes like \n used to format strings

# \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
# \W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
# \s - matches whitespace, so spaces, tabs, newlines, etc.
# \S - matches everything that isn't whitespace.
# \d - is how we match any number from 0 to 9
# \D - matches anything that isn't a number.
# \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
# \B - matches anything that isn't the edges of a word.

file_path = '/Users/Cristian/Google Drive/Dropbox/Code/learning_python/Regular Expressions/names.txt'
# Open a txt file:
#--------------------------------------------------------------
# names_file is a pointer to the names.txt file on the system
names_file = open(file_path, encoding='utf-8') 
# data recieves all the content from names.txt file
data = names_file.read()
# then close the file to realease memory
names_file.close()

# use match to look for a string at the beginning of the text
print(re.match(r'Love', data))
# use search to look for a string in somewhere in the text
print(re.search(r'Kenneth', data))

# \w{3} - matches any three word characters in a row.
# \w{,3} - matches 0, 1, 2, or 3 word characters in a row.
# \w{3,} - matches 3 or more word characters in a row. There's no upper limit.
# \w{3, 5} - matches 3, 4, or 5 word characters in a row.
# \w? - matches 0 or 1 word characters.
# \w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
# \w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
# .findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.

# We have to put \ before () like that -> \( <content> \) because parenthesis have a different meaning in raw strings
print('\nLinha 48: ', re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data)) # re.search = returns the first match
print('\nLinha 49: ', re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))  # re.findall = returns all matches
    # colocar \ antes do parenteses para ser interpretado da forma certa
    # \(?   -> talvez tenha um parenteses
    # \s?   -> talvez tenha um espaço
print('\nLinha 50: ', re.findall(r'\w*, \w+', data))

# procurar por padrões especificos dentro de um conjunto de caracteres
# Set         What is macthces
# [apple]     apple
# [a-z]       any lowercase letters from a to z
# [^2]        anything that is not 2
# [-\w\d+.]   anything with '-', letters, numbers, '+', and '.' 
# [-\w\d+.]+  anything with '-', letters, numbers, '+', and '.', one or more times 

print('\nLinha 63:', re.findall(r'[-\w\d+.]+@[-\w\d+.]+', data))

# find all emails from Treehouse, LOWERCASE OR UPPERCASE
# \b to set the boundaries before and after the case
# otherwise it will find also something like 'or', 'te', 'the', etc
# {9} to look for a pattern with 9 letters long
print(r'\nLinha 66:', re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))

out1 = re.findall(r'''
    \b@[-\w\d+.]*     # first a word boundarie, a @, and then any number of characters
    [^gov\t]+           # ignore 1+ instances of 'g' 'o' or 'v' and the tab
    \b                  # match another word boundarie
    ''', data, re.VERBOSE | re.IGNORECASE)    # re.VERBOSE  to write in different lines to add coments
print('\nline 71', out1)

# find the 'last_name, first_name' and 'profession, company_name' pattern
out1 = re.findall(r'''
    \b[-\w]+,       # first a word boundary, hyphens or characters, and a comma
    \s              # find 1 whitespace
    [-\w ]+         # 1+ hyphens or characters and explicit spaces
    [^\t\n]         # ignore tabs and new lines
    ''', data, re.X | re.I)    # re.VERBOSE = re.X , and re.I = re.IGNORECASE
print('\nline 78', out1)

# Use parenthesis to return tupples with the selected patterns
# Use ?P<key> to set a key for the dictionary conversion through out.groupdict()  for the re.search method
out2 = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t            # Last Name (optional), First Name   (^ indicates the beggining of the string)
    (?P<email>[-\w\d.+]+@[-\w\d+.]+)\t         # email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone number (optional)
    (?P<job>[\w\s]+,\s[\w\s]+)\t?              # job and company (tab optional, may be a new line instead)
    (?P<twitter>@[\w\d]+)?$                    # twitter (optional)  ($ indicates de end of the string)
''', data, re.X | re.M)     # re.M = re.MULTILINE, consider each line of data separately
print('Line 88: ', out2)
print('Line 88 group dict:', out2.groupdict())

# Another way to do the same thing, but better
# create a pattern
line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t            # Last Name (optional), First Name   (^ indicates the beggining of the string)
    (?P<email>[-\w\d.+]+@[-\w\d+.]+)\t         # email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone number (optional)
    (?P<job>[\w\s]+,\s[\w\s]+)\t?              # job and company (tab optional, may be a new line instead)
    (?P<twitter>@[\w\d]+)?$                    # twitter (optional)  ($ indicates de end of the string)
''', re.X | re.M)                              # re.M = re.MULTILINE, consider each line of data separately
print('Line 101: ', line.search(data).groupdict())

# To do that for all lines:
print('\nLine 111: ')
for match in line.finditer(data):
    print(match.group('name'))
    print(match.group('phone'),'\n')

for match in line.finditer(data):
    print('{first} {last} | {email} | {phone}'.format(**match.groupdict()))   








