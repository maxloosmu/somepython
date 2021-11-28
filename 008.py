#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_name_age(self):
        print(f"{self.name}, {self.age} years old")
class PersonWithPhone(Person):
    def __init__(self, name, age, phone):
        super().__init__(name, age)
        self.phone = phone
    def phone_num(self):
        print(f"Phone Number: {self.phone}")
class PersonWithSecondPhone(PersonWithPhone):
    def __init__(self, name, age, phone, second_phone):
        super().__init__(name, age, phone)
        self.second_phone = second_phone
    def second_phone_num(self):
        print(f"Second Phone Number: {self.second_phone}")
jonathon = PersonWithSecondPhone("Jon", 8, 1111, 2222)
jonathon.second_phone_num()
jonathon.phone_num()
jonathon.print_name_age()

