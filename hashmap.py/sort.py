
import heapq 
d={}

array=list(map(int,input().split()))
k=int(input())
for i in array:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
arr=[array[0]]
heapq.heapify(arr)
for i in range(1,len(array)):
    if d[array[i]]>d[array[i-1]]:
        heapq.heappop()
print(arr)
