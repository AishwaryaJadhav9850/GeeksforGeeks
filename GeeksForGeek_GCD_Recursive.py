# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:31:43 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def gcd(self, A, B):
        if A==0:
            return B
        if B==0:
            return A
        if A==B:
            return A
        if A<B:
            return self.gcd(A,B-A)
        else:
            return self.gcd(A-B,B)     

if __name__ == '__main__': 
        A,B = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(A,B))
