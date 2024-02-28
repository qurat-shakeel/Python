# -*- coding: utf-8 -*-
"""map.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZDUxaNa5q-mM5xR1VxxJ8fY-qxvYIRMW
"""

def cube(x):
  return x*x*x
print(cube(2))

def cube(x):
  return x*x*x
print(cube(2))
l = [1,2,4,6,4]
newl = []
for item in l:
  newl.append(cube(item))
print(newl)

#map
def cube(x):
  return x*x*x

print(cube)

l = [1,2,4,6,4,3]
newl = list(map(cube,l))
print(newl)

l = [1,2,4,6,4,3]
newl = list(map(lambda x:x*x*x,l))
print(newl)

# filter
def filter_funct(a):
  return a>2

newnewl = list(filter(filter_funct,l))
print(newnewl)

#reduce
from functools import reduce

num = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y,num)
print(sum)