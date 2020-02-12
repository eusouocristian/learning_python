# transform Morse Code into typed Morse Code, i.e. '.' '.' '.' => dot-dot-dot

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
        
    def __str__(self):
        typed_pattern = []
        for item in self.pattern:
            if item == '.':
                typed_pattern.append('dot')
            if item == '_':
                typed_pattern.append('dash')
        return '-'.join(typed_pattern)
    

class S(Letter):
    def __init__(self):
        pattern = ['_', '.', '_']
        super().__init__(pattern)

esse = S()
print(str(esse))