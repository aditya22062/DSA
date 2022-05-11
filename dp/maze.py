def fun(n, m, arr):
    dp = [[0 for c in range(m)] for r in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j]=1
            elif i==n-1:
                dp[i][j]=dp[i][j+1]+arr[i][j]
            elif j==m-1:
                dp[i][j]=dp[i+1][j]+arr[i][j]
            else:
                dp[i][j]=min(dp[i][j+1],dp[i+1][j])+arr[i][j]
   
    return dp[0][0]


# driver code

def main():
    n = int(input())
    m = int(input())
    
    arr = []
    
    for i in range(0,n):
        ar=[]
        l=input()
        for j in range(0,m):
            lst=l.split(" ")
            val=int(lst[j])
            ar.append(val)
        arr.append(ar)
    
    
    
    print(fun(n, m, arr))
    
if __name__ == "__main__":
    main()