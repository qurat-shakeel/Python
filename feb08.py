# -*- coding: utf-8 -*-
"""feb08.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bp1gdoD0ZnGE2XITca5uu6Prvyo_Z96l
"""

# implicit conversion --- Automatic type conversion
# Converting integer to float
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

# Explicit conversion  --- Manual type conversion

# Addition of string and integer Using Explicit Conversion

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

