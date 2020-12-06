# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:11:03 2020

@author: aishw
"""

#User function Template for python3

class Solution:
    def prime_Sum(self, N):
        if N<=1:
            return []
        l=[True for i in range(N+1)]
        l[0]=l[1]=False
        i=2
        while(i*i<=N):
            if i:
                j=i*i
                while j<=N:
                    #print(l,i,j)
                    if j%i==0:
                        l[j]=False
                    j+=i
            i+=1
        sum=0
        for i in range(len(l)):
            if l[i]==True:
                sum=sum+i                
        return sum


if __name__ == '__main__':
		n= int(input())
		ob = Solution()
		ans = ob.prime_Sum(n)
		print(ans)
# } Driver Code Ends