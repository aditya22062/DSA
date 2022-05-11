c=0
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        mergesort(arr,0,n-1)
        return c

def merge2sortedarray(left,right):
    global c
    i=0
    j=0
    k=0
    merged=[]
    while i <len(left) and j <len(right):
        if left[i]<=right[j]:
            merged[k]=left[i]
            i+=1
            k+=1
        else:
            merged[k]=right[j]
            j+=1
            k+=1
            c+=len(left)-i
    while i <len(left):
        merged[k]=left[i]
        i+=1
        k+=1
    while j <len(right):
        merged[k]=right[j]
        j+=1
        k+=1
    return merged
def mergesort(arr,l,r):
    if l==r:
        ba=[]
        ba.append(arr[l])
        return ba
    mid=(l+r)//2
    left=mergesort(arr,l,mid)
    right=mergesort(arr,mid+1,r)
    merge=merge2sortedarray(left,right)
    return merge
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends