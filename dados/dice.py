import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError('Must have at least 2 sides')
        if not isinstance(sides, int):
            raise ValueError('Sides must be an integer number')
        self.value = value or random.randint(1, sides)
    
    def __int__(self):
        return self.value
    
    def __eq__(self, other):
        return int(self) == other
    
    def __ne__(self, other):
        return int(self) != other
    
    def __gt__(self, other):
        return int(self) > other
    
    def __lt__(self, other):
        return int(self) < other
    
    def __ge__(self, other):
        return int(self) >= other
    
    def __le__(self, other):
        return int(self) <= other
    
    def __add__(self, other): # D6 + 5
        return int(self) + other
    
    def __radd__(self, other): # 5 + D6
        return int(self) + other
    
    def __repr__(self): 
        return str(self.value)

class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value = value)

class D20(Die):
    def __init__(self, value=0):
        super().__init__(sides=20, value = value)
    

# from dice import D6
# dado = D6()
# int(D6)
# D6 > 3    ?
# D6 <= 4   ?
# ...

# Teacher Notes:
# If you want to get a lot of magic method goodies easily, 
# check out attrs. It's a solid library and makes a lot of common usages much easier.
# https://www.attrs.org/en/stable/
# Or, to stick with the standard library, check out the docs for functools.total_ordering. 
# You need to define __eq__ and then one of the other operations and Python will figure out the rest.
# https://docs.python.org/3/library/functools.html#functools.total_ordering