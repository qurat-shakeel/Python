# -*- coding: utf-8 -*-
"""feb03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_2qgYCVH7yun1mO7hKgPNUdk9ngQe2FO
"""

a=3
b=2
if a==5 and b>0:
  print('a is 5 and',b,'is greater than zero.')
else:
  print('a is not 5 or',b,'is not greater than zero.')

#tuple
x = tuple()
if not x:
  print("tuple is empty")
else:
  print(x)

#ternary operator
a,b=2,5
#get maximum of a,b
max = a if a>b else b
print('Maximum :', max)

a,b=5,2
print('Python') if a > b else print('Examples')

a, b, c = 15, 93, 22

# Nested ternary operator
max = a if a > b and a>c else b if b>c else c

print(max)

