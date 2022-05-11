def targetSumPair(arr,target):
    #write your code here
    dp=[[False for j in range(target+1)]for i in range(len(arr)+1)]

    for i in range(len(arr)+1):
        for j in range(target+1):
            if i==0 and j==0:
                dp[i][j]=True
            elif j==0:
                dp[i][j]=True
            else:
                if dp[i-1][j] ==True or dp[i-1][j-arr[i-1]]==True:
                    dp[i][j]=True
    print(dp)
    print(dp[len(arr)][target])
        
                
                
n=int(input());
arr=[];
for i in range(0,n):
    val=int(input());
    arr.append(val);
target=int(input());
targetSumPair(arr,target);