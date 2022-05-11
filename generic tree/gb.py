def unboundedknapSack(cap,wt,val,n):
    dp=[0]*(cap+1)
    dp[0]=0
    for i in range(1,len(dp)):
        max1=0
        for j in range(n):
            
            if i>=wt[j]:
                
                totalvalue=dp[i-wt[j]]+val[j]
                max1=max(max1,totalvalue)
        dp[i]=max1
    return dp[cap]
n = int(input())

st1 = input()
v=st1.split()
val=[int(i) for i in v]

st2 = input()
w = st2.split()
wt = [int(j) for j in w]

cap = int(input()) 
 
print(unboundedknapSack(cap, wt, val, n))