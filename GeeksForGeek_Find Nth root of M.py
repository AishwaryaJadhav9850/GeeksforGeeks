# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:20:34 2020

@author: aishw
"""

#code
import math
p,n=map(int, input().strip().split())
num=math.pow(n,1/p)
if num-int(num) == 0.0:
    print(int(num))
else:
    print(-1)

