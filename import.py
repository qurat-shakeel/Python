# -*- coding: utf-8 -*-
"""import.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQJ_q5tCdVdXAqTQwKuXFtaMxDyQ_E0c
"""

import math
result = math.sqrt(9)
print(result)

import math
result = math.floor(4.2343)
print(result)

from math import sqrt, pi
result = sqrt(16) * pi
print(result)

from math import *   #importing everything, (not recommended)

result = sin(90)
print(result)

from math import sqrt as s
result = s(25)
print(result)

import math as m
result = m.sqrt(64)
print(result)

import math
print(dir(math))

print(math.nan, type(math.nan))

def welcome():
  print("Hey you are welcome my friend")

harry =  "A good boy"
welcome()
print(harry)