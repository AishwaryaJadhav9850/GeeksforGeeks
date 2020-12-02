# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:35:21 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def lcmAndGcd(self, a , b):
        # code here 
        A=a
        B=b
        l=[-1,-1]
        while a!=0 and b!=0:
            if a==b:
                l[1]=a
                break
            elif a<b:
                b=b-a
            else:
                a=a-b
        if a==0:
            l[1]=b
        elif b==0:
            l[1]=a
        l[0]=(A*B)//l[1]
        return l


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
