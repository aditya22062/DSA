import sys
import math


def twoTransactions(arr,n):
    #write your code here
    mbsp=arr[0]
    msp=0
    dpl=[0]*n
    for i in range(1,len(arr)):
        mbsp=min(arr[i],mbsp)
        msp=arr[i]-mbsp
        dpl[i]=max(dpl[i-1],msp)
    rmbsp=arr[-1]
    rmsp=0
    dpr=[0]*n
    for i in range(len(arr)-2,-1,-1):
        rmbsp=max(arr[i],rmbsp)
        rmsp=rmbsp-arr[i]
        dpr[i]=max(dpr[i+1],rmsp)
    op=0
    for i in range(n):
        op=max(op,dpl[i]+dpr[i]) 
    print(dpl)
    print(dpr)
    print(op)   

def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    twoTransactions(array,n)

if __name__ == '__main__':
    main()
  