import sys
from typing import Sized

def kLargest(arr,size,k):
    
    # write your code here
    minheap=[]
    for i in range(k):
        minheap.append(arr[i])
    for i in range(k+1,len(arr)):
        mini=min(minheap)
        if mini<arr[i]:
            minheap.remove(mini)
            minheap.append(arr[i])
    print(minheap)
    
		
def main():
    ints = []
    n = int(input())
    ints=list(map(int,input().split()))
    size=len(ints)
    k=int(input())
    kLargest(ints, size, k)
    
if __name__ == '__main__':
    main()
    