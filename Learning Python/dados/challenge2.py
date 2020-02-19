from dice import D6

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()
        
        for _ in range(size):
            self.append(die_class())
        self.sort()
        
    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice


class CapitalismHand(Hand):
    def __init__(self, size=2, die_class=D6):
        super().__init__(size=2,  die_class=D6)
        
    @property
    def ones(self):
        return self._by_value(1)
    
    @property
    def twos(self):
        return self._by_value(2)
    
    @property
    def threes(self):
        return self._by_value(3)
    
    @property
    def fours(self):
        return self._by_value(4)
    
    @property
    def fives(self):
        return self._by_value(5)
    
    @property
    def sixes(self):
        return self._by_value(6)
    
    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
    
    @property
    def doubles(self):            
        if self[0] == self[1]:
            return True
        else:
            return False
    
    @classmethod
    def reroll(cls):
        return cls()
        
    
    
    