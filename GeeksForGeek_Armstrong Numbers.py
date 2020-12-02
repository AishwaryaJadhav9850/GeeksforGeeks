# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:14:43 2020

@author: aishw
"""

class Solution:
    def armstrongNumber (ob, n):
        # code here
        sum=0
        num=n
        while(n//10!=0):
            r=n%10
            n=n//10
            sum=sum+(r*r*r)
        sum=sum+(n*n*n)    
        if sum==num:
            return "Yes"
        else:
            return "No"



if __name__ == '__main__': 
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
