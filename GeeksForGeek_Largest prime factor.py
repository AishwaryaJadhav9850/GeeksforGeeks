# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:59:56 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        if N==1:
            return 1
        if N==2:
            return 2
        p=N
        n=(N//2)+1
        for i in range(2,n):
            if N==1:
                break
            while N%i==0:
                N=N//i
                p=i
        return p
        

if __name__ == '__main__': 
        N = int(input())    
        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends