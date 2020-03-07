def rememberer(thing):
    # with é usado para abrir o arquivo, e não é necessario fazer file.close()
    with open('database.txt', 'a') as file:
        # 'a' habilita gravação. Se o arquivo não existir, é criado um
        # 'w' zera o conteudo antes de escrever
        # 'a' acrescenta o conteudo mantendo o que tinha anteriormente
        file.write(thing+'\n')
        

if __name__ == '__main__':
    rememberer(input('What should I remember? '))

