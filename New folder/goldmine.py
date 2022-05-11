def fun(n, m, arr):
    dp = [ [0 for c in range(m)] for r in range(n) ]
    
    # write code here
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if  j==m-1:
                dp[i][j]=arr[i][j]
            elif i==0:
                dp[i][j]=arr[i][j]+max(dp[i][j+1],dp[i+1][j+1])
            elif i==n-1:
                dp[i][j]=arr[i][j]+max(dp[i][j+1],dp[i-1][j+1])
            else:
                dp[i][j]=arr[i][j]+max(dp[i][j+1],dp[i-1][j+1],dp[i][j+1])
    ans=0
    for i in range(n-1):
        ans=max(dp[i][0],ans)
    
    
    
    return ans





# driver code

def main():
    n = int(input())
    m = int(input())
    
    mine = []
    
    for i in range(0, n):
        a = []
        l = input()
        for j in range(0, m):
            lst = l.split(" ")
            val = int(lst[j])
            a.append(val)
        mine.append(a)
        

    print(fun(n, m, mine))
    
if __name__ == "__main__":
    main()