# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:00:30 2020

@author: aishw
"""

def printPat(n):
    #Code here
    for i in range(n,0,-1):
        
        for j in range(n,0,-1):
            for k in range(i):
                print(j, end=" ")
                
        print("$",end ="")    
    

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))
