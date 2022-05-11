from collections import deque 
class Edge:
    def __init__(self,src,nbr):
        self.src = src
        self.nbr = nbr
class pair:
    def __init__(self,v,psf) -> None:
        self.v=v
        self.psf=psf        
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
        e1 = Edge(v1 ,v2)
        e2 = Edge(v2 ,v1)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)
        
    src=int(input())
    #write your code here
    visited=[False]*vtces
    q=deque()
    q.append(pair(src,str(src)+""))
    while len(q)!=0:
        r=q.popleft()
        if visited[r.v]==True:
            continue
        visited[r.v]=True
        print(str(r.v)+"@"+r.psf)
        for e in graph[r.v]:
            if visited[e.nbr]==False:
                q.append(pair(e.nbr,r.psf+str(e.nbr)))
         


if __name__ == "__main__":
    main()
    
    