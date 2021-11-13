#!/usr/bin/env python3
"""
2021 Python Distilled
Section 3.3 Loops and Iteration
"""

my_list = [(1,2), (3,4)]
for x, y in my_list:
    print(x, y)

i = 2
while (i > 0):
   print(i)
   i -= 1


"""
The code below don't work well,
unlike what has been proclaimed in the book.
"""
with open('z.txt') as file:
    for line in file:
        print(line)
        if line == "Missing section separator":
            break
    else:
        raise RuntimeError('Missing section separator')

my_list2 = [(1,2), (3,4), (False,None)]
for x, y in my_list2:
    print(x, y)
else:
    print("None found")
