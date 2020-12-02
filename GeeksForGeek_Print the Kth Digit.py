# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:05:24 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def kthDigit(self, A, B, K):
        n=pow(A, B)
        k=1
        while n//10!=0 :
        # code here
            num=n%10
            n=n//10
            if k==K :
                return num
            k+=1            
        return n
            




if __name__ == '__main__':
    A,B,K = input().split()
    ob = Solution()
    print(ob.kthDigit(int(A),int(B),int(K)))
    

