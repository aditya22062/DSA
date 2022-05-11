n=int(input())
dp=[0]*(n+1)
dp[n]=1
for i in range(n-1,-1,-1):
    if n-i==1:
        dp[i]=dp[i+1]
    elif n-i==2:
        dp[i]=dp[i+2]+dp[i+1]
    else:
        dp[i]=dp[i+2]+dp[i+1]+dp[i+3]
print(dp[0])