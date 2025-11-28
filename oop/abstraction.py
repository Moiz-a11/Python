
from  abc import ABC, abstractmethod

class Animal(ABC): # it is abstract class 
    @abstractmethod
    def make_sound():
        pass # show null value inside function

class Lion(Animal):
    def make_sound(self):
        print("Roar!")


class Cow:
    def make_sound(self):
        print("moo")


l1 = Lion()
l1.make_sound()

c1=Cow()
c1.make_sound()