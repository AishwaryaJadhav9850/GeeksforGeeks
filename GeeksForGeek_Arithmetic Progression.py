# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:52:50 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def nthTermOfAP(self,A1,A2,N):
        #code here
        if N == 1:
            return A1
        elif N==2:
            return A2
        else:
            d=A2-A1
            k=A2
            
            k=k+((N-2)*d)
            return k



if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A1,A2,N=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.nthTermOfAP(A1,A2,N))  
