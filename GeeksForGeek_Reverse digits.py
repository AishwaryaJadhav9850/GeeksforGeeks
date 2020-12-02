# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:33:37 2020

@author: aishw
"""


class Solution:     
	def reverse_digit(self, n):
            n1=n
            while(n1%10==0):
                n1=n1//10
            n=n1    
            num=0
            while(n//10!=0):
                num=(num+(n%10))*10
                n=n//10
            num=num+n
            return num
        
if __name__ == '__main__':
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
