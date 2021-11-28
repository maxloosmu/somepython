#!/usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name}, {self.age} years old"
class PersonWithPhone(Person):
    def __init__(self, name, age, phone):
        super().__init__(name, age)
        self.phone = phone
    def phoneNum(self):
        print(f"Phone Number: {self.phone}")
class PersonWithSecondPhone(PersonWithPhone):
    def __init__(self, name, age, phone, secondPhone):
        super().__init__(name, age, phone)
        self.secondPhone = secondPhone
    def secondPhoneNum(self):
        print(f"Second Phone Number: {self.secondPhone}")
jonathon = PersonWithSecondPhone("Jon", 8, 1111, 2222)
jonathon.secondPhoneNum()
jonathon.phoneNum()
print(jonathon)
