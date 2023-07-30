#!/usr/bin/env python
# coding: utf-8

from typing import Callable


print("type(1):\t", str(type(1)))
print("type(1.0):\t", str(type(1.0)))
print("type(\"Hi!\"):\t", str(type("Hi!")))
print("type([]):\t", str(type([])))
print("type(()):\t", str(type(())))
print("type((1, 2, 3)):", str(type((1, 2, 3))))
print("type({}):\t", str(type({})))
print("type({1, 2, 3}):", str(type({1, 2, 3})))
print("type(True):\t", str(type(True)))
print("type(len):\t", str(type(len)))
greet: Callable[[],str] = lambda : "hello world!"
print("type(greet()):\t", str(type(greet)))


# Create a new class type called Sample
class Sample:
    pass


# Instance of Sample
my_sample: Sample = Sample()
print("type(my_sample): ", type(my_sample))


class Dog:

    # Class instance Constructor / Attribute Initializer
    def __init__(self, breed: str = "dog") -> None:
        self.breed = breed

    # Method
    def identify(self) -> None:
        print("This is a", self.breed)


# Initializing the method attributes of the object instance
sam: Dog = Dog(breed="Lab")
frank: Dog = Dog("Huskie")
jim: Dog = Dog()

sam.identify()
frank.identify()
jim.identify()


class Cat:

    # Class Object Attribute (Static)
    species: str = "mammal" # A dog is always a mammal
    
    # Methods
    def __init__(self, breed: str, name: str) -> None: 
        self.breed = breed
        self.name = name
    
    def identify(self) -> str:
        return f"- Name: {self.name}\n- Breed: {self.breed}\n- Specie: {self.species}"


sammy: Cat = Cat(breed="Cat", name="Sammy")
john: Cat = Cat(breed="Dog", name="John")

john.identify()
print("---")
sammy.identify()


from typing import Final

class Circle(object):

    # Class private static attributes
    # *******************************
    # Constants: There is no constant keyword in Python, but "Final" in mypy
    # Private: Only semantic, not actually "private"
    # Set to private and use getter/No setter
    _PI: Final[float] = 3.14 # Pseudo-private, pseudo-constant

    # Constant Getters
    def PI(self) -> float:
        return Circle._PI

    # Constructor
    # ***********
    # Circles get instantiated with a radius (default = 1). 
    def __init__(self, radius: float = 1.0) -> None:
        # Private Attributes to be accessed with public methods
        self._radius = radius

    # Methods
    # *******
    def set_radius(self, radius: float) -> None:
        """
        Takes a new radius and resets the current radius of the circle instance.
        """
        self._radius = radius


    def radius(self) -> float:
        """
        Get the circle's radius.
        """
        return self._radius


    def area(self) -> float:
        """
        Calculate the circle's area.
        """
        return self.PI() * (self.radius() ** 2)  # PI * R^2
    

    def perimeter(self) -> float:
        """
        Calculate the circle's perimeter.
        """
        return 2 * self.PI() * self._radius # 2 * PI * R
    

    def __repr__(self) -> str:
        return f"Circle{{radius: {self.radius()}, perimeter: {self.perimeter()}, area: {self.area()}}}"


# Testing: Instantiation
c: Circle = Circle()
print("c.PI():", c.PI())
c.set_radius(2)
print(f"c: {c}")
print(f"Radius of c = {c.radius()}")
print(f"Area of c = {c.area()}")
print(f"Perimeter of c = {c.perimeter()}")


# Base class: Animal
# Implicit inherit from object
class Animal:
    def __init__(self) -> None:
        print("Animal created.")

    def what_am_i(self) -> str:
        return "Animal"

    def eat(self) -> str:
        return "Eating"


# Subclass of Animal: Duck
class Duck(Animal):
    # Methods
    def __init__(self) -> None:
        # Call Animal.__init(): Similar to super() in other languages
        Animal.__init__(self)
        print("Duck created.")
      
    # Overriding Animal.what_am_i()
    def what_am_i(self) -> str:
        return "Duck"

    # New methods for Ducks only    
    def quack(self) -> str:
        return "quack! quack!"


# Testing
d: Duck = Duck()
print("d.what_am_i():", d.what_am_i()) # Overridden method from Animal
print("d.eat():", d.eat()) # Inherited method from Animal
print("d.quack():", d.quack()) # Extend: New class method


# Abstract Base Class
from abc import ABC

class Animus(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Subclass of Animus must implement a speak() method")


# Then subclasses can implement this abstract base class
class ACat(Animus):
    def speak(self) -> str:
        return "{} says miaou!".format(self.name)

class ALion(Animus):
    def speak(self) -> str:
        return "{} says grawoo!".format(self.name)


# Testing
niko: ACat = ACat("Niko")
felix: ALion = ALion("Felix")

print("niko.speak():", niko.speak())
print("felix.speak():", felix.speak())


class Book(object):
    # Constructor: __init__()
    # Called with Book(title, author, pages)
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        print(f"Creating a new book: {self}") # This will call book.__str__()

    # __str__()
    # Called as the string representation: E.g. when using print(book)
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}."

    # __len__()
    # Called when using len(book)
    def __len__(self) -> int:
        return self.pages

    # __del__()
    # Called when using del(book)
    # By default, only calls "del self"
    def __del__(self) -> None:
        print("--- The book {self.title} book will be deleted")
        del self
        print("--- Deleted.")


# Testing
book: Book = Book("Python Rocks!", "Jose Calembar", 159)

# Special Methods
print("str(book):", str(book))
print("len(book):", len(book))
del(book)


