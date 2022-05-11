from collections import deque
import threading , queue
class pair:
    def __init__(self,v,level):
        self.v=v
        self.level=level
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
    t = int(input())  
    # Write your code here
    visited=[0]*vtces
    q=deque()
    q.append(pair(src,1))
    c=0
    while len(q)>0:
        r=q.popleft()
        if visited[r.v]>0:
            continue
        visited[r.v]=r.level
        if r.level>t:
            break
        c+=1
        for e in graph[r.v]:
            if visited[e.nbr]==0:
                q.append(pair(e.nbr,r.level+1))

    print(r.level)
      
if __name__ == "__main__":
    main()