# -*- coding: utf-8 -*-
"""Loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17J05bO9zHYMl3eQbfkZC4siDzrhZ2YE-
"""

# while loop
x = 0
while (x < 3):
    x = x + 1
    print("Hello World")

# while else loop
y = 0
while (y < 3):
    y = y + 1
    print("Hello World")
else:
    print("In Else Block")

x = 0
while (x == 0):             # it is suggested not to use this loop as it is never ending (infinite loop)
    print("Hello World")

n = 4
for i in range(0, n):
    print(i)

list = ["Hello", "World"]
for index in range(len(list)):
    print(list[index])



list = ["Hello", "World"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")

#  continue statement returns the control to the beginning of the loop.
for letter in 'HelloWorld':
    if letter == 'o' or letter == 'l':
        continue
    print('Current Letter :', letter)

# Break statement brings control out of the loop.
for letter in 'HelloWorld':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

# pass statement to write empty loops
for letter in 'helloworld':
    pass
print('Last Letter :', letter)

fruits = ["apple", "orange", "kiwi"]

for fruit in fruits:

    print(fruit)