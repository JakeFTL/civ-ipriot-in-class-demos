class Cat:
    def __init__(self, name, age, coat_colour):
        self.name = name
        self.age = age
        self.coat_colour = coat_colour

    def meow(self):
        print(f'{self.name} says "Meow".')

    def purr(self):
        print(f'{self.name} purrs.')

    def meet(self, other):
        if isinstance(other, Dog):
            print(f'{self.name} hisses at {other.name}')
    pass


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{dog.name} says "Woof, Woof!"')

    def meet(self, other):
        if isinstance(other, Dog):
            print(f'{self.name} wags their tail at {other.name}')
        elif isinstance(other, Cat):
            print(f'{self.name} barks at {other.name}')
    pass

# cat = Cat()
# print(type(cat))
#
# cat.name = "Lenny"
# cat.age = 3


cat = Cat("Whiskers", 3, "Orange")
print(cat.name)
print(cat.age)
print(cat.coat_colour)

cat2 = Cat("Lenny", 3, "White")
cat2.meow()
cat2.purr()

dog = Dog("Gary", 5)
print(dog.name)
print(dog.age)
dog.bark()

dog2 = Dog("Barry", 3)

cat2.meet(dog)
dog.meet(dog2)
dog.meet(cat2)
