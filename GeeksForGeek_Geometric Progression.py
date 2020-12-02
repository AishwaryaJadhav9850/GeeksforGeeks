# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:09:42 2020

@author: aishw
"""
#User function Template for python3

class Solution:
	def Nth_term(self, a, r, n):
		# Code here
		return a*r*n
		    

if __name__ == '__main__':
    a,r,n=map(int,input().strip().split(' '))
    ob=Solution()
    ans = ob.Nth_term(a, r, n)
    print(ans)
    