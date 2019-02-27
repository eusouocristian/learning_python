books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]
video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

def display_wishlist(display_name,wishes):
    items = wishes.copy()
    print(display_name + ":")
    suggested_gift = items.pop(0)
    print("====>", suggested_gift,"<====")
    for item in items:
        print("* " + item)
print()



print("Books:")
for item in books:
    print("* " + item)

print("\nsuggested gift: {}\n".format(books[0]))

gift = books[0]
suggestion = gift

# Deleta um objeto, ou um item da lista
del gift
# poderia usar ->  del books[0] 

try:
    print(gift)
except NameError:
    print("The variable named as {} has been deleted".format("'gift'"))

# Apaga itens da lista (do ultimo para o primeiro) 
books.pop()
print("\n", "line 25")
for item in books:
    print(item)

# Apaga itens da lista do indice relacionado
books.pop(0)
print("\n", "line 31")
for item in books:
    print(item)

# Para apagar items de uma lista => lista.remove('index')
# para apagar todos os items, tem que comparar com a copia da lista
# caso contrário não irá apagar todos os items da lista
for item in books.copy():
    books.remove(item)
print("Linha 59 e 60")
print(books)

quote = "The greatest teacher failure is"
words = quote.split()
print("Line 65\n",words)

# Unir cada uma das palavras que foram separadas novamente em um string unico
# Com uma virgula entre cada uma
join = ", ".join(words)
print("Line 70\n", join)

# Separar o string em uma lista
# A separação ocorre a cada ", "
unjoin = join.split(", ")
print("Line 74\n", unjoin)

