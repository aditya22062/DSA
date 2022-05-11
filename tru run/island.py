def main():
    n = int(input())
    m = int(input())
    arr = []
    
    for i in range(n):
        values = list(map(int , input().split(" ")))
        arr.append(values)
    
    visited=[[False for j in range(m)]for i in range(n)]
    c=0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col]==0 and visited[row][col]==False:
                dfs(arr,row,col,visited)
                c+=1
    print(c)
def dfs(arr,row,col,visited):
    if (row< 0 or col< 0 or col >=len(arr[0]) or row>=len(arr) or arr[row][col]==1 or visited[row][col]==True):
        return False 
    
    visited[row][col]=True
    dfs(arr,row+1,col,visited)
    dfs(arr,row-1,col,visited)
    dfs(arr,row,col+1,visited)
    dfs(arr,row,col-1,visited)



    #write your code here

main()