# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:21:15 2020

@author: aishw
"""

class Solution:
    def gcd(self, a, b):
        while a!=0 and b!=0:
            if a==b:
                return a
            elif a<b:
                b=b-a
            else:
                a=a-b
        if a==0:
            return b
        elif b==0:
            return a
        
            

if __name__ == '__main__': 
        A,B = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(A,B))