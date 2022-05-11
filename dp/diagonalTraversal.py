def diagonalTravesal(arr):
    
    for g in range(len(arr)):
        i,j=0,g
        while i<len(arr) and j<len(arr):
            print(arr[i][j])
            i+=1
            j+=1
    
    
n=int(input())
arr=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j]=int(input())
diagonalTravesal(arr)