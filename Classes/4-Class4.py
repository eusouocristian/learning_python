# Metodos especiais 

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # permite que o resultado seja impresso na forma de texto, (print(A))
    def __str__(self):
        return 'Vector({},{})'.format(self.x,self.y)

    def __add__(self, other):
        soma = Vector(self.x + other.x, self.y + other.y)
        return soma

        
A = Vector(1,3)
B = Vector(4,-1)
print(A+B)
print(A-B)