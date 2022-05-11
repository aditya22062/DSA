import math

def kTransactions(arr,n,k):
    
    dp=[[0 for j in range(n)]for i in range(k+1)]
    for i in range(1,len(dp)):
        maxi=float('-inf')
        for j in range(1,len(dp[0])):
            maxi=max(dp[i-1][j-1]-arr[j-1],maxi)
            dp[i][j]=max(maxi+arr[j],dp[i][j-1])
          
    
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
    