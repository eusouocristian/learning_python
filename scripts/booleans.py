# pode-se usar texto 'and', 'not', 'or' e o texto True and False 

is_smoker = True
has_kids = True
question = is_smoker and not has_kids
print(question)

# A função bool() avalia se o argumento é True or False
# qualquer string que não seja vazia é True
# Qualquer número que não seja zero é True
bool("")      # True
bool("abcd") # True
bool(0)     # False
bool(1)    # False
