# -*- coding: utf-8 -*-
"""feb12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18-U5kEDyxGuybbliFcJ3jB8aywlWVkWc
"""

import time;
#prints the number of ticks spent since 12 AM, 1st January 2020
print(time.time())

import time;

#returns a time tuple

print(time.localtime(time.time()))

import time
  #returns the formatted time

print(time.asctime(time.localtime(time.time())))

import datetime
#returns the current datetime object
print(datetime.datetime.now())

import calendar;
cal = calendar.month(2024,2)
#printing the calendar of December 2018
print(cal)

import calendar
#printing the calendar of the year 2024
s = calendar.prcal(2024)

