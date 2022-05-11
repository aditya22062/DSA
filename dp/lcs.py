def lcs(s1,s2,dp):
    for i in range(len(dp)-1,-1,-1):
        for j in range(len(dp[0])-1,-1,-1):
            if i==len(dp)-1 or j==len(dp[0])-1:
                dp[i][j]=0
            elif s1[i]==s2[j]:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])+1
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])
    print(dp[0][0])

s1=input()
s2=input()
dp=[[0 for i in range(len(s2)+1)]for j in range(len(s1)+1)]
lcs(s1,s2,dp)