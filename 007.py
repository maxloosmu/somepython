#!/usr/bin/env python3
'''
https://realpython.com/inner-functions-what-are-they-good-for/
'''

greet = "global hello"
n = 999
def layer1Greet():
  greet = "layer 1 local hello"
  n = 0
  def layer2Greet():
    greet = "layer 2 local hello"
    def link():
      return
    def count():
      nonlocal n
      n += 1
      return (f"{n} {greet}")
    def globalCount():
      global n
      n += 2
      return (f"{n} {greet}")
    def reset():
      n = 0
      return (f"{n} {greet}")
    link.count = count
    link.globalCount = globalCount
    link.reset = reset
    return link
  return layer2Greet
greet1 = layer1Greet()()
greet2 = layer1Greet()()
print(greet1.count())       # 1 layer 2 local hello
print(greet1.globalCount()) # 1001 layer 2 local hello
print(greet1.count())       # 2 layer 2 local hello
print(greet1.count())       # 3 layer 2 local hello
print(greet1.reset())       # 0 layer 2 local hello
print(greet1.count())       # 4 layer 2 local hello
print(greet1.globalCount()) # 1003 layer 2 local hello
print(greet2.count())       # 1 layer 2 local hello
print(greet2.count())       # 2 layer 2 local hello
print(greet1.count())       # 5 layer 2 local hello

