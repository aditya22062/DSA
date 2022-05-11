import math

def kTransactions(arr,n,k):
    
    dp=[[0 for j in range(n)]for i in range(k+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            maximum=dp[i][j-1]
            
            for f in range(j):
                ptp=dp[i-1][f]
                profittill=arr[j]-arr[f]+ptp
                maximum=max(profittill,maximum)

            dp[i][j]=maximum
    print(dp)
    print(dp[k][n-1])
def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    k = int(input())
    kTransactions(array,n,k)

if __name__ == '__main__':
    main()
    