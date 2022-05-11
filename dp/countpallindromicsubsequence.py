def pallindromicsubstring(n,dp):
    c=0
    for g in range(len(dp)):
        i,j=0,g
        while i <len(dp) and j <len(dp):
            if g==0:
                dp[i][j]=1
            elif g==1:
                if n[i]==n[j]:
                    dp[i][j]=True
                else:
                    dp[i][j]=False
            else:
                if n[i]==n[j] and dp[i+1][j-1]==True:
                    dp[i][j]=True
                else:
                    dp[i][j]=False
            if dp[i][j]:
                c+=1
            i+=1
            j+=1
    print(c)
n=input()
dp=[[0 for j in range(len(n))]for i in range(len(n))]
pallindromicsubstring(n,dp)