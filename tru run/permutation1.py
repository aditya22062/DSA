def permutation(idx,arr,k):
    if idx==k:
        for i in range(len(arr)):
            print(arr[i],end="")
        print()
        return

    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=idx
            permutation(idx+1,arr,k)
            arr[i]=0

n=int(input())
k=int(input())
arr=[0]*n
permutation(1,arr,k)