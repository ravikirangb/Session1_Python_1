# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:15:36 2018

@author: 1000091

Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
"""
import sys, os
Name = input ("First Name:" )
SurName = input("SurName:")

FullName = (Name + " " + SurName)
print (''.join(reversed(FullName)))