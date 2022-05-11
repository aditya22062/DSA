def targetSumPair(arr,target,n):
    #write your code here
    dp=[[False for j in range(target+1)]for i in range(n+1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i ==0 and j==0:
                dp[i][j]==True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True
            else:
                if dp[i-1][j]==True:
                    dp[i][j]=True
                else:
                    val=arr[i-1]
                    if val>j:
                        if dp[i-1][j-val]==True:
                            dp[i][j]=True

    print(dp[len(arr)][target])




n=int(input())
arr=[]
for i in range(0,n):
    val=int(input())
    arr.append(val)
target=int(input())
targetSumPair(arr,target,n)