class Student:    

    # method para inicialização 
    def __init__(self, name, **kwargs):
        self.name = name
        # descompacta kwargs em tuples (key, value)
        for key, value in kwargs.items():
            # função que atribui atributos a classe Student (no caso, 'self')
            setattr(self,key,value)
    
    def praise(self):
        print("You inspire me, {}".format(self.name))
    
    def reassurance(self):
        print("Chin up, {}. You'll get it next time!".format(self.name))
    
    def feedback(self, grade):
        if grade > 50:
            print('You got a great score, {}'.format(self.name))
            return self.praise()
        return self.reassurance()

# No terminal, iniciar python3, e carregar a classe digitando 
# >> from Class import Student

# Criar uma instancia para copiar a classe, por exemplo 'Cristian'
# com o argumento 'nome' conforme a linha 5
# >> Cristian = Student('Cristian')

# Para rodar o method, digitar no teminal:
# >> Cristian.feedback(10)      # Colocar a nota como argumento 

class Eu(Student):
    # method para inicialização, nesse caso sobrepõe o método __init__ da superclasse 'Student'
    def __init__(self, name, **kwargs):
        super().__init__(name) 
        self.name = name
        # descompacta kwargs em tuples (key, value)
        for key, value in kwargs.items():
            # função que atribui atributos a classe Student (no caso, 'self')
            setattr(self,key,value)

    def praise_Cristian(self):
        # super() faz com que sejam executados métodos da superclasse, nesse caso, 'Student'
        super().praise()
    
    def feedback(self, grade):
        super().feedback(grade)

Cristian = Eu('Cristian', age = 33)
Cristian.praise_Cristian()
Cristian.feedback(55)

Cristian.__class__
Cristian.__class__.__name__

