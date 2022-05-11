n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
lis=[0]*n
lds=[0]*n
lis[0]=1
for i in range(1,n):
    maxi=0
    for j in range(i):
        if arr[j]<=arr[i]:
            maxi=max(lis[j],maxi)
    lis[i]=maxi+1
for i in range(n-1,-1,-1):
    maxi=0
    for j in range(n-1,i,-1):
        if arr[j]<=arr[i]:
            maxi=max(lds[j],maxi)
    lds[i]=maxi+1
omax=0
for i in range(n):
    omax=max(lds[i]+lis[i]-1,omax)
print(omax)