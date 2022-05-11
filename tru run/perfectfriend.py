class Edge:
    def __init__(self, src, nbr):
        self.src = src
        self.nbr = nbr


def main():
    n = int(input())
    k = int(input())
    graph = {}
    for i in range(n):
        graph[i] = []

    for i in range(k):
        values = input().split(" ")
        v1 = int(values[0])
        v2 = int(values[1])

        e1 = Edge(v1, v2)
        e2 = Edge(v2, v1)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)
        visited=[False]*n
    comp=[]  
    for i in range(n):
        if visited[i]==False:
            c=[]
            getcomponent(graph,i,visited,c)
            comp.append(c)
    pairs=0
    for r in range(len(comp)):
        for j in range(r+1,len(comp)):
            count=len(comp[r])*len(comp[j])
            pairs+=count
    print(pairs) 
def getcomponent(graph,src,visited,c):
    
    visited[src]=True
    c.append(src)
    for e in graph[src]:
        if visited[e.nbr]==False:
            getcomponent(graph,e.nbr,visited,c)
    return c
if __name__ == "__main__":
    main()