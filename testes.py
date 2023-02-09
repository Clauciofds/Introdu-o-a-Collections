from operator import attrgetter


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


people = [Person("John", 30), Person("Jane", 25), Person("Jim", 35)]

# Ordenar a lista de pessoas pelo atributo 'idade'
people.sort(key=attrgetter('age'))
print(people)
# [Person(name=Jane, age=25), Person(name=John, age=30), Person(name=Jim, age=35)]
