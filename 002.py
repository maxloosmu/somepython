#!/usr/bin/env python3
"""https://sebhastian.com/list-comprehension-javascript/
"""

pets = ["cat", "bird", "fish", "dog"]
petsWithD = [pet for pet in pets if "d" in pet]
print(petsWithD)
# ['bird', 'dog']

morePets = [pet+"s" for pet in petsWithD]
print(morePets)
# ['birds', 'dogs']

birdsAndDogs = [pet+"s" for pet in pets if "d" in pet]
print(birdsAndDogs)
# ['birds', 'dogs']


