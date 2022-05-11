import sys
sys.setrecursionlimit (10000)
def allindices(arr,x,idx,fsf):
    if idx==len(arr):
        return []*(fsf+1)
    if arr[idx]==x:
        a=allindices(arr,x,idx+1,fsf+1)
        a[fsf]=idx
        return a
    else:
        a=allindices(arr,x,idx+1,fsf)
        return a
        
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    x=int(input())
    
    iarr=allindices(arr,x,0,0)
    
    for i in range(len(iarr)):
        print(iarr[i])
        
main()