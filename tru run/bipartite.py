from collections import deque
class Edge:
    def __init__(self,src,nbr):
        self.src = src
        self.nbr = nbr
class pair:
    def __init__(self,v,level):
        self.v=v
        self.level=level
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
        e1 = Edge(v1 ,v2 )
        e2 = Edge(v2 ,v1 )
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)
        
    # write your code here
    visited=[-1]*vtces
    for v in range(vtces):
        if visited[v]==-1:
            a=bipartite(graph,v,visited)
            if a==False:
                print("false")
                return
    print("true")
def bipartite(graph,src,visited):
    q=deque()
    q.append(pair(src,0))
    while len(q)>0:
        r=q.popleft()
        if visited[r.v]!=1:
            if r.level!=visited[r.v]:
                return False
        else:
            visited[r.v]=r.level
        for e in graph[r.v]:
            if visited[e.nbr]==1:
                q.append(pair(e.nbr,r.level+1))
    return True
      
if __name__ == "__main__":
    main()