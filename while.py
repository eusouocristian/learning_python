import sys

# usar maiusculas para constantes, no codigo
MASTER_PASSWORD = "parangari"

password = input("Type the secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Try again, it's not the right password:  ")
    attempt_count += 1
print("Welcome to secret town!")