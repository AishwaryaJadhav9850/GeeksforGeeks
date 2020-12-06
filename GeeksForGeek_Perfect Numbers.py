# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:49:17 2020

@author: aishw
"""

#User function Template for python3

import math
class Solution:
    def isPerfectNumber(self, N):
        if N==1 or N==2:
            return 0
        num=1
        n=int(math.sqrt(N))+1
        for i in range(2,n+1):
            if N%i==0:
                num=num+i+(N//i)
                if num>N:
                    return 0
        if num==N:
            return 1
        else:
            return 0



if __name__ == '__main__': 
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends