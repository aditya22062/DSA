def unbounded_knapSack(cap, wt, val, n):
    dp=[0]*(cap+1)
    dp[0]=0
    for i in range(1,len(dp)):
        maxi=0
        for j in range(n):
            if wt[j]<=i:
                totalval=dp[i-j]+val[j]
                maxi=max(maxi,totalval)
        
        dp[i]=maxi
    print(dp)
    return dp[cap]
# write your code here

n = int(input())

st1 = input()
v=st1.split()
val=[int(i) for i in v]

st2 = input()
w = st2.split()
wt = [int(j) for j in w]

cap = int(input()) 
 
print(unbounded_knapSack(cap, wt, val, n))