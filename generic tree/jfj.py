s=input()
dp=[[0 for j in range(len(s))]for i in range(len(s))]
for g in range(len(dp)):
    i,j=0,g
    while j <len(dp):
        if g==0:
            dp[i][j]=1
        elif g==1:
            if s[i]==s[j]:
                dp[i][j]=3
            else:
                dp[i][j]=2
        else:
            if s[i]==s[j]:
                dp[i][j]=dp[i-1][j-1]+dp[i+1][j]+1
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i+1][j]-dp[i+1][j-1]
print(dp[len(dp)-1][len(dp)-1])