import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

# Criar um dictionary com as relativas =>>   keys: Values
cristian = {"first_name": "Cristian", "job": "Field Technician"}
print(cristian,"\n")

# Incluir keys a um dictionary
cristian["last_name"] = "F Santos"
print(cristian,"\n")

# alterar valores de Keys e acrescentar outras keys
cristian.update({"job": "Field Operation Techinican","Company": "Petrobras"})
print(cristian,"\n")

# deletar keys de um dictionary
del cristian["job"]
print(cristian,"\n")

# Criar um dictionary com as relativas keys
# um dictionary para uma key especifica. Em education, podemos ter um dictionary conforme abaixo:
cristian = {"first_name": "Cristian", "job": "Field Technician","education": {"graduate": "Electric Eng","Masters": True}}
print(cristian["education"]["graduate"],"\n")

input("Enter para continuar: > ")

# Cria um pack de variáveis
def packer(name = None, **kwargs):
    print("kwargs:", kwargs)

packer(name="Cristian", idade = 32, weigth = 80)

# Unpack as variaveis do pack
# Inicia as variaveis como None, e depois recebe o argumento quando a função é chamada  
def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print("Hi, {} {}!".format(first_name,last_name))
    else:
        print("Hi, no name!")

unpacker(**{"first_name": "Cristian","last_name": "F Santos"})