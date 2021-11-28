#!/usr/bin/env python3
"""
2021 Python Distilled
Chapter 7 Classes and Object-Oriented Programming
"""

# https://stackoverflow.com/questions/33097143/what-is-the-difference-between-r-and-r-in-python
# https://stackoverflow.com/questions/9455111/define-a-method-outside-of-class-definition/9455442
# https://realpython.com/inheritance-composition-python/

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __repr__(self):
        return f'Account({self.owner!r}, {self.balance!r})\
            \n Account({self.owner!s}, {self.balance!s})\
            \nAccount({self.owner}, {self.balance})'
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def inquiry(self):
        return self.balance
a = Account("aaa", 111)
b = Account("bbb", 222)
"""
print(a)
print(b)
print(vars(a))
print(vars(b))
print(type(a))
print(type(b))
print(type(a.deposit))
print(type(b.deposit))
print(type(a).deposit)
print(type(b).deposit)
"""

# https://www.programiz.com/python-programming/methods/built-in/super

class Animal0(object):
    def __init__(self, animal_type):
        print('Animal Type:', animal_type)
class Mammal0(Animal0):
    def __init__(self):
        # call superclass
        super().__init__('Mammal')
        print('Mammals give birth directly')
# this code prints only when it initialises/constructs
# Animal and Mammal objects
dog = Mammal0()

class Mammal1(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
class Dog1(Mammal1):
    def __init__(self):
        print(f'{type(self).__name__} has four legs.')
        # Mammal.__init__(self, 'Dog')
        super().__init__('Dog')
# this code is similar to the previous
d1 = Dog1()
print('')

class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');

class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)

class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')

d = Dog()
print('')
bat = NonMarineMammal('Bat')
print('')
print(Dog.__mro__)
