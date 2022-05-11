import sys
def minCost(arr, N ):
    # write your code here
    dp=[[0 for j in range(3)]for i in range(N)]
    dp[0][0]=arr[0][0]
    dp[0][1]=arr[0][1]
    dp[0][2]=arr[0][2]
    for i in range(1,len(arr)):
        dp[i][0]=arr[i][0]+min(dp[i-1][1],dp[i-1][2])
        dp[i][1]=arr[i][1]+min(dp[i-1][0],dp[i-1][2])
        dp[i][2]=arr[i][2]+min(dp[i-1][0],dp[i-1][1])
    print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))

n=int(input())
arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)
minCost(arr,n)
