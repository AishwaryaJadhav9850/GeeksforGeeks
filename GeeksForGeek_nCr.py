# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:10:59 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def nCr(self, n, r):
        
        if r>n:
            return 0
        
        r=n-r
        
        if r==0 or r==n:
            return 1
        
        if r==1:
            return n
        
        num=1
        for i in range(r):
            num=num*n
            n-=1
        
        fact=1
        for i in range(1,r+1):
            fact=fact*i
           
        return ((num//fact)%1000000007)




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends