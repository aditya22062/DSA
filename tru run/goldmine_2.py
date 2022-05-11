def travelandcollectgold(arr,i,j,visited,bag):
    if i<0 or j<0 or i>=len(arr) or j >= len(arr[0]) or visited[i][j]==True:
        return


    visited[i][j]=True
    bag.append(arr[i][j])
    travelandcollectgold(arr,i-1,j,visited,bag)
    travelandcollectgold(arr,i+1,j,visited,bag)
    travelandcollectgold(arr,i,j-1,visited,bag)
    travelandcollectgold(arr,i,j+1,visited,bag)
def getMaxGold(arr):
    visited=[[False for i in range(len(arr[0]))] for j in range(len(arr))]
    max1=0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]!=0:
                bag=[]
                travelandcollectgold(arr,i,j,visited,bag)

                sum1=0
                for i in bag:
                    sum1+=i
                if sum1>max1:
                    max1=sum1
    return max1




n =int(input()) 
m = int(input()) 
arr=[]
for i in range(m):
    l=list(map(int,input().split()))
    arr.append(l)

print(getMaxGold(arr))

