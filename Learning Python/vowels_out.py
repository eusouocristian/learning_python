import os
import copy

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def desemvowel(word):
    clear_screen()
    vowels = list("aeiouAEIOU")
    word = list(word)
    vowels_out = []
    #copia a palacra digitada para outra variável
    nword = copy.copy(word)
    # remove a letra se for uma vogal
    # mas no laço for tem que estar a cópia da lista
    for letter in nword:
        if letter in vowels:
            vowels_out.append(letter)
            word.remove(letter)
    joined_no_vowels = "".join(word)
    vowels_out = "".join(vowels_out)
    return joined_no_vowels, vowels_out

clear_screen()
word = input("Retirar as vogais da palavra:\n> ")

# como input é necessário colocar a palavra como lista
# por isso foi usada a função list
no_vowels = desemvowel(word)
print("Vogais que foram retiradas: {}".format(no_vowels[1]))
print("Palavra sem as vogais: {}\n".format(no_vowels[0]))
