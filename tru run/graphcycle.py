from collections import deque 
class Edge:
    def __init__(self,src,nbr):
        self.src = src
        self.nbr = nbr
class pair:
    def __init__(self,v):
        self.v=v
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
    visited=[False]*vtces
    flag=False
    for v in range(vtces):
        if visited[v]==False:
            if isCyclic(graph,v,visited):
                flag=True
                break
    if flag==True:
        print("true")
    else:
        print("false")
            

def isCyclic(graph,src,visited):
    q=deque()
    q.append(pair(src))
    while len(q)>0:
        r=q.popleft()
        if visited[r.v]==True:
            return True
        visited[r.v]=True
        for e in graph[r.v]:
            if visited[e.nbr]==False:
                q.append(pair(e.nbr))
    return False           
    #write your code here
      
if __name__ == "__main__":
    main()