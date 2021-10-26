#!/usr/bin/env python3
"""2016 Data Visualization with Python and JavaScript
Chapter 2"""

from collections import Counter, defaultdict, OrderedDict

items = ['F', 'C', 'C', 'A', 'B', 'A', 'C', 'E', 'F']
cntr = Counter(items)
print(cntr)

d = defaultdict(int)
for item in items:
    d[item] += 1
print(d)
print(d.items())
print(sorted(d.items()))

# lambda function, as used for key, chooses the second element of tuple in `d.items()` for sort
print(sorted(d.items(), key=lambda x : x[1]))
e = OrderedDict(sorted(d.items(), key=lambda x : x[1]))
print(e)

