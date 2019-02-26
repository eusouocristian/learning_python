def disemvowel(word):
    word = list(word)
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for vowel in word:
        if vowel in vowels:
            word.remove(vowel)
        else:
            pass
    return word

word = input("Ditite uma palavra:\n>")
new_word = disemvowel(word)
print(new_word)
