# -*- coding: utf-8 -*-
"""classes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E5tDoq4orA59xI6J-1pe4BpJt-9HMX_J
"""

class person:
  name = "qurat"
  occupation = "developer"
  networth = 10

a = person()
print(a.name)

class person:
  name = "qurat"
  occupation = "developer"
  networth = 10

a = person()
a.name = "aisha"
a.occupation = "student"
print(a.name, a.occupation)

class person:
  name = "qurat"
  occupation = "developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")
a = person()
a.info()

class person:
  name = "qurat"
  occupation = "developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")
a = person()
a.name = "aisha"
a.occupation = "student"
a.info()

class person:
  name = "qurat"
  occupation = "developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")
a = person()
b = person()
c = person()
a.name = "aisha"
a.occupation = "student"

b.name = "insha"
b.occupation = "accountant"
a.info()
b.info()
c.info()

