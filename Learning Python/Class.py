class Student:
    name = "Cristian"
    
    # method para inicialização 
    def __init__(self, name, **kwargs):
        self.name = name
        # descompacta kwargs em tuples (key, value)
        for key, value in kwargs.items():
            # função que atribui atributos a classe Student (no caso, 'self')
            setattr(self,key,value)
    
    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()

# No terminal, iniciar python3, e carregar a classe digitando 
# >> from Class import Student

# Criar uma instancia para copiar a classe, por exemplo 'Cristian'
# com o argumento 'nome' conforme a linha 5
# >> Cristian = Student('Cristian')

# Para rodar o method, digitar no teminal:
# >> Cristian.praise()
# >> Cristian.reassurance()
#  >> Cristian.feedback(10)      # Colocar a nota como argumento 