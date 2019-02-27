import math

# Função que faz a divisão da conta do bar pelo numero de pessoas na mesa
def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the total?  "))
    number_of_people = int(input("How many people? "))
    amount_due = split_check(total_due,number_of_people)
except ValueError as error:
    print("Oh no! That's not a valid number! Try again")
    print("({})".format(error))
else:
    print("Each person owes ${} ".format(amount_due))


# nesse ponto a função retornaria $21.2425 se não fosse a função math.ceil

    else:
        raise NameError("Please try again with only Y or N, ok? ")
except NameError as error:
    print("Oh no! That's not a valid answer!")
    print("({})".format(error))