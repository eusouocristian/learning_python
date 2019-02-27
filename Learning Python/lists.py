import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

temperatures = []
# Adicionar valores a lista
temperatures.append(1) 
temperatures.append(2)
temperatures.append(3)

# concatenar listas
err_temp = [4 , 5, 6]
temperatures.extend(err_temp)
print(temperatures)

# concatenar usando o simbolo +
doctors_list = ["DocA", "DocB"]
doctors_list2 = ["DocC","DocD"]
all_doctors = doctors_list + doctors_list2
print(all_doctors)

# Indexing 
books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]
# acessar o ultimo item da lista
print(books[-1])
# acessar o penultimo item da lista
print(books[-2])
# Inserir um item na lista, sem modificar os demais
books.insert(0, "Learning Python: Powerful Object-Oriented Programing")
# Concatenar conteúdo a um dos elementos
books[0] += " - Mark Lutz"
print("\n",books)

new_list = ["books", "beer","internet"]
# metodo .append() insere o conteudo integralmente a lista
new_list.append("chocolate")
# metodo .extend() insere o conteudo de forma iterativa na lista, um a um
new_list.extend("sex")
# metodo .insert() insere um objeto no indice desejado
new_list.insert(0,"bola")
print("\n",new_list)

lista = ["a","b","c","d","e"]
# deletar item da lista pelo indice (deletando item 'b', indice 1)
del lista[1] 
print("lista linha 47: {}".format(lista))

# pop(index) retira um item da lista e retorna o item retirado
# se não colocar nenhum argumento, ele retira o ultimo item da lista
pop_variable = lista.pop(0)
print("Pop_variable: {}".format(pop_variable))
print("lista linha 51: {}".format(lista))

# remove() remove o item desejado, mas para quando encontra o primeiro item na lista
lista.remove("e")
print("lista linha 56: {}".format(lista))






