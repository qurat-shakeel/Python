# -*- coding: utf-8 -*-
"""localandglobal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XF8mSQMEH6MgeXEKlfyPP5EgiZd3UoHX
"""

x=4
print(x)

def hello():
  print(x)
  print("hey")

hello()

x=4
print(x)

def hello():
  x=9
  print(f"the local x is {x}")
  print("hey")
print(f"the global x is {x}")   #this gets printed first
hello()
print(f"the global x is {x}")

x = 2  #global variable

def name():
  y=5 #local variable
  print(y)

name()
print(x)

x = 2  #global variable

def name():
  y=5 #local variable
  print(y)

name()
print(x)

 #print(y)  #it will cause error as y is local here and cannot be accessed outside the function



x = 2  #global variable

def name():
  global x   # changes the value of global x
  x=7
  y=5 #local variable
  print(y)

name()
print(x)