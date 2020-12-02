# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:49:25 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def gcd(self, n, arr):
        # code here 
        
        if n==1:
            return arr[0]
        gcd=arr[0]
        arr.sort()
        for i in range(1,n):
            a=arr[i-1]
            b=arr[i]
            if a==b:
                continue
            while a!=0 and b!=0:
                if a==b:
                    gcd=a
                    arr[i]=a
                    break
                elif a<b:
                    b=b-a
                else:
                    a=a-b
            if a==0:        
                gcd=b
                arr[i]=b
            elif b==0:     
                gcd=a
                arr[i]=a
            if gcd==1:
                break
        return gcd



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(n,arr))
# } Driver Code Ends