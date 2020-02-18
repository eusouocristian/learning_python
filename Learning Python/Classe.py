# Metodos especiais 
# Para testar as classes:
# Clicar com o direito sobre a pasta Learning Python  e abrir no terminal

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # permite que o resultado seja impresso na forma de texto, (print(A))
    def __str__(self):
        return 'Vector({},{})'.format(self.x,self.y)

    def __add__(self, other):
        soma = Vector(self.x + other.x, self.y + other.y)
        return soma
# from Classe import Vector
# A = Vector(1,3)
# B = Vector(4,-1)
# print(A+B)        

class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self
# from Classe import ReversedString
# Inverted = ReversedString('Hello')
# print(inverted)

class JavaScriptObject(dict): 
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:     # caso não exista a key inserida, tenta-se procurar no proprio dict
            return super().__getattribute__(item)  # caso não exista retornará um AttributeError
# import Classe
# a = Classe.JavaScriptObject({'name': 'Cristian'})       (se adiciona o dicionario)
# a.profession = 'Engineer'                               (se pode adicionar keys dessa forma)
# a.name                                                  (ira retornar 'Cristian')
# a.profession                                            (ira retornar 'Engineer')

import copy
class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count): # range(5) = [0,1,2,3,4]
            self.append(copy.copy(value)) # poderia fazer self.append(value), mas tem alguma coisa que não aprendi
# Cria uma lista, repetidos numeros ou listas iguais, por exemplo:
# FilledList(5,4) retorna [4, 4, 4, 4, 4]
# FilledList(2, [1,2,3]) retorna [[1,2,3], [1,2,3]]
# count = numero de vezes que quer repetir
# value = o que quer repetir (um numero ou uma outra lista)
# para testar:
# import Classe   (quando está extendendo str, ou int, ou dic, tem que importar a classe)
# a = Classe.FilledList(5,4)
# print(a)

# Classe que altera o valor do tamanho de uma lista
class Liar(list):
    def __len__(self):
        return super().__len__() + 10

# import Classe
# a = Classe.Liar([1,2,3])
# len(a)              (devera retornar 13)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
    
class Bookcase:
    def __init__(self, books=None):   #self, and a list of books, none as default value
        self.books = books

    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)














