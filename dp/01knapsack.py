def zeroknapSack(cap, wt, val, n):
    
    # write your code here
    dp=[[0 for c in range(cap+1)]for r in range(n+1) ]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j]=dp[i-1][j]
            if j>=wt[i-1]:
                if (dp[i-1][j-wt[i-1]]+val[i-1]>dp[i-1][j]):
                    dp[i][j]=dp[i-1][j-wt[i-1]]+val[i-1]
                else:
                    dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return (dp[n][cap])
 
n = int(input())

st1 = input()
v=st1.split()
val=[int(i) for i in v]

st2 = input()
w = st2.split()
wt = [int(j) for j in w]

cap = int(input()) 
 
print(zeroknapSack(cap, wt, val, n))