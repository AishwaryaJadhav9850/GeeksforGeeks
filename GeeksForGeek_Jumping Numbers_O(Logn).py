# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:25:46 2020

@author: aishw
"""
t=int(input())
while t>0:
    n=int(input())
    print(0,end=" ")
    l=[x for x in range(1,10)]
    while len(l)>0:
        temp=l.pop(0)
        if n<temp:
            continue
        print(temp,end=" ")
        lm=temp%10
        if lm>0:
            l.append(temp*10+(lm-1))
        if lm<9:
            l.append(temp*10+(lm+1))
        #print(l)
    print()
    t-=1