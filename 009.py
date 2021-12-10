#!/usr/bin/env python3
# https://stackoverflow.com/questions/59735826/create-immutable-object-in-python


class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    @property
    def my_age(self):
        return self.__age
    @my_age.setter
    def my_age(self, age):
        self.__age = age
    @classmethod
    def any_name_age(cls, value):
        return cls(value, value)
    @classmethod
    def nil_name_age(cls):
        return cls.any_name_age(0)
    def add_age(self, years):
        self.__age += years
        return self
luke = Person("Luke", 25)
print(luke._name)
print(luke._Person__age)
luke._Person__age = 29
print(luke.get_age())
luke.set_age(44)
print(luke.get_age())
luke.my_age = 35
print(luke.my_age)
new_person = Person.nil_name_age()
print(new_person._name, new_person.my_age)
new_person._Person__age = 5
new_person2 = new_person.add_age(10)
print(new_person2.my_age)


