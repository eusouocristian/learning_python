import re

data = '1-Cristian Figueiredo dos Santos2'


data1 = 'kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk'

def first_number(data):
    search = re.match(r'\d', data)
    return search

print(first_number(data))


def find_emails(data):
    output = []
    mails = re.findall(r'[-\w\d+.]*@[-\w\d+.]+', data, re.IGNORECASE)
    for mail in mails:
        output.append(mail)
    return output

string = 'Perotto, Pier Giorgio'
names = re.match(r'([\w]*),\s([\w ]+)', string)
print(names)

# Create a new variable named contacts that is an re.search() 
# where the pattern catches the email address and phone number 
# from string. Name the email pattern email and the phone number 
# pattern phone. The comma and spaces * should not* be part of 
# the groups.

datas = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

# contacts = re.search(r'''
#     ^(?P<email>[-\w\d.+]+@[-\w\d+.]+)
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?$
# ''', string, re.M | re.X)
contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d+.]+)
    ,\s(?P<phone>\d{3}-\d{3}-\d{4}),\s
    ''', datas, re.M | re.X)
print(contacts.groupdict())

# Great! Now, make a new variable, twitters that is an re.search() 
# where the pattern catches the Twitter handle for a person. 
# Remember to mark it as being at the end of the string. 
# You'll also want to use the re.MULTILINE flag.

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

twitters = re.search(r'''
    @[\w\d]+$   
''', string, re.M|re.X)
print(twitters)

# Create a variable named players that is an re.search() 
# or re.match() to capture three groups: 
# last_name, first_name, and score. 
# It should include re.MULTILINE.

string = '''
Love, Kenneth: 20
Stewart Pinchback, Pinckney Benton: 18
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
'''

players = re.search(r'''
    ^(?P<last_name>\w+\s?\w+?)
    ,\s(?P<first_name>\w+\s?\w+)
    :\s(?P<score>\d+)
''', string, re.M | re.X)

print(players)
print(players.groupdict())

lista = '1234567890'
print(re.match(r'\d{1,}', lista)) # {1,} = 1    or more 
