# -*- coding: utf-8 -*-
"""Feb04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ta76Mc1Vohy41ALY7uIJcmi4FIHUZkTs
"""

string1 = "Apple"
string2 = "Banana"

result = string1 +" "+ string2
print(result)

string1 = "Apple"
string2 = "Banana"
string3 = "Cherry"
string4 = "Mango"

result = string1 +" "+ string2 +" "+ string3 +" "+ string4
print(result)

#sort list in ascending order
my_list = ['cherry', 'mango', 'apple', 'orange', 'banana']
my_list.sort()
print(my_list)

# copy and sort
my_list = ['cherry', 'mango', 'apple', 'orange', 'banana']
my_list.copy()
sorted_list=my_list.copy()
sorted_list.sort()
print(my_list)
print(sorted_list)

# sort in descending order
my_list = ['cherry', 'mango', 'apple', 'orange', 'banana']
my_list.sort(reverse=True)
print(my_list)

#convert str to lower case
mystring = 'Hello World'
print('Original String :',mystring)

lowerstring = mystring.lower()
print('Lowercase String :',lowerstring)

# trim white spaces from edges
mystring = '   Hello world        '

cleanstring = mystring.strip()

# Before strip
print(mystring)
print(len(mystring))

# After string
print(cleanstring)
print(len(cleanstring))

# convert string to integer
# Take a string
a = '125'
print('Input', a, type(a))

# Convert string to int
output = int(a)
print('Output', output, type(output))

# Convert binary str to integer
# Take a binary string
a = '10111010'
print('Input', a, type(a))

# Convert binary string to int
output = int(a, base=2)
print('Output', output, type(output))

# Convert Hex str to int
# Take a hex string
a = 'AB96210F'
print('Input', a, type(a))

# Convert hex string to int
output = int(a, base=16)
print('Output', output, type(output))