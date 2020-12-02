# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:42:58 2020

@author: aishw
"""

def factorial(N):
    fact=1
    for i in range(1,N+1):
        fact=fact*i
    return fact


t=int(input())
while t>0:
    n,r=map(int, input().strip().split())
    nfact=factorial(n)
    rfact=factorial(n-r)
    print(nfact//rfact)
    t-=1
    
