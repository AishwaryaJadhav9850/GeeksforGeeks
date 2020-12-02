# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:59:07 2020

@author: aishw
"""

#Your task is to complete this function
#Your shouldn't return any thing it should print the required output
def addFraction(num1, den1, num2, den2):
    if den1==den2:
        s=str(num1+num2)+"/"+str(den1)
        print(s)
    else:
        num=a=((den1*num2)+(den2*num1))
        den=b=den1*den2
        while a!=0 and b!=0:
            if a==b:
                gcd=a
                break
            elif a<b:
                b=b-a
            else:
                a=a-b
        if a==0:
            gcd=b
        elif b==0:
            gcd=a
        num=num//gcd
        den=den//gcd
        s=str(num)+"/"+str(den)
        print(s)
    




#{ 
#  Driver Code Starts
if __name__=='__main__':
        arr = list(map(int, input().strip().split(' ')))
        addFraction(arr[0], arr[1], arr[2], arr[3])

# } Driver Code Ends