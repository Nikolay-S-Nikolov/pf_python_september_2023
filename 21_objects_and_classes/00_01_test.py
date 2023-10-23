class Person:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person("Nikolay", 44)
you = Person("Maria", 37)
print(me.species)
print(you.species)
