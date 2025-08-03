from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk")
class snake(animal):
    def move(self):
        print("I can slither")
class lizard(animal):
    def move(self):
        print("I can crawl")
class whale(animal):
    def move(self):
        print("I can swim")

a=human()
a.move()

b=snake()
b.move()

c=lizard()
c.move()

d=whale()
d.move()