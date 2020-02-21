# transforma um numero de input em string, e possibilita fazer operações matematicas com o string

class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
      
    def __radd__(self, other):
        return self + other
    
    # x += y is equivalent to x = x.__iadd__(y)
    def __iadd__(self, other):
        self.value = self + other
        return self.value
    
    def __mul__(self,other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other
    
    def __rmul__(self,other):
        return self * other

five = NumString(5)
print('five: ', five)
print('type(five): ', type(five))
print('five + 5: ', five + 5)
print('5 + five: ', 5 + five)
print('five * 3: ', five * 3)
print('3 * five: ', 3 * five)