# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 17:20:19 2018

@author: 1000091

Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be
printed in a comma-separated sequence on a single line.
"""

list = range(2000,3200) 
result = filter(lambda x: x % 7 == 0 and x % 5 != 0, list)
result = (str(x) for x in result)

print(",".join(result))