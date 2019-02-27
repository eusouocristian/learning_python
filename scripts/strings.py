quote = "A person who never failed never tried something new"
quote.upper()
quote.lower()
quote.title()
    #   \
# argumentos relacionados a strings
# help(str)


# usar o 'method' .format para completar strings
# method é uma função que pertence a cada objeto, podendo ser acessado através de um ponto.
subject_sample = "Thanks for learning {} with us, {}"
subject_sample = subject_sample.format("Python","Cristian")
print(subject_sample)

# The number of characters os a string
number_of_char = len(subject_sample)
number_of_char_phrase = "The number of chars is {}"
print(number_of_char_phrase.format(number_of_char))



