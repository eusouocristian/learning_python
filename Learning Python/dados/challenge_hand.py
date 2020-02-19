from dice import D20
class Hand(list): # extende a classe lista
    def __init__(self, size = 2, *args, **kwargs):
        super().__init__() 
        self.size = size
        for _ in range(size):
            self.append(D20())

    def __len__(self):
        return self.size

    @classmethod
    def roll(cls, size=2):
        return cls(size)

    @property   
    def total(self):
        return sum(self)
    

# >>> from challenge_hand import Hand
# >>> a = Hand.roll(5)
# >>> print(a)
# [20, 9, 9, 16, 15]
# >>> a.total
# 69

class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)
    
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)
    hand._sets
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)
    
    def score_chance(self, hand):
        return sum(hand)
    
    def score_yatzy(self, hand):
        fives = hand.count()
        return fives*10
        