# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:52:05 2021

@author: TARUN
"""

import calendar
year =int( input("Enter the year of the required calendar "))
month = int( input("Enter the month of the required calendar "))
print(calendar.month(year,month))
print(calendar.calendar(year))
# Checking leap year
print("Leap Year:",calendar.isleap(year))
