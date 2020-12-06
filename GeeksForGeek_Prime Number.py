# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:25:12 2020

@author: aishw
"""

#User function Template for python3
import math
class Solution:
    def isPrime (self, N):
        if N <=1:
            return 0
        for i in range(2,int(math.sqrt(N))+1):
            if N%i==0:
                return 0
        return 1
            
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends