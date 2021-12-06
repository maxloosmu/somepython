#!/usr/bin/env python3
"""
2021 Python Distilled
Chapter 7 Classes and Object-Oriented Programming
"""
import time

# https://stackoverflow.com/questions/33097143/what-is-the-difference-between-r-and-r-in-python
# https://stackoverflow.com/questions/9455111/define-a-method-outside-of-class-definition/9455442
# https://realpython.com/inheritance-composition-python/

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __repr__(self):
        return f'{type(self).__name__}({self.owner!r}, {self.balance!r})\
            \n {type(self).__name__}({self.owner!s}, {self.balance!s})\
            \n{type(self).__name__}({self.owner}, {self.balance})'
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def inquiry(self):
        return self.balance
    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext('owner'), \
            float(doc.findtext('amount')))
data = '''
<account>
    <owner>Guido</owner>
    <amount>1000.0</amount>
</account>
'''
class EvilAccount(Account):
    pass
c = Account.from_xml(data)
d = EvilAccount.from_xml(data)
print(c)
print(d)
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
class Date:
    datefmt = '{year}-{month:02d}-{day:02d}'
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return self.datefmt.format(year=self.year,\
            month=self.month, day=self.day)
@classmethod
def from_timestamp(cls, ts):
    tm = time.localtime(ts)
    return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)
@classmethod
def today(cls):
    return cls.from_timestamp(time.time())
class MDYDate(Date):
    datefmt = '{month}/{day}/{year}'
class DMYDate(Date):
    datefmt = '{day}/{month}/{year}'
e = Date(1967, 4, 9)
f = MDYDate(1967, 4, 9)
g = DMYDate(1967, 4, 9)
print(e) # 1967-04-09
print(f) # 4/9/1967
print(g) # 9/4/1967



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
"""
d = Dog()
print('')
bat = NonMarineMammal('Bat')
print('')
print(Dog.__mro__)
"""

def must_use_keyword(a, *, b):
    return a + b
print(must_use_keyword(1, b=2))


