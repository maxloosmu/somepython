#!/usr/bin/env python3
""" JavaScript's Switch Expression and Python's Dictionary Switch Hack
https://www.dummies.com/programming/python/how-to-replace-the-switch-statement-with-a-dictionary-in-python/
"""

def get_cat():
    print("You got a cat!")
def get_dog():
    print("You got a dog!")
def get_bird():
    print("You got a bird!")

get_pet = {
    1 : get_cat,
    2 : get_dog,
    3 : get_bird
}

get_pet_list = [get_cat, get_dog, get_bird]

select_pet = 1
if (select_pet < 1 or select_pet >3 ):
    print("You got no pet!")
else:
    get_pet[select_pet]()
    get_pet_list[select_pet]()

if (select_pet == 1):
    print("You got a cat!")
elif (select_pet == 2):
    print("You got a dog!")
elif (select_pet == 2):
    print("You got a bird!")
else:
    print("You got no pet!")