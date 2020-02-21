def combiner(lista):
    soma = 0
    lista_output = []
    for item in lista:
        if isinstance(item, (int,float)):
            soma += item
        if isinstance(item, str):
            lista_output.append(item)
    soma_str = str(soma)
    lista_output.append(soma_str)
    lista_output = [''.join(lista_output)]
    return lista_output[0]

result = combiner(['a',1,'bc',2,'cde',3])
print(result)