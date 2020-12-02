# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:34:52 2020

@author: aishw

0 1 2 3 4 5 6 7 8 9 10
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45

"""

T=int(input())
while(T>0):
    a=0
    n = int(input())
    while a<=n and a<=10:
        print(a,end=" ")
        a+=1
    if a>n:
        continue
    for i in range(11,n+1):
            #print(i)
            k=i
            flag=0
            while k//10!=0:
                r=k%10
                k=k//10
                if k//10!=0:
                    m=k%10
                    if r+1!=m and r-1!=m:
                        flag=1
                        break              
            if flag==0:
                if r+1==k or r-1==k:
                    print(i,end=" ")
    T-=1
    print()

