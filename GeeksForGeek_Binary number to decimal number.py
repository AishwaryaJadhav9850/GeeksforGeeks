# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:19:15 2020

@author: aishw
"""

class Solution:
    def binary_to_decimal(self, str):
        l=list(str)
        l=l[::-1]
        sum=0
        for i in range(len(l)):
            if l[i]=='1':
                sum=sum+pow(2,i)
        return sum

if __name__ == '__main__':
    str = input()
    ob = Solution()
    ans = ob.binary_to_decimal(str)
    print(ans)
    
   
    

