# str() --> WhateverType.__str__()
from abc import ABC, abstractmethod


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        ...

class Bird(Flyable):
    def fly(self):
        print("Woosh woosh fly")


class Plane(Flyable):
    def fly(self):
        print("Zhroom Bzzz SHHHH")


class Chicken:
    ...


def go_flying(thing: Flyable):
    thing.fly()


go_flying(Bird())
go_flying(Plane())
go_flying(Chicken())