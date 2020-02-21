def sillycase(string):
    length = len(string) // 2
    if len(string) % 2 == 0:
        output = string[:length].lower() + string[-length:].upper()
    elif len(string) % 2 != 0:
        output = string[:length].lower() + string[-1-length:].upper()
    print(output)
    return output

sillycase(input("Digite uma palavra: > "))