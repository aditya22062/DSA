import heapq
import threading 


class Edge:
    def __init__(self,src,nbr,wt):
        self.src = src
        self.nbr = nbr
        self.wt=wt


    

def main():
    vtces = int(input())
    edges = int(input()) 
    graph = {}
    for i in range(vtces):
        graph[i] = []
    
    for i in range(edges): 
        lines = input().split(" ")
        v1=int(lines[0])
        v2=int(lines[1])
        wt=int(lines[2])
        e1 = Edge(v1 ,v2 ,wt)
        e2 = Edge(v2 ,v1 ,wt)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)
        
    src = int(input())
    dest=int(input())
    visited=[False]*(vtces)
    q=[]
    heapq.heappush(q,(0,str(src)+"",src))
    while len(q)>0:
        cost,psf,veticess=heapq.heappop(q)
        
            
        visited[veticess]=True
        if visited[veticess]==True and veticess==dest:
            print(heapq.heappop(q))
        

        for e in graph[veticess]:
            if visited[e.nbr]==False :
                heapq.heappush(q,(e.wt+cost,psf+str(e.nbr),e.nbr))
            
    
    #write your code here
   
if __name__ == '__main__':
    main()
      
    