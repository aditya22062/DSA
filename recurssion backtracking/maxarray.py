import sys
sys.setrecursionlimit (10000)

def maxi(arr,idx,n):
    if idx==n-1:
        return arr[idx]
    
    ars=maxi(arr,idx+1,n)
    if arr[0]>ars:
        return arr[0]
    else:
        return ars


def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    res=maxi(arr,0,n)
    print(res)
main()