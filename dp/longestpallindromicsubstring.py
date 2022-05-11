def LongesPallindromicSubstring(n,dp):
    l=0
    for g in range(len(n)):
        i,j=0,g
        while i <len(n) and j <len(n):
            if g==0:
                dp[i][j]=True
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
                l=g+1
            i+=1
            j+=1
    print(l)    
n=input()
dp=[[False for j in range(len(n))]for i in range(len(n))]
LongesPallindromicSubstring(n,dp)