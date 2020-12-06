# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:34:32 2020

@author: aishw
"""
#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
        if N<=1:
            return []
        k=[]
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
        for i in range(len(l)):
            if l[i]==True:
                k.append(i)
        return k


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends