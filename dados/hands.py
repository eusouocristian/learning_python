from dice import D6

class Hand(list): # extende a classe lista
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        
        if not die_class:
            raise ValueError("You Must provide die class!")
        super().__init__() 
        
        # cria uma lista com tamanho=size, com o return da da classe die_class, nesse caso, die.D6
        for _ in range(size):
            self.append(die_class())
        self.sort() 

# função que cria uma lista pronta de 5 posições com valores sorteados
class YatzyHand(Hand):
    def __init__(self, size=5, *args, **kwargs):
        # sobrescreve __init__ com size=5 e die_class=6, tem que importar D6 no começo do código
        super().__init__(size=size , die_class=D6, *args,**kwargs)

    
# import dice, hands
# h = hads.Hand(size=5, die_class=dice.D6)
# for _ in h:
#       print(int(h[_]))
# h deverá conter uma lista com tamanho=size, cada item com um valor sorteado 

# from hands import YatzyHand
# yh = YatzyHand()         
# yh      >> deverá retornar uma lista de tamanho 5, com numeros sorteados de um dado de 6 lados


