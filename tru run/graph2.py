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
        e1 = Edge(int(values[0]), int(values[1]), int(values[2]))
        e2 = Edge(int(values[1]), int(values[0]), int(values[2]))
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)

    comps = []
    visited=[False]*vtces
    # write your code here
    for vtx in range(vtces):
        if visited[vtx]==False:
            ab=[]
            a=getcomponent(graph,vtx,ab,visited)
            comps.append(a)
    print(comps)
def getcomponent(graph,vtx,ab,visited):
    visited[vtx]=True
    ab.append(vtx)
    for vt in graph[vtx]:
        if visited[vt.nbr]==False:
            getcomponent(graph,vt.nbr,ab,visited)
    return ab

if __name__ == "__main__":
    main()