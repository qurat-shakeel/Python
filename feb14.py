# -*- coding: utf-8 -*-
"""feb14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rn6vQNN2BJ1FQ3UeVcY-zaN5HCCP5qAx
"""

def name(fname, lna:
    print("Hello,", fname, lname)

name("Qurat", "Shakeel")

def name(fname, mname = "Qurat", lname = "Shakeel"):
    print("Hello,", fname, mname, lname)

name("I am")

def name(one, two, three):
    print("Hello,", one, two, three)

name(two = "Insha", three = "Aisha", one = "Qurat")

def name(one, two, three):
    print("Hello,", one, two, three)

name("Qurat", "Insha", "Aisha")

def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("Qurat", "Insha", "Aisha")

def name(**name):
    print("Hello,", name["one"], name["two"], name["three"])

name(two = "Insha", three = "Aisha", one = "Qurat")

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("Qurat", "Insha", "Aisha"))

def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

# Driver Code
num = 10;
print("number: ",num)
print("Factorial: ",factorial(num))