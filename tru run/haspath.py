class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt


def main():
    vtces = int(input())
    edges = int(input())
    graph = {}
    for i in range(vtces):
        graph[i] = []

    for i in range(edges):
        values = input().split(" ")
        v1 = int(values[0])
        v2 = int(values[1])
        wt = int(values[2])
        e1 = Edge(v1, v2, wt)
        e2 = Edge(v2, v1, wt)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)

    src = int(input())
    dest = int(input())
    visited=[False]*vtces
    haspath(graph,src,dest,visited)
  # write your code here
def haspath(graph,src,dest,visited):

    if src==dest:
        return True
    visited[src]=True
    for edge in graph[src]:
        if visited[edge.nbr]==False:
            a=haspath(graph,edge.nbr,dest,visited)
            if a==True:
                return True
        
    
    return False






if __name__ == "__main__":
    main()