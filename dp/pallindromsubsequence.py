def pallindromesubsequence(s,dp):
    for g in range(len(dp)):
        i,j=0,g
        while i <len(dp) and j<len(dp):
            if g==0:
                dp[i][j]=1
            elif g==1:
                dp[i][j]= 3 if(s[i]==s[j]) else 2
            else:
                if s[i]==s[j]:
                    dp[i][j]=dp[i][j-1]+dp[i+1][j]-1
                else:
                    dp[i][j]=dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1]
            i+=1
            j+=1
    print(dp[0][len(s)-1])

s=input()
dp=[[0 for j in range(len(s))]for i in range(len(s))]
pallindromesubsequence(s,dp)