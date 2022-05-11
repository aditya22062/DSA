def fun(n, arr, dp):
    
    # write code here
    dp[n]=0
    for i in range(len(arr)-1,-1,-1):
        j=1
        ans=float('inf')
        while j<=arr[i] and i+j<=n:

            ans=min(ans,dp[i+j])+1
            j+=1
        dp[i]=ans
    print(dp) 
    return dp[0]


# driver code
def main():
    n = int(input())
    arr = []
    
    for i in range(0,n):
        arr.append(int(input()))
        
    dp = [0]*(n+1)
    
    print(fun(n, arr, dp))
    
if __name__ == "__main__":
    main()