# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:11:12 2020

@author: aishw
"""

class Solution:
    def getTable(self,N):
        # code here
        j=[]
        for i in range(1,11):
            j.append(N*i)    
        return j




if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i,end=" ")
        print()
