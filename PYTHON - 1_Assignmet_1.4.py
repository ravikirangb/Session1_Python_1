# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:28:37 2018

@author: 1000091

Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3
NOTE: The solution shared through Github directory should contain the source
code used and screenshot of the output.

"""

import os,sys
import math
SDia = 12

SVolume = (4 / 3) * math.pi * ((SDia / 2) ** 3) 
print("The volume is:",SVolume)
print("The volume rounded upto 2 decimal::",round(SVolume,2))