# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:09:03 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def closestNumber(self, N , M):
        # code here 
        n1=abs((abs(N)//M)*M)
        n2=abs(n1+M)
        if abs(abs(N)-n1) > abs(abs(N)-n2):      
            if N < 0:
                return -n2
            else:
                return n2
        else:
            if N < 0:
                return -n1
            else:
                return n1

if __name__ == '__main__':
    N,M=map(int,input().split())
    ob = Solution()
    print(ob.closestNumber(N,M))
