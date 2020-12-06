# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:39:15 2020

@author: aishw
"""

t=int(input())
while t>0:
    N=int(input())
    
    l=[True for i in range(N+1)]
    l[0]=l[1]=False
    
    i=2
    while(i*i<=N):
        if i:
            j=i*i
            while j<=N:
                #print(l,i,j)
                if j%i==0:
                    l[j]=False
                j+=i
        i+=1
    
    k=[]
    for i in range(len(l)):
        if l[i]==True:
            k.append(i)
    #print(k)
    i=0
    while k[i]<=N//2:
        j=0
        while k[j]<=N//2:
            if (k[i]*k[j])<=N:
                print(k[i],k[j],end=" ")
            else:
                break
            j+=1
        i+=1
    
    t-=1