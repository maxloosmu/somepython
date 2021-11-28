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
