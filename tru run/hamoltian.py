class Edge:
    def __init__(self,src,nbr):
        self.src = src
        self.nbr = nbr
    

def main():
    n1=input().split()
    vtces =int(n1[0])
    edges = int(n1[1])
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
    
    visited={}
    
    src=int(input())    
    # write  your code here
    print(hamiltonpath(graph,src,visited,src))
    
def hamiltonpath(graph,src,visited,osrc):
    if len(visited)==len(graph)-1:
        flag=True
        for e in graph[src]:
            if e.nbr==osrc:
                flag=False
                break
        return flag

    visited[src]=True
    for edge in graph[src]:
        if visited[edge.nbr]==False:
            hamiltonpath(graph,edge.nbr,visited,osrc)
    visited[src]=False

      
if __name__ == "__main__":
    main()