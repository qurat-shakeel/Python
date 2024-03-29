# -*- coding: utf-8 -*-
"""dict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oxAj9gvoDkF-JDThjxgpOO9C38V4C_QB
"""

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# print all the values using values mmethod
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# print all the key-value pairs in the dictionary using items() method.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

#  to add items to a dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info['DOB'] = 2001
print(info)

#  update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# to remove items from dictionary.


info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = info.copy()
print(newDictionary)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
newDictionary = dict(info)
print(newDictionary)