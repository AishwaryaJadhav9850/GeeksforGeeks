# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:39:12 2020

@author: aishw
"""

#User function Template for python3


class Solution:
    def factorial (self, N):
        fact=1
        for i in range(1,N+1):
            fact=fact*i
        return fact
            
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends