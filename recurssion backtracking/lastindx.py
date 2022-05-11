import sys
sys.setrecursionlimit (10000)
def Lastindex(arr,idx,x,n):
 # Write your code here
    a=Lastindex(arr,idx+1,x,n)
    if a==-1:
        if arr[idx]==x:
            return idx
        else:
            return -1
    else:
        return a
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    x=int(input())
    ans=Lastindex(arr,0,x,n)
    print(ans)
main()