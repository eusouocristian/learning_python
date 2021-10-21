from dataclasses import dataclass, field

# Decorator for dataclass with sorting by age
@dataclass(order=True)
class Person:
    sort_index: int=field(init=False, repr=False)
    name: str
    job: str
    age: int
    strenght: int = 100

    # Here the definition of sorting is set
    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.age)

    def __str__(self):
        return f'{self.name}, {self.job}, strenght is ({self.strenght})'



person1 = Person("Gerald", "Witcher", 30, 99)
person2 = Person('Yennefer', 'Sorceress', 25)
person3 = Person('Yennefer', 'Sorceress', 25)

print(id(person2))
print(id(person3))
print(person1)

# Check if person1 is older than person2
print(person1 > person2)