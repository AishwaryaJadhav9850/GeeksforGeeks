# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:16:46 2020

@author: aishw
"""
#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        l=[]
        n=N
        sum=0
        while(n//10!=0):
            sum=sum+(n%10)
            n=n//10
        sum=sum+n
        while(sum//10!=0):
            l.append(sum%10)
            sum=sum//10
        l.append(sum)
        i=0
        j=len(l)-1
        while(i<j):
            if l[i]!=l[j]:
                return 0
            i+=1
            j-=1
        return 1
            
            
      
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends

