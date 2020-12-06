# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:29:33 2020

@author: aishw
"""
import math
#User function Template for python3
class Solution:
    
    def pairCubeCount(self, N):
        cnt=0
        for i in range(0,round(math.pow(N, 1/3))+ 1):        
            t=N-(i*i*i)
            ans=round(math.pow(abs(t),1/3))
            if ans ** 3 == t and t!=0:
                cnt+=1
                
        return cnt 

if __name__ == '__main__': 

        N=int(input())
        
        ob = Solution()
        print(ob.pairCubeCount(N))
# } Driver Code Ends