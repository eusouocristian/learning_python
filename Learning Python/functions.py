import math

# Função que faz a divisão da conta do bar pelo numero de pessoas na mesa
def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

total_due = float(input("What is the total?  "))
number_of_people = int(input("How many people? "))
amount_due = split_check(total_due,number_of_people)

print("Each person owes ${} ".format(amount_due))
# nesse ponto a função retornaria $21.2425 se não fosse a função math.ceil

