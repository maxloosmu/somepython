#!/usr/bin/env python3
"""
https://docs.python.org/3/library/functions.html#dir
https://www.programiz.com/python-programming/methods/built-in/dir

"""
list_object = [1,2,3]
print("dir(list_object) shows:")
print(dir(list_object))
print("dir() shows:")
print(dir())

class NewSelfCreatedObject:
    def __dir__(self):
        return ['A', 'B', 'C']
new_object = NewSelfCreatedObject()
print("dir(new_object) shows:")
print(dir(new_object))

