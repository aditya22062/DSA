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
    printallpaths(graph,src,dest,visited,str(src)+"")

  # write your code here
def printallpaths(graph,src,dest,visited,asf):
    if src==dest:
        print(asf)
        return
    visited[src]=True
    for edge in graph[src]:
        if visited[edge.nbr]==False:
            printallpaths(graph,edge.nbr,dest,visited,str(asf)+str(edge.nbr))
    visited[src]=False



if __name__ == "__main__":
    main()