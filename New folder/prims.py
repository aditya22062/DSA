import threading 
import heapq


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
        
        #Write your code here
    q=[]
    visited=[False]*vtces
    heapq.heappush(q,(0,0,-1))
    while len(q)>0:
        cost,vetex,avetex=heapq.heappop(q)
        if visited[vetex]==True:
            continue
        visited[vetex]=True
        if avetex!=-1:
            print("["+str(vetex)+"-"+str(avetex)+"@"+str(cost)+"]")

        for e in graph[vetex]:
            if visited[e.nbr]==False:
                heapq.heappush(q,(e.wt,e.nbr,vetex))

if __name__ == '__main__':
    main()